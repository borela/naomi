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
    package_path,
)

from Naomi.system.headers import (
    indentation as indentation_header,
    plist as plist_header,
)

from Naomi.system.logging import get_logger
from Naomi.system.util import to_plist_string
from sublime_plugin import ApplicationCommand

def build():
    logger = get_logger()
    logger.debug('Cleaning: %s' % package_path(INDENTATION_BUILD_DIR))

    delete_dir_contents(INDENTATION_BUILD_DIR)

    logger.info('Building indentation preferences...')

    for file in list_files(INDENTATION_SRC_DIR):
        destination = file
        destination = destination.replace('src', 'build')
        destination = destination.replace('.yml', '.tmPreferences')

        logger.debug('Building file: %s' % package_path(file))

        data = load_yaml(file)
        plistString = to_plist_string(data)

        write_file(
            destination,
            plist() + indentation_header() + plistString
        )

    logger.info('Done building indentation preferences.')


class NaomiBuildIndentationPreferencesCommand(ApplicationCommand):
    def run(self):
        build()
