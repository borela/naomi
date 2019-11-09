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
    SETTINGS_LOADED,
    SETTINGS_UPDATED,
)

from Naomi.system import set_log_level

SETTINGS_EVENTS = [
    SETTINGS_LOADED,
    SETTINGS_UPDATED,
]

VALID_LOG_LEVELS = [
    'CRITICAL',
    'ERROR',
    'WARNING',
    'INFO',
    'DEBUG',
]


def log_level_from_settings(settings):
    result = settings.get('log_level', 'INFO').upper()
    if result not in VALID_LOG_LEVELS:
        return 'INFO'
    return result


def reducer(state={}, event=None):
    if event is None or event['type'] not in SETTINGS_EVENTS:
        return state

    SETTINGS = event['payload']

    log_level = log_level_from_settings(SETTINGS)
    set_log_level(log_level)

    new_settings = {}
    new_settings['log_level'] = log_level
    new_settings['syntaxes'] = SETTINGS.get('syntaxes', [])


    return new_settings
