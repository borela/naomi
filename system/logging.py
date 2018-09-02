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

from logging import (
    Formatter,
    getLogger,
    StreamHandler,
)

from .settings import (
    call_on_change,
    get_setting,
)

import logging


plugin_not_loaded = True
loggers = []
formatter = Formatter(fmt="[{name}][{levelname}]: {message}", style='{')
handler = StreamHandler()
handler.setFormatter(formatter)


def get_level():
    if not plugin_not_loaded:
        raise SystemError('Plugin not loaded.')
    return get_setting('log_level', 'INFO').upper()


def get_logger(name=None):
    if name is not None:
        name = 'Naomi.' + name
    else:
        name = 'Naomi'

    logger = getLogger(name)
    if logger in loggers:
        return logger

    loggers.append(logger)
    logger.addHandler(handler)
    logger.setLevel(get_level())

    return logger


def plugin_loaded():
    plugin_not_loaded = False
    call_on_change(settings_changed)


def plugin_unloaded():
    for logger in loggers:
        logger.removeHandler(handler)


def settings_changed():
    for logger in loggers:
        logger.setLevel(get_level())
