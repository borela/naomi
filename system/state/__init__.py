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

from Naomi.system.settings import get_settings
from Naomi.system.events import settings_updated

from .Store import Store
from .reducers.directories import reducer as directories_reducer
from .reducers.settings import reducer as settings_reducer


STORE = Store(
    directories=directories_reducer,
    settings=settings_reducer,
)


def plugin_loaded():
    def update_settings_state():
        SETTINGS = get_settings()
        STORE.apply(settings_updated(SETTINGS))

    SETTINGS = get_settings()
    SETTINGS.clear_on_change('naomi-settings-state')
    SETTINGS.add_on_change('naomi-settings-state', update_settings_state)

    update_settings_state()
