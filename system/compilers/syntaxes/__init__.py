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

from Naomi.system.logging import (
    log_error,
    log_info,
)

from Naomi.system.events import (
    building_syntaxes,
    finished_building_syntaxes,
)

from .Syntax import Syntax
from Naomi.system import EVENT_BUS
from Naomi.system.state import STORE


def compile_syntax(syntax_settings):
    names = syntax_settings.get('names', None)
    entry = syntax_settings.get('entry', None)

    if not isinstance(entry, str) or not entry:
        log_error('Configured syntax has no entry.')
        return

    if not names:
        log_info('Compiling syntax: %s' % entry)
    else:
        log_info('Compiling syntax for: %s' % names)

    syntax = Syntax(entry)
    # TODO: Save to a file.


def compile_syntaxes():
    EVENT_BUS.emit(building_syntaxes())

    for syntax in STORE['settings']['syntaxes']:
        compile_syntax(syntax)

    EVENT_BUS.emit(finished_building_syntaxes())
