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
    EVENT_BUS,
    log_error,
    log_info,
    STATE_STORE,
)

from Naomi.system.events import (
    building_syntaxes,
    finished_building_syntaxes,
)

from .Syntax import Syntax


def compile_syntaxes():
    EVENT_BUS.emit(building_syntaxes())

    for syntax_settings in STATE_STORE['settings']['syntaxes']:
        names = syntax_settings.get('names', None)

        if not names:
            log_info('Compiling syntax: %s' % entry)
        else:
            log_info('Compiling syntax for: %s' % names)

        syntax = Syntax(syntax_settings)
        # TODO: Save to a file.

    EVENT_BUS.emit(finished_building_syntaxes())
