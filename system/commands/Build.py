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

from Naomi.system.compilers import (
    compile_configured_syntaxes,
    compile_integrated_commands,
    compile_integrated_keymaps,
    compile_integrated_menus,
    compile_integrated_preferences,
)

from sublime_plugin import ApplicationCommand

COMPILERS = {
    'syntaxes': compile_configured_syntaxes,
    'commands': compile_integrated_commands,
    'keymaps': compile_integrated_keymaps,
    'menus': compile_integrated_menus,
    'preferences': compile_integrated_preferences,
}

class NaomiBuildCommand(ApplicationCommand):
    def description(self, what):
        return 'Build %s' % what.title()

    def run(self, what):
        COMPILERS[what]()
