# Licensed under the Apache License, Version 2.0 (the “License”); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from borela import (
    delete_dir_contents,
    list_files,
    load_yaml,
    to_json_string,
    write_text_file,
)

from .ast import FunctionCall
from .CompilationError import CompilationError
from .generator import generate_dict
from .optimizer import optimize
from .parser import parse
from .transformer import transform
from borela.functions import dict_to_yaml_string
from hashlib import sha512
from Naomi.system import log_error
from os.path import join
from ruamel.yaml.constructor import DuplicateKeyError

def cleanup_unneeded_syntaxes(hashes):
    # TODO:..
    pass

def compile_syntax(settings, integrated_syntaxes):
    try:
        compilation = parse(
            settings,
            integrated_syntaxes,
        )

        transform(compilation)
        optimize(compilation)

        hashes = []
        names = settings.get('names')
        syntax = generate_dict(compilation)
        build_dir = compilation.build_dir

        if isinstance(names, list):
            for name in names:
                syntax['name'] = name
                hashes.append(generate_file(build_dir, syntax))
        else:
            hashes.append(generate_file(build_dir, syntax))

        cleanup_unneeded_syntaxes(hashes)
    except CompilationError as error:
        log_error(str(error))
    except DuplicateKeyError as error:
        lc = error.problem_mark
        log_error('(%i, %i) Duplicated key.' % (
            lc.line + 1,
            lc.column + 1,
        ))

def generate_file(build_dir, syntax):
    contents = dict_to_yaml_string(syntax)
    name_hash = sha512(syntax['name'].encode())
    file_name = '%s.yml' % name_hash.hexdigest()
    write_text_file(
        join(build_dir, file_name),
        contents,
    )
    return name_hash
