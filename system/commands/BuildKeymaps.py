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

        if 'platform' not in data:
            shared += data['bindings']
            continue

        if data.platform == 'windows':
            windows += data['bindings']
            continue

        if data.platform == 'linux':
            linux += data['bindings']
            continue

        if data.platform == 'osx':
            osx += data['bindings']
            continue

        raise ValueError(
            'Invalid platform value “%s” for file: %s' %
            data['platform'], file
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
