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

from Naomi.system.compilers.indentation_preferences import (
    compile_indentation_preferences
)

from Naomi.system.paths import (
    INDENTATION_BUILD_DIR,
    INDENTATION_SRC_DIR,
)

from sublime_plugin import ApplicationCommand


class NaomiBuildIndentationPreferencesCommand(ApplicationCommand):
    def run(self):
        compile_indentation_preferences(
            INDENTATION_SRC_DIR,
            INDENTATION_BUILD_DIR,
        )
