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

NOT_WATCHING_COMMANDS = 'NOT_WATCHING_COMMANDS'
NOT_WATCHING_KEYMAPS = 'NOT_WATCHING_KEYMAPS'
NOT_WATCHING_MENUS = 'NOT_WATCHING_MENUS'
NOT_WATCHING_PREFERENCES = 'NOT_WATCHING_PREFERENCES'
NOT_WATCHING_SYNTAXES = 'NOT_WATCHING_SYNTAXES'


def not_watching_commands():
    return {'type': NOT_WATCHING_COMMANDS}


def not_watching_keymaps():
    return {'type': NOT_WATCHING_KEYMAPS}


def not_watching_menus():
    return {'type': NOT_WATCHING_MENUS}


def not_watching_preferences():
    return {'type': NOT_WATCHING_PREFERENCES}


def not_watching_syntaxes():
    return {'type': NOT_WATCHING_SYNTAXES}
