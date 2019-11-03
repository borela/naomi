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

WATCHING_COMMANDS = 'WATCHING_COMMANDS'
WATCHING_KEYMAPS = 'WATCHING_KEYMAPS'
WATCHING_MENUS = 'WATCHING_MENUS'
WATCHING_PREFERENCES = 'WATCHING_PREFERENCES'
WATCHING_SYNTAXES = 'WATCHING_SYNTAXES'


def watching_commands():
    return {'type': WATCHING_COMMANDS}


def watching_keymaps():
    return {'type': WATCHING_KEYMAPS}


def watching_menus():
    return {'type': WATCHING_MENUS}


def watching_preferences():
    return {'type': WATCHING_PREFERENCES}


def watching_syntaxes():
    return {'type': WATCHING_SYNTAXES}
