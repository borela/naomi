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

from os.path import (
    dirname,
    join,
)

from borela import read_text_file
from Naomi.system import package_relpath


def command(src_dir):
    return read_header('command.txt', src_dir)


def keymap(src_dir):
    return read_header('keymap.txt', src_dir)


def menu(src_dir):
    return read_header('menu.txt', src_dir)


def plist():
    return read_header('plist.txt')


def preferences(src_dir):
    return read_header('preferences.txt', src_dir)


def read_header(file_name, src_dir=None):
    template = read_text_file(join(dirname(__file__), file_name))

    if src_dir:
        return template.replace(
            '$1',
            # Just to make sure the paths in headers always use forward slashes
            # to prevent build files from showing up on git when compiling on
            # another platform.
            package_relpath(src_dir).replace("\\","/")
        )

    return template


def syntax(src_dir):
    return read_header('syntax.txt', src_dir)
