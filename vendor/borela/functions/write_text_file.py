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

from . import ensure_dir_exists
from os.path import dirname

def write_text_file(
    file_path,
    data,
    encoding='utf-8',
    newline='\n',
    create_dirs=True,
):
    if create_dirs:
        ensure_dir_exists(dirname(file_path))

    with open(file_path, 'w', encoding=encoding, newline=newline) as file:
        return file.write(data)
