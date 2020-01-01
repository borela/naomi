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

BUILDING_COMMANDS = 'BUILDING_COMMANDS'
BUILDING_KEYMAPS = 'BUILDING_KEYMAPS'
BUILDING_MENUS = 'BUILDING_MENUS'
BUILDING_PREFERENCES = 'BUILDING_PREFERENCES'
BUILDING_SYNTAXES = 'BUILDING_SYNTAXES'

def building_commands():
    return {'type': BUILDING_COMMANDS}

def building_keymaps():
    return {'type': BUILDING_KEYMAPS}

def building_menus():
    return {'type': BUILDING_MENUS}

def building_preferences():
    return {'type': BUILDING_PREFERENCES}

def building_syntaxes():
    return {'type': BUILDING_SYNTAXES}
