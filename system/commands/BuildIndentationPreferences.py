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
    write_file,
)

from Naomi.system.paths import (
    INDENTATION_BUILD_DIR,
    INDENTATION_SRC_DIR,
)

from Naomi.system.headers import indentation as indentation_header
from Naomi.system.util import to_plist_string
from sublime_plugin import ApplicationCommand


XML_VERSION = '<?xml version="1.0" encoding="utf-8"?>\n'
DOCTYPE = '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'


def build():
    delete_dir_contents(INDENTATION_BUILD_DIR)

    for file in list_files(INDENTATION_SRC_DIR):
        destination = file
        destination = destination.replace('src', 'build')
        destination = destination.replace('.yml', '.tmPreferences')

        data = load_yaml(file)
        plistString = to_plist_string(data)

        write_file(
            destination,
            XML_VERSION + DOCTYPE + indentation_header() + plistString
        )


class NaomiBuildIndentationPreferencesCommand(ApplicationCommand):
    def run(self):
        build()
