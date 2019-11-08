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

from .statements import (
    ContextDeclaration,
    VariableDeclaration,
)

from Naomi.system import package_relpath
from Naomi.system.event_bus import EVENT_BUS
from Naomi.system.headers import syntax as syntax_header
from Naomi.system.state import STORE


class Syntax:
    path = None
    resolved_path = None
    package_relpath = None
    raw = None

    name = None
    file_extensions = None
    first_line_match = None
    hidden = None
    scope = None

    variables = []
    contexts = []


    def __init__(self, path):
        self.path = path
        self.resolved_path = resolve_path(path)
        self.package_relpath = package_relpath(self.resolved_path)
        self._load()
        self._compile()

    def _load(self):
        log_debug('Loading syntax file: %s' % self.package_relpath)

        self.raw = load_yaml(self.resolved_path)

        self.name = self.raw.get('name', '')
        self.scope = self.raw.get('scope', '')
        self.file_extensions = self.raw.get('file_extensions', [])
        self.first_line_match = self.raw.get('first_line_match', '')
        self.hidden = self.raw.get('hidden', '')

        log_debug('Done loading syntax file: %s' % self.package_relpath)

    def _compile(self):
        log_debug('Compiling syntax file: %s' % self.package_relpath)

        for name, raw in self.raw.get('variables', []).items():
            self.variables.append(VariableDeclaration(name, raw))

        for name, raw in self.raw.get('contexts', []).items():
            self.contexts.append(ContextDeclaration(name, raw))

        log_debug('Done compiling syntax file: %s' % self.package_relpath)
