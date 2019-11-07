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

FINISHED_BUILDING_COMMANDS = 'FINISHED_BUILDING_COMMANDS'
FINISHED_BUILDING_KEYMAPS = 'FINISHED_BUILDING_KEYMAPS'
FINISHED_BUILDING_MENUS = 'FINISHED_BUILDING_MENUS'
FINISHED_BUILDING_PREFERENCES = 'FINISHED_BUILDING_PREFERENCES'
FINISHED_BUILDING_SYNTAXES = 'FINISHED_BUILDING_SYNTAXES'


def finished_building_commands():
    return {'type': FINISHED_BUILDING_COMMANDS}


def finished_building_keymaps():
    return {'type': FINISHED_BUILDING_KEYMAPS}


def finished_building_menus():
    return {'type': FINISHED_BUILDING_MENUS}


def finished_building_preferences():
    return {'type': FINISHED_BUILDING_PREFERENCES}


def finished_building_syntaxes():
    return {'type': FINISHED_BUILDING_SYNTAXES}
