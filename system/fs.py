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

from ruamel.yaml import load
from os import makedirs, walk
from os.path import dirname, exists, join
from shutil import rmtree
from json import dumps


def deleteDir(dir_path):
    if not exists(dir_path):
        return
    rmtree(dir_path)


def ensureDirExists(dir_path):
    if not exists(dir_path):
        makedirs(dir_path)


def listFiles(dir_path):
    for path, directories, files in walk(dir_path):
        for file in files:
            yield join(path, file)


def loadYaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return load(file)


def readFile(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def toJsonString(value):
    return dumps(value, indent=2, sort_keys=True)


def writeFile(file_path, data):
    ensureDirExists(dirname(file_path))
    with open(file_path, 'w', encoding='utf-8', newline='\n') as file:
        return file.write(data)
