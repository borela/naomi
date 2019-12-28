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

from Naomi.system import (
    EVENT_BUS,
    STATE_STORE,
)

from Naomi.system.events import (
    building_commands,
    building_keymaps,
    building_menus,
    building_preferences,
    building_syntaxes,

    finished_building_commands,
    finished_building_keymaps,
    finished_building_menus,
    finished_building_preferences,
    finished_building_syntaxes,
)

from .syntaxes import compile_syntax # noqa
from .commands import compile_commands # noqa
from .keymaps import compile_keymaps # noqa
from .menus import compile_menus # noqa
from .preferences import compile_preferences # noqa

def compile_integrated_commands():
    EVENT_BUS.emit(building_commands())

    for integrated in STATE_STORE['integrated']['commands']:
        compile_commands(
            integrated['src_dir'],
            integrated['build_dir'],
        )

    EVENT_BUS.emit(finished_building_commands())

def compile_integrated_keymaps():
    EVENT_BUS.emit(building_keymaps())

    for integrated in STATE_STORE['integrated']['keymaps']:
        compile_keymaps(
            integrated['src_dir'],
            integrated['build_dir'],
        )

    EVENT_BUS.emit(finished_building_keymaps())

def compile_integrated_menus():
    EVENT_BUS.emit(building_menus())

    for integrated in STATE_STORE['integrated']['menus']:
        compile_menus(
            integrated['src_dir'],
            integrated['build_dir'],
        )

    EVENT_BUS.emit(finished_building_menus())

def compile_integrated_preferences():
    EVENT_BUS.emit(building_preferences())

    for integrated in STATE_STORE['integrated']['preferences']:
        compile_preferences(
            integrated['src_dir'],
            integrated['build_dir'],
        )

    EVENT_BUS.emit(finished_building_preferences())

def compile_configured_syntaxes():
    EVENT_BUS.emit(building_syntaxes())

    for settings in STATE_STORE['settings']['syntaxes']:
        compile_syntax(settings)

    EVENT_BUS.emit(finished_building_syntaxes())
