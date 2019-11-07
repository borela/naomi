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

from Naomi.system.events import settings_updated
from Naomi.system.event_bus import EVENT_BUS
from sublime import load_settings


def plugin_loaded():
    SETTINGS = load_settings('Naomi.sublime-settings')
    SETTINGS.add_on_change('naomi-settings-state', update_settings)
    update_settings()


def plugin_unloaded():
    SETTINGS = load_settings('Naomi.sublime-settings')
    SETTINGS.clear_on_change('naomi-settings-state')


def update_settings():
    SETTINGS = load_settings('Naomi.sublime-settings')
    EVENT_BUS.emit(settings_updated(SETTINGS))
