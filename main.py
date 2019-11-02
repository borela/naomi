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
    LOG_MESSAGE_ADDED,
    settings_updated,
)
import logging
from sublime import load_settings
from Naomi.system.state import STORE
from Naomi.system.event_bus import EVENT_BUS


def plugin_loaded():
    # Print log messages sent to the event bus.
    EVENT_BUS.on(
        event=LOG_MESSAGE_ADDED,
        subscriber=print_log_message,
    )

    SETTINGS = load_settings('Naomi.sublime-settings')
    SETTINGS.add_on_change('naomi-settings-state', update_settings)

    update_settings()

def plugin_unloaded():
    # EVENT_BUS.on(
    #     type=LOG_MESSAGE_ADDED,
    #     subscriber=print_log_message,
    # )

    SETTINGS = load_settings('Naomi.sublime-settings')
    SETTINGS.clear_on_change('naomi-settings-state')


def print_log_message(event):
    message = event['payload']['message']
    level = event['payload']['level']

    message_level = getattr(logging, level)
    current_level = getattr(logging, STORE['settings']['log_level'])

    if message_level >= current_level:
        print('[Naomi][%s]: %s' % (level, message))


def update_settings():
    SETTINGS = load_settings('Naomi.sublime-settings')
    EVENT_BUS.emit(settings_updated(SETTINGS))
