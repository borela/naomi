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
    load_yaml,
    list_files,
    write_file,
)

from Naomi.system.headers import (
    preferences as preferences_header,
    plist as plist_header,
)

from Naomi.system.paths import (
    modify_path,
    package_path,
)

from Naomi.system.logging import get_logger
from Naomi.system.utils import to_plist_string


def compile_preferences(target_dir_path, output_dir_path):
    logger = get_logger()
    logger.debug('Cleaning: %s' % package_path(output_dir_path))

    delete_dir_contents(output_dir_path)

    logger.info('Compiling preferences...')

    for file_path in list_files(target_dir_path):
        relative_file_path = package_path(file_path)
        destination = modify_path(
            file_path,
            old_base=target_dir_path,
            new_base=output_dir_path,
            new_extension='tmPreferences',
        )

        logger.debug('Processing: %s' % relative_file_path)

        data = load_yaml(file_path)

        if  data is None:
            logger.debug('Empty file: %s' % relative_file_path)
            continue

        plist_string = to_plist_string(data)
        final_string = plist_header() + preferences_header() + plist_string

        write_file(destination, final_string)

        logger.debug('Done processing: %s' % relative_file_path)

    logger.info('Done compiling preferences.')
