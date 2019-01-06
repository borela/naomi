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

from Naomi.system.utils import to_json_string


class Store:
    """
    Represents a store for holding and changing state following the event
    sourcing pattern.
    """

    def __init__(self, **reducers):
        self.__reducers = reducers

        # Initialize state.
        for name, reducer in self.__reducers.items():
            self.__state[name] = reducer()

    def __contains__(self, key):
        return key in self.__state

    def __getitem__(self, key):
        return self.__state[key]

    def __iter__(self):
        return iter(self.__state)

    def __len__(self):
        return len(self.__state)

    def __str__(self):
        return to_json_string(self.__state)

    def apply(self, event):
        if event.get('type', None) is None:
            raise ValueError('Event type is undefined.')

        state_changed = False

        for name, reducer in self.__reducers.items():
            old_state = self.__state.get(name, None)
            new_state = reducer(old_state, event)

            if new_state == old_state:
                continue

            self.__state[name] = new_state
            state_changed = True

        if state_changed:
            for listener in self.__changeListeners:
                listener(self.__state)

    def on_change(self, callback):
        self.__changeListeners.append(callback)

    __changeListeners = []
    __reducers = {}
    __state = {}
