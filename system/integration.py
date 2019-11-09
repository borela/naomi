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

from Naomi.system import EVENT_BUS
from Naomi.system.events import (
    integrated_commands,
    integrated_keymaps,
    integrated_menus,
    integrated_preferences,
    integrated_syntaxes,
)


def integrate_commands(src_dir, build_dir):
    EVENT_BUS.emit(integrated_commands(src_dir, build_dir))


def integrate_keymaps(src_dir, build_dir):
    EVENT_BUS.emit(integrated_keymaps(src_dir, build_dir))


def integrate_menus(src_dir, build_dir):
    EVENT_BUS.emit(integrated_menus(src_dir, build_dir))


def integrate_preferences(src_dir, build_dir):
    EVENT_BUS.emit(integrated_preferences(src_dir, build_dir))


def integrate_syntaxes(src_dir, build_dir):
    EVENT_BUS.emit(integrated_syntaxes(src_dir, build_dir))
