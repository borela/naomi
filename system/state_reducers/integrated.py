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
    INTEGRATED_COMMANDS,
    INTEGRATED_KEYMAPS,
    INTEGRATED_MENUS,
    INTEGRATED_PREFERENCES,
    INTEGRATED_SYNTAXES,
)

from copy import deepcopy

INITIAL_STATE = {
    'commands': [],
    'keymaps': [],
    'menus': [],
    'preferences': [],
    'syntaxes': [],
}

EVENTS = [
    INTEGRATED_COMMANDS,
    INTEGRATED_KEYMAPS,
    INTEGRATED_MENUS,
    INTEGRATED_PREFERENCES,
    INTEGRATED_SYNTAXES,
]

def reducer(state=INITIAL_STATE, event=None):
    if event is None or event['type'] not in EVENTS:
        return state

    state = deepcopy(state)

    if event['type'] == INTEGRATED_COMMANDS:
        state['commands'].append(event['payload'])

    if event['type'] == INTEGRATED_KEYMAPS:
        state['keymaps'].append(event['payload'])

    if event['type'] == INTEGRATED_MENUS:
        state['menus'].append(event['payload'])

    if event['type'] == INTEGRATED_PREFERENCES:
        state['preferences'].append(event['payload'])

    if event['type'] == INTEGRATED_SYNTAXES:
        state['syntaxes'].append(event['payload'])

    return state
