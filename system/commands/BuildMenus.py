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

from Naomi.system.compilers.menus import compile_menus
from Naomi.system.state import STORE
from sublime_plugin import ApplicationCommand


class NaomiBuildMenusCommand(ApplicationCommand):
    def description(self):
        return 'Build Menus'

    def run(self):
        compile_menus(
            STORE['directories']['integration']['menus']['src'],
            STORE['directories']['integration']['menus']['build'],
        )
