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
from datetime import datetime
from time import time

t1 = time()
t2 = t1

def print_log_message(event):
    global t1, t2

    message = event['payload']['message']
    level = event['payload']['level']

    message_level = getattr(logging, level)
    current_level = getattr(logging, STORE['settings']['log_level'])

    if message_level >= current_level:
        print('%s [Naomi][%s]: %s +%ims' % (
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            level,
            message,
            t2 - t1
        ))

    t1 = t2
    t2 = time()


LOG_EVENT_SUBSCRIPTION = EVENT_BUS.on(
    event=LOG_MESSAGE_ADDED,
    subscriber=print_log_message,
)


def plugin_loaded():
    LOG_EVENT_SUBSCRIPTION.subscribe()
    SETTINGS = load_settings('Naomi.sublime-settings')
    SETTINGS.add_on_change('naomi-settings-state', update_settings)
    update_settings()


def plugin_unloaded():
    SETTINGS = load_settings('Naomi.sublime-settings')
    SETTINGS.clear_on_change('naomi-settings-state')


def update_settings():
    SETTINGS = load_settings('Naomi.sublime-settings')
    EVENT_BUS.emit(settings_updated(SETTINGS))
