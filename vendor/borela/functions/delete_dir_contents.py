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

from os import (
    listdir,
    remove,
)
from os.path import (
    exists,
    join,
)
from shutil import rmtree


def delete_dir_contents(dir_path):
    if not exists(dir_path):
        return

    for node in listdir(dir_path):
        full_path = join(dir_path, node)
        try:
            rmtree(full_path)
        except OSError:
            remove(full_path)
