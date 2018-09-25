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
    realpath,
    relpath,
    splitext,
)


SYSTEM_DIR = dirname(__file__)
HEADERS_DIR = join(SYSTEM_DIR, 'headers')
PACKAGE_DIR = join(SYSTEM_DIR, '..')

INTEGRATION_DIR = realpath(join(PACKAGE_DIR, 'integration'))

COMMANDS_DIR = join(INTEGRATION_DIR, 'commands'))
COMMANDS_SRC_DIR = join(COMMANDS_DIR, 'src')
COMMANDS_BUILD_DIR = join(COMMANDS_DIR, 'build')

KEYMAPS_DIR = join(INTEGRATION_DIR, 'keymaps'))
KEYMAPS_SRC_DIR = join(KEYMAPS_DIR, 'src')
KEYMAPS_BUILD_DIR = join(KEYMAPS_DIR, 'build')

MENUS_DIR = join(INTEGRATION_DIR, 'menus'))
MENUS_SRC_DIR = join(MENUS_DIR, 'src')
MENUS_BUILD_DIR = join(MENUS_DIR, 'build')

PREFERENCES_DIR = join(INTEGRATION_DIR, 'preferences'))
PREFERENCES_SRC_DIR = join(PREFERENCES_DIR, 'src')
PREFERENCES_BUILD_DIR = join(PREFERENCES_DIR, 'build')


def change_base(path, old_base, new_base):
    relative = relpath(path, old_base)
    return join(new_base, relative)


def change_extension(file_path, new_extension):
    base = splitext(file_path)[0]
    return base + '.' + new_extension


def modify_path(path, old_base, new_base, new_extension=None):
    result = change_base(path, old_base, new_base)
    if new_extension is not None:
        result = change_extension(result, new_extension)
    return result


def package_path(path):
    """
    Calculates the relative path to the package’s root.
    """
    return relpath(path, PACKAGE_DIR)
