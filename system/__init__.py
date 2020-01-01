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

from os.path import (
    dirname,
    join,
    realpath,
)

from .integration import (
    integrate_commands,
    integrate_keymaps,
    integrate_menus,
    integrate_preferences,
    integrate_syntaxes,
)

from .event_bus import * # noqa
from .logging import * # noqa
from .path import * # noqa
from .state_store import * # noqa

INTEGRATION_DIR = realpath(join(dirname(__file__), '..', 'integration'))

integrate_commands(
    join(INTEGRATION_DIR, 'commands', 'src'),
    join(INTEGRATION_DIR, 'commands', 'build'),
)

integrate_keymaps(
    join(INTEGRATION_DIR, 'keymaps', 'src'),
    join(INTEGRATION_DIR, 'keymaps', 'build'),
)

integrate_menus(
    join(INTEGRATION_DIR, 'menus', 'src'),
    join(INTEGRATION_DIR, 'menus', 'build'),
)

integrate_preferences(
    join(INTEGRATION_DIR, 'preferences', 'src'),
    join(INTEGRATION_DIR, 'preferences', 'build'),
)

integrate_syntaxes(
    join(INTEGRATION_DIR, 'syntaxes', 'src'),
    join(INTEGRATION_DIR, 'syntaxes', 'build'),
)
