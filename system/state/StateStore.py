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
        self._reducers = reducers

        # Initialize state.
        for name, reducer in self._reducers.items():
            self._state[name] = reducer()

    def __contains__(self, key):
        return key in self._state

    def __getitem__(self, key):
        return self._state[key]

    def __iter__(self):
        return iter(self._state)

    def __len__(self):
        return len(self._state)

    def __str__(self):
        return to_json_string(self._state)

    def apply(self, event):
        event_type = event.get('type', None)

        if not isinstance(event_type, str):
            raise ValueError('Invalid event type.')

        for name, reducer in self._reducers.items():
            self._state[name] = reducer(old_state, event)

    _reducers = {}
    _state = {}
