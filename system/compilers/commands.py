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
    modify_path,
    package_path,
)

from Naomi.system.logging import (
    log_debug,
    log_info,
)

from Naomi.system.headers import command as command_header
from Naomi.system.utils import to_json_string


def compile_commands(dir_path, dest_dir_path):
    """
    Convert commands from “x.yml” to “x.sublime-commands”.
    """

    log_debug('Cleaning: %s' % package_path(dest_dir_path))

    delete_dir_contents(dest_dir_path)

    log_info('Building command files...')

    for file in list_files(dir_path):
        destination = modify_path(
            file,
            old_base=dir_path,
            new_base=dest_dir_path,
            new_extension='sublime-commands',
        )

        relative_file_path = package_path(file)
        log_debug('Building file: %s' % relative_file_path)

        data = load_yaml(file)

        if data is None:
            log_debug('Empty file: %s' % relative_file_path)
            continue

        json_string = to_json_string(data)
        final_string = command_header() + json_string

        write_file(destination, final_string)
        log_debug('File generated: %s' % package_path(destination))

    log_info('Done building commands.')
