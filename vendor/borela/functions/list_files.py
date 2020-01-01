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

from os import walk
from os.path import join

def list_files(dir_path, recursive=True):
    if not recursive:
        path, _, files = next(walk(dir_path))
        for file in files:
            yield join(path, file), path, file
        return

    for path, _, files in walk(dir_path):
        for file in files:
            yield join(path, file), path, file
