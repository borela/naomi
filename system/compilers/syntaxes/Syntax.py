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

from borela.functions import load_yaml
from Naomi.system import log_info
from Naomi.system import package_relpath


class Syntax:
    path = None
    package_relpath = None
    settings = None
    raw = None

    name = None
    file_extensions = None
    first_line_match = None
    hidden = None
    scope = None
    scope_suffix = None

    variables = []
    contexts = []

    def __init__(self, path, settings):
        self.path = path
        self.package_relpath = package_relpath(path)
        self.settings = settings

        log_info('Loading syntax file: %s' % self.package_relpath)

        self.raw = load_yaml(path)

        self.name = self.raw.get('name', '')
        self.scope = self.raw.get('scope', '')
        self.scope_suffix = self.raw.get('scope_suffix', '')
        self.file_extensions = self.raw.get('file_extensions', [])
        self.first_line_match = self.raw.get('first_line_match', '')
        self.hidden = self.raw.get('hidden', '')

        log_info('Done loading syntax file: %s' % self.package_relpath)
        log_info('Compiling syntax file: %s' % self.package_relpath)

        for name, raw in self.raw.get('variables', []).items():
            self.variables.append(VariableDeclaration(self, name, raw))

        for name, raw in self.raw.get('contexts', []).items():
            self.contexts.append(ContextDeclaration(self, name, raw))

        log_info('Done compiling syntax file: %s' % self.package_relpath)
