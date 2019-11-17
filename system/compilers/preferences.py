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

from borela import (
    delete_dir_contents,
    list_files,
    load_yaml,
    modify_path,
    to_plist_string,
    write_text_file,
)

from Naomi.system.headers import (
    preferences as preferences_header,
    plist as plist_header,
)

from Naomi.system import (
    EVENT_BUS,
    log_debug,
    log_info,
    package_relpath,
)

from Naomi.system.events import (
    building_preferences,
    finished_building_preferences,
)

# Convert preferences from “x.yml” to “x.tmPreferences”.
def compile_preferences(src_dir, build_dir):
    EVENT_BUS.emit(building_preferences())
    log_debug('Cleaning: %s' % package_relpath(build_dir))

    delete_dir_contents(build_dir)

    log_info('Compiling preferences...')

    for file_path, _, _ in list_files(src_dir):
        relative_file_path = package_relpath(file_path)
        destination = modify_path(
            file_path,
            old_base=src_dir,
            new_base=build_dir,
            new_extension='tmPreferences',
        )

        log_debug('Processing: %s' % relative_file_path)

        data = load_yaml(file_path)

        if data is None:
            log_debug('Empty file: %s' % relative_file_path)
            continue

        plist_string = to_plist_string(data)
        final_string = (
            plist_header()
            + preferences_header(src_dir)
            + plist_string
        )

        write_text_file(destination, final_string)
        log_debug('File generated: %s' % package_relpath(destination))

    log_info('Done compiling preferences.')
    EVENT_BUS.emit(finished_building_preferences())
