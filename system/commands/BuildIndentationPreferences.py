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

from Naomi.system.fs import (
    delete_dir_contents,
    list_files,
    load_yaml,
    to_plist_string,
    write_file,
)

from Naomi.system.paths import (
    INDENTATION_BUILD_DIR,
    INDENTATION_SRC_DIR,
)

from Naomi.system.headers import INDENTATION as INDENTATION_HEADER
from sublime_plugin import ApplicationCommand


class NaomiBuildIndentationPreferencesCommand(ApplicationCommand):
    def run(self):
        delete_dir_contents(INDENTATION_BUILD_DIR)

        for file in list_files(INDENTATION_SRC_DIR):
            destination = file
            destination = destination.replace('src', 'build')
            destination = destination.replace('.yml', '.temp')
            # destination = destination.replace('.yml', '.tmPreferences')

            data = load_yaml(file)
            plistString = to_plist_string(data)
            write_file(destination, plistString)
