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

STOPPED_WATCHING_COMMANDS = 'STOPPED_WATCHING_COMMANDS'
STOPPED_WATCHING_KEYMAPS = 'STOPPED_WATCHING_KEYMAPS'
STOPPED_WATCHING_MENUS = 'STOPPED_WATCHING_MENUS'
STOPPED_WATCHING_PREFERENCES = 'STOPPED_WATCHING_PREFERENCES'
STOPPED_WATCHING_SYNTAXES = 'STOPPED_WATCHING_SYNTAXES'

def stopped_watching_commands():
    return {'type': STOPPED_WATCHING_COMMANDS}

def stopped_watching_keymaps():
    return {'type': STOPPED_WATCHING_KEYMAPS}

def stopped_watching_menus():
    return {'type': STOPPED_WATCHING_MENUS}

def stopped_watching_preferences():
    return {'type': STOPPED_WATCHING_PREFERENCES}

def stopped_watching_syntaxes():
    return {'type': STOPPED_WATCHING_SYNTAXES}
