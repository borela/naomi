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
    to_json_string,
    write_text_file,
)

from Naomi.system import (
    EVENT_BUS,
    log_debug,
    log_info,
    package_relpath,
)

from Naomi.system.headers import command as command_header

# Convert commands from “x.yml” to “x.sublime-commands”.
def compile_commands(src_dir, build_dir):
    log_debug('Cleaning: %s' % package_relpath(build_dir))

    delete_dir_contents(build_dir)

    log_info('Building command files: %s' % src_dir)

    for file, _, _ in list_files(src_dir):
        destination = modify_path(
            file,
            old_base=src_dir,
            new_base=build_dir,
            new_extension='sublime-commands',
        )

        relative_file_path = package_relpath(file)
        log_debug('Building file: %s' % relative_file_path)

        data = load_yaml(file)

        if data is None:
            log_debug('Empty file: %s' % relative_file_path)
            continue

        json_string = to_json_string(data, indent=True)
        final_string = command_header(src_dir) + json_string

        write_text_file(destination, final_string)
        log_debug('File generated: %s' % package_relpath(destination))

    log_info('Done building commands: %s' % src_dir)
