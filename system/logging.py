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
    Formatter as LogFormat,
    getLogger as create_log,
    StreamHandler as Stream,
)

from .settings import (
    call_on_change,
    get_setting,
)


# Create the log used by Naomi. If the log already exists, it will return the
# previous instance.
log = create_log('Naomi')

# If the log already exists, the output does not need to be configured again.
if len(log.handlers) < 1:
    # Create a log format like: [Naomi][INFO]: Some message.
    logFormat = LogFormat(fmt="[{name}][{levelname}]: {message}", style='{')

    # Output log messages to the console.
    logOutput = Stream()
    logOutput.setFormatter(logFormat)
    log.addHandler(logOutput)


def get_level():
    """Get the log level from the settings and defaults to “INFO”."""
    return get_setting('log_level', 'INFO').upper()


def plugin_loaded():
    log.setLevel(get_level())

    # Update level when settings change.
    def settings_changed():
        log.setLevel(get_level())

    call_on_change(settings_changed)
