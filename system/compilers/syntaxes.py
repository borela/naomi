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

from Naomi.system.event_bus import EVENT_BUS
from Naomi.system.events import (
    building_syntaxes,
    finished_building_syntaxes,
)


def compile_syntaxes(target_dir_path, output_dir_path):
    EVENT_BUS.emit(building_syntaxes())
    EVENT_BUS.emit(finished_building_syntaxes())
