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

from os.path import dirname, join, realpath

SYSTEM_DIR = dirname(__file__)

HEADERS_DIR = join(SYSTEM_DIR, 'headers')

KEYMAPS_DIR = realpath(join(SYSTEM_DIR, '..', 'keymaps'))
KEYMAPS_SRC_DIR = join(KEYMAPS_DIR, 'src')
KEYMAPS_BUILD_DIR = join(KEYMAPS_DIR, 'build')
