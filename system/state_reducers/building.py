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

from Naomi.system.events import (
    FINISHED_BUILDING_COMMANDS,
    FINISHED_BUILDING_KEYMAPS,
    FINISHED_BUILDING_MENUS,
    FINISHED_BUILDING_PREFERENCES,
    FINISHED_BUILDING_SYNTAXES,

    BUILDING_COMMANDS,
    BUILDING_KEYMAPS,
    BUILDING_MENUS,
    BUILDING_PREFERENCES,
    BUILDING_SYNTAXES,
)

INITIAL_STATE = {
    'working': False,
    'commands': False,
    'keymaps': False,
    'menus': False,
    'preferences': False,
    'syntaxes': False,
}

EVENTS = [
    FINISHED_BUILDING_COMMANDS,
    FINISHED_BUILDING_KEYMAPS,
    FINISHED_BUILDING_MENUS,
    FINISHED_BUILDING_PREFERENCES,
    FINISHED_BUILDING_SYNTAXES,

    BUILDING_COMMANDS,
    BUILDING_KEYMAPS,
    BUILDING_MENUS,
    BUILDING_PREFERENCES,
    BUILDING_SYNTAXES,
]


def reducer(state=INITIAL_STATE, event=None):
    if event is None or event['type'] not in EVENTS:
        return state

    # This dictionary will be simple, deep copy won’t be necessary.
    state = dict(state)

    # NOT building.
    if event['type'] == FINISHED_BUILDING_COMMANDS:
        state['commands'] = False

    if event['type'] == FINISHED_BUILDING_KEYMAPS:
        state['keymaps'] = False

    if event['type'] == FINISHED_BUILDING_MENUS:
        state['menus'] = False

    if event['type'] == FINISHED_BUILDING_PREFERENCES:
        state['preferences'] = False

    if event['type'] == FINISHED_BUILDING_SYNTAXES:
        state['syntaxes'] = False

    # Building.
    if event['type'] == BUILDING_COMMANDS:
        state['commands'] = True

    if event['type'] == BUILDING_KEYMAPS:
        state['keymaps'] = True

    if event['type'] == BUILDING_MENUS:
        state['menus'] = True

    if event['type'] == BUILDING_PREFERENCES:
        state['preferences'] = True

    if event['type'] == BUILDING_SYNTAXES:
        state['syntaxes'] = True

    state['working'] = (
        state['commands']
        or state['keymaps']
        or state['menus']
        or state['preferences']
        or state['syntaxes']
    )

    return state
