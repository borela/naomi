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

from borela.logging import (
    log as borela_log,
    set_log_level,
)

def log(level, message):
    borela_log('NAOMI', level, message)


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
