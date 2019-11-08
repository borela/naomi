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

from Naomi.system.logging import (
    log_debug,
    log_error,
    log_info,
    log_warning,
)

from Naomi.system.events import (
    building_syntaxes,
    finished_building_syntaxes,
)

from os.path import (
    isabs,
    join,
    realpath,
)

from .Syntax import Syntax
from Naomi.system import package_relpath
from Naomi.system.event_bus import EVENT_BUS
from Naomi.system.headers import syntax as syntax_header
from Naomi.system.state import STORE

def compile_syntaxes():
    EVENT_BUS.emit(building_syntaxes())

    for syntax in STORE['settings']['syntaxes']:
        compile_syntax(syntax)

    EVENT_BUS.emit(finished_building_syntaxes())

    # syntaxes = get_setting('syntaxes', [])

    # for syntax in syntaxes:
    #     name = syntax['name']
    #     entry = syntax['entry']
    #     output = syntax['output']
    #     features = syntax['features']

    #     entry = realpath(join(dir_path, entry))
    #     if not isfile(entry):
    #         log_error('Entry not found: %s' % entry)
    #         continue

    #     output = realpath(join(dest_dir_path, output))


def compile_syntax(syntax_settings):
    names = syntax_settings.get('names', None)
    entry = syntax_settings.get('entry', None)

    if not isinstance(entry, str) or not entry:
        log_error('Configured syntax has no entry.')
        return

    log_info('Compiling syntax for: %s' % names)

    syntax = Syntax(entry)
    # syntax.compile()


def resolve_path(path):
    """
    Resolve relative paths to the syntaxes src directory.
    """
    if not isabs(path):
        path = join(STORE['directories']['syntaxes']['src'], path)
    return realpath(path)
