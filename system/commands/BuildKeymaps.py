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

from Naomi.system.paths import (
    KEYMAPS_BUILD_DIR,
    KEYMAPS_SRC_DIR,
)

from Naomi.system.compilers.keymap import compile_keymaps
from Naomi.system.fs import list_files
from sublime_plugin import ApplicationCommand


class NaomiBuildKeymapsCommand(ApplicationCommand):
    def run(self):
        compile_keymaps(
            [file for file in list_files(KEYMAPS_SRC_DIR)],
            KEYMAPS_BUILD_DIR,
        )
