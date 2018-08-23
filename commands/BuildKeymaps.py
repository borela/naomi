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

from Naomi.plugin.paths import KEYMAPS_BUILD_DIR, KEYMAPS_SRC_DIR
from os import makedirs, walk
from os.path import dirname, exists, join
from sublime_plugin import ApplicationCommand
from ruamel.yaml import load
from json import dump
from shutil import rmtree


def deleteBuildDir():
    if not exists(KEYMAPS_BUILD_DIR):
        return
    rmtree(KEYMAPS_BUILD_DIR)


def loadYaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return load(file)


def writeJson(file_path, data):
    # Make sure directory exits.
    directory = dirname(file_path)
    if not exists(directory):
        makedirs(directory)

    with open(file_path, 'w', encoding='utf-8', newline='\n') as file:
        return dump(data, file, indent=2, sort_keys=True)


class NaomiBuildKeymapsCommand(ApplicationCommand):
    def run(self):
        deleteBuildDir()
        for path, directories, files in walk(KEYMAPS_SRC_DIR):
            for file in files:
                SOURCE = join(path, file)
                DESTINATION = join(
                    path.replace('src', 'build'),
                    file.replace('.yml', '.json')
                )
                data = loadYaml(SOURCE)
                writeJson(DESTINATION, data)
