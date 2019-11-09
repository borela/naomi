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

from .event_bus import EVENT_BUS
from borela import StateStore

# Reducers.
from .state_reducers.building import reducer as building_reducer
from .state_reducers.integrated import reducer as integrated_reducer
from .state_reducers.settings import reducer as settings_reducer
from .state_reducers.watching import reducer as watching_reducer

# Store that holds the plugins’ state.
STATE_STORE = StateStore(
    building=building_reducer,
    integrated=integrated_reducer,
    settings=settings_reducer,
    watching=watching_reducer,
)

# Listen to all events to modify the store through the reducers.
EVENT_BUS.on_any(lambda event: STATE_STORE.apply(event))
