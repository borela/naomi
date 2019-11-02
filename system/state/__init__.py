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

from borela import StateStore
from Naomi.system.event_bus import EVENT_BUS

# Reducers.
from .directories import reducer as directories_reducer
from .settings import reducer as settings_reducer


STORE = StateStore(
    directories=directories_reducer,
    settings=settings_reducer,
)

EVENT_BUS.onAny(lambda event: STORE.apply(event))
