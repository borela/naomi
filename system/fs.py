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
    makedirs,
    remove,
    walk,
)

from os.path import (
    dirname,
    exists,
    join,
)

from .util import dict_to_plist_xml
from ruamel.yaml import safe_load
from shutil import rmtree


def delete_dir(dir_path):
    if exists(dir_path):
        rmtree(dir_path)


def delete_dir_contents(dir_path):
    if not exists(dir_path):
        return
    for node in listdir(dir_path):
        full_path = join(dir_path, node)
        try:
            rmtree(full_path)
        except OSError:
            remove(full_path)


def ensure_dir_exists(dir_path):
    if not exists(dir_path):
        makedirs(dir_path)


def list_files(dir_path):
    for path, directories, files in walk(dir_path):
        for file in files:
            yield join(path, file)


def load_yaml(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        return safe_load(file)


def read_file(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        return file.read()


def write_file(file_path, data):
    ensure_dir_exists(dirname(file_path))
    with open(file_path, 'w', encoding = 'utf-8', newline = '\n') as file:
        return file.write(data)
