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

from ..fs import read_file
from Naomi.system.state import STORE
from os.path import join


def command():
    return read_header('command.txt')


def keymap():
    return read_header('keymap.txt')


def menu():
    return read_header('menu.txt')


def plist():
    return read_header('plist.txt')


def preferences():
    return read_header('preferences.txt')


def read_header(file_name):
    HEADERS_DIR = STORE['directories']['system']['headers']
    return read_file(join(HEADERS_DIR, file_name))


def syntax():
    return read_header('syntax.txt')