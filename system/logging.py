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
from logging import (
    Formatter,
    getLogger,
    StreamHandler,
)


loggers = []
formatter = Formatter(fmt="[{name}]: {message}", style='{')
handler = StreamHandler()
handler.setFormatter(formatter)


def get_logger(name=None):
    if name is not None:
        name = 'Naomi.' + name
    else:
        name = 'Naomi'

    logger = getLogger(name)

    if logger in loggers:
        return logger
    else:
        loggers.append(logger)

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def plugin_unloaded():
    for logger in loggers:
        logger.removeHandler(handler)
