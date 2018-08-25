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
    KEYMAPS_BUILD_DIR,
    KEYMAPS_SRC_DIR,
)

from Naomi.system.headers import KEYMAP as KEYMAP_HEADER
from Naomi.system.util import to_json_string
from os.path import join
from sublime_plugin import ApplicationCommand


def get_keymaps():
    shared = []
    windows = []
    linux = []
    osx = []
    for file in list_files(KEYMAPS_SRC_DIR):
        data = load_yaml(file)

        # Empty file.
        if data is None:
            continue

        if 'os' not in data:
            shared += data['bindings']
            continue

        # We convert the simple string value to an array to use the generic
        # algorithm below.
        if isinstance(data['os'], str):
            data['os'] = [data['os']]

        not_windows = False
        not_linux = False
        not_osx = False

        if 'windows' in data['os']:
            windows += data['bindings']
        else:
            not_windows = True

        if 'linux' in data['os']:
            linux += data['bindings']
        else:
            not_linux = True

        if 'osx' in data['os']:
            osx += data['bindings']
        else:
            not_osx = True

        if not_windows and not_linux and not_osx:
            raise ValueError(
                'Invalid value “%s” for OS on file: %s' %
                data['os'], file
            )
    return shared, windows, linux, osx


class NaomiBuildKeymapsCommand(ApplicationCommand):
    def run(self):
        shared, windows, linux, osx = get_keymaps()

        delete_dir_contents(KEYMAPS_BUILD_DIR)

        if len(shared) > 0:
            write_file(
                join(KEYMAPS_BUILD_DIR, 'Default.sublime-keymap'),
                KEYMAP_HEADER + to_json_string(shared)
            )

        if len(windows) > 0:
            write_file(
                join(KEYMAPS_BUILD_DIR, 'Default (Windows).sublime-keymap'),
                KEYMAP_HEADER + to_json_string(windows)
            )

        if len(linux) > 0:
            write_file(
                join(KEYMAPS_BUILD_DIR, 'Default (Linux).sublime-keymap'),
                KEYMAP_HEADER + to_json_string(linux)
            )

        if len(osx) > 0:
            write_file(
                join(KEYMAPS_BUILD_DIR, 'Default (OSX).sublime-keymap'),
                KEYMAP_HEADER + to_json_string(osx)
            )
