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

from Naomi.system import (
    log_debug,
    log_info,
    package_relpath,
)

from .ast import Syntax
from .parse_variables import parse_variables
from .parse_contexts import parse_contexts
from borela.functions import load_yaml
from os.path import dirname


def parse_syntax(path, src_dir, build_dir, settings):
    syntax = Syntax(settings)

    syntax.path = path
    syntax.home_dir = src_dir
    syntax.build_dir = build_dir
    syntax.parent_dir = dirname(path)
    syntax.package_relpath = package_relpath(path)

    syntax.index_file(syntax)

    log_debug('Loading syntax file: %s' % syntax.package_relpath)

    raw = load_yaml(syntax.path)
    syntax.raw = raw

    log_debug('Done loading syntax file: %s' % syntax.package_relpath)

    syntax.name = raw.get('name', '')
    syntax.hidden = raw.get('hidden', '')
    syntax.scope = raw.get('scope', '')
    syntax.scope_suffix = raw.get('scope_suffix', '')
    syntax.file_extensions = raw.get('file_extensions', [])
    syntax.first_line_match = raw.get('first_line_match', '')

    log_debug('Parsing variables: %s' % syntax.package_relpath)

    parse_variables(syntax)

    log_debug('Parsing contexts: %s' % syntax.package_relpath)

    parse_contexts(syntax)

    log_info('Done parsing: %s' % syntax.package_relpath)

    return syntax
