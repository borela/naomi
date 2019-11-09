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

import logging
from datetime import datetime, timedelta

global_level = 'DEBUG'
time_start = datetime.now()
time_end = time_start
time_diff = timedelta()


def get_log_level():
    global global_level
    return global_level


def set_log_level(new_level):
    global global_level
    global_level = new_level


def print_log_message(group, level, message):
    global global_level, time_start, time_end, time_diff

    # Get the log level as a number to make the comparison easier.
    message_level = getattr(logging, level)
    current_level = getattr(logging, global_level)

    # If multiple messages are sent at the same second, we need to see the
    # millisecond difference between them to enable easier profiling.
    time_end = datetime.now()
    time_diff = time_end - time_start

    if time_diff > timedelta(seconds=1):
        time_diff = timedelta()

    if message_level >= current_level:
        print('%s [%s:%s] +%ims: %s' % (
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            group,
            level,
            time_diff.microseconds / 1000,
            message,
        ))

    time_start = time_end


def log(group, level, message):
    print_log_message(group, level, message)


def log_critical(message):
    log('CRITICAL', message)


def log_debug(message):
    log('DEBUG', message)


def log_error(message):
    log('ERROR', message)


def log_info(message):
    log('INFO', message)


def log_warning(message):
    log('WARNING', message)
