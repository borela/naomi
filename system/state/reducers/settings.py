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

from Naomi.system.events import SETTINGS_UPDATED

VALID_LOG_LEVELS = [
    "CRITICAL",
    "ERROR",
    "WARNING",
    "INFO",
    "DEBUG",
]


def get_log_level(settings):
    result = settings.get('log_level', 'INFO').upper()
    if result not in VALID_LOG_LEVELS:
        return 'INFO'
    return result


def reducer(state={}, event=None):
    if event is None or event['type'] != SETTINGS_UPDATED:
        return state

    SETTINGS = event['payload']

    new_settings = {}
    new_settings['log_level'] = get_log_level(SETTINGS)

    return new_settings
