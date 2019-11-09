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

from .statements import (
    ContextDeclaration,
    VariableDeclaration,
)

from Naomi.system import (
    package_relpath,
    resolve_path,
)

from borela.functions import load_yaml
from Naomi.system import log_info


class Syntax:
    settings = None

    path = None
    resolved_path = None
    package_relpath = None
    raw = None

    name = None
    file_extensions = None
    first_line_match = None
    hidden = None
    scope = None
    scope_suffix = None

    variables = []
    contexts = []

    def __init__(self, settings):
        self.settings = settings

        entry = settings.get('entry', None)

        if not isinstance(entry, str) or not entry:
            log_error('Configured syntax has no entry.')
            return

        self.path = entry
        self.resolved_path = resolve_path(path)
        self.package_relpath = package_relpath(self.resolved_path)

        log_info('Loading syntax file: %s' % self.package_relpath)

        self.raw = load_yaml(self.resolved_path)

        self.name = self.raw.get('name', '')
        self.scope = self.raw.get('scope', '')
        self.scope_suffix = self.raw.get('scope_suffix', '')
        self.file_extensions = self.raw.get('file_extensions', [])
        self.first_line_match = self.raw.get('first_line_match', '')
        self.hidden = self.raw.get('hidden', '')

        log_info('Done loading syntax file: %s' % self.package_relpath)
        log_info('Compiling syntax file: %s' % self.package_relpath)

        for name, raw in self.raw.get('variables', []).items():
            self.variables.append(VariableDeclaration(name, raw))

        for name, raw in self.raw.get('contexts', []).items():
            self.contexts.append(ContextDeclaration(name, raw))

        log_info('Done compiling syntax file: %s' % self.package_relpath)
