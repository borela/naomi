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

from Naomi.system.fs import (
    delete_dir_contents,
    list_files,
    load_yaml,
    write_file,
)

from Naomi.system.headers import keymap as keymap_header
from Naomi.system.logging import get_logger
from Naomi.system.paths import package_path
from Naomi.system.util import to_json_string
from os.path import join


def compile_keymaps(dir_path, dest_dir_path):
    logger = get_logger()

    logger.debug('Cleaning: %s' % package_path(dest_dir_path))

    delete_dir_contents(dest_dir_path)

    logger.info('Compiling keymaps...')

    files = [file for file in list_files(dir_path)]
    (shared, per_os) = load_keymaps(files)

    write_shared_keymap(shared, dest_dir_path)
    write_per_os_keymap(per_os, dest_dir_path)

    logger.info('Done compiling keymaps...')


def load_keymaps(files_paths):
    combined_shared = []
    combined_per_os = {}
    loaded_files = [load_keymap(file_path) for file_path in files_paths]

    for (shared, per_os) in loaded_files:
        combined_shared += shared
        for os in per_os:
            if os not in combined_per_os:
                combined_per_os[os] = []
            combined_per_os[os] += per_os[os]

    return combined_shared, combined_per_os


def load_keymap(file_path):
    logger = get_logger()
    relative_file_path = package_path(file_path)
    shared = []
    per_os = {}

    data = load_yaml(file_path)
    if data is None:
        logger.debug('Empty file: %s' % relative_file_path)
        return shared, per_os

    logger.debug('Loading: %s' % relative_file_path)

    # The actual key bindings.
    bindings = data['bindings']

    # If “oss” is not specified, that means that the keymap works on all
    # platforms.
    if 'oss' not in data:
        shared = bindings
        logger.debug('Done processing: %s' % relative_file_path)
        return shared, per_os

    # “oss” can be a string representing a single platform.
    oss = data['oss']
    if isinstance(oss, str):
        oss = [oss]

    # Triage the bindings by OS.
    for os in oss:
        validate_os(os, file_path)
        if os not in per_os:
            per_os[os] = []
        per_os[os] += bindings

    logger.debug('Done processing: %s' % relative_file_path)
    return shared, per_os


def validate_os(os, file_path):
    valid_os = ['Linux', 'Windows', 'OSX']
    if os not in valid_os:
        raise ValueError('Invalid OS “%s” for file: %s' % (os, file_path))


def write_per_os_keymap(per_os_bindings, dest_dir_path):
    logger = get_logger()

    for os in per_os_bindings:
        bindings = per_os_bindings[os]
        if len(bindings) < 1:
            continue

        file_name = 'Default (%s).sublime-keymap' % os
        destination = join(dest_dir_path, file_name)
        final_string = keymap_header() + to_json_string(bindings)

        logger.debug('Writting keymap: %s' % destination)
        write_file(destination, final_string)


def write_shared_keymap(bindings, dest_dir_path):
    if len(bindings) < 1:
        return

    logger = get_logger()
    destination = join(dest_dir_path, 'Default.sublime-keymap')
    final_string = keymap_header() + to_json_string(bindings)

    logger.debug('Writting keymap: %s' % destination)
    write_file(destination, final_string)
