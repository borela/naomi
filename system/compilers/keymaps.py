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

from borela import (
    delete_dir_contents,
    list_files,
    load_yaml,
    to_json_string,
    write_text_file,
)

from Naomi.system import (
    EVENT_BUS,
    log_debug,
    log_info,
    package_relpath,
)

from Naomi.system.events import (
    building_keymaps,
    finished_building_keymaps,
)

from Naomi.system.headers import keymap as keymap_header
from os.path import join


def compile_keymaps(src_dir, build_dir):
    """
    Load all keymaps sources and generate files for each OS on demand:

      Default.sublime-keymap
      Default (Linux).sublime-keymap
      Default (Windows).sublime-keymap
      Default (OSX).sublime-keymap
    """

    EVENT_BUS.emit(building_keymaps())
    log_debug('Cleaning: %s' % package_relpath(build_dir))

    delete_dir_contents(build_dir)

    log_info('Compiling keymaps...')

    files = [file for file, _, _ in list_files(src_dir)]
    (shared, per_os) = load_keymaps(files)

    write_shared_keymap(shared, src_dir, build_dir)
    write_per_os_keymap(per_os, src_dir, build_dir)

    log_info('Done compiling keymaps...')
    EVENT_BUS.emit(finished_building_keymaps())


def load_keymaps(files_paths):
    """
    Load keymaps, combine all shared and exclusive bindings into a single
    result that is used later to generate the final “Default” files.
    """

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
    """
    Load a single keymap source, returns bindings shared by all OSs and the
    exclusive ones indexed by OS.
    """

    relative_file_path = package_relpath(file_path)
    shared = []
    per_os = {}

    data = load_yaml(file_path)
    if data is None:
        log_debug('Empty file: %s' % relative_file_path)
        return shared, per_os

    log_debug('Loading: %s' % relative_file_path)

    # The actual key bindings.
    bindings = data['bindings']

    # If “os” is not specified, that means that the keymap works on all
    # platforms.
    if 'os' not in data:
        shared = bindings
        log_debug('Generic shortcut: %s' % relative_file_path)
        return shared, per_os

    # “os” can be a string representing a single platform.
    oss = data['os']
    if isinstance(oss, str):
        oss = [oss]

    # Triage the bindings by OS.
    for os in oss:
        validate_os(os, file_path)
        if os not in per_os:
            per_os[os] = []
        per_os[os] += bindings

    log_debug('Contains shortcuts for %s: %s' % (oss, relative_file_path))
    return shared, per_os


def validate_os(os, file_path):
    valid_os = ['Linux', 'Windows', 'OSX']
    if os not in valid_os:
        raise ValueError('Invalid OS “%s” for file: %s' % (os, file_path))


def write_per_os_keymap(per_os_bindings, src_dir, build_dir):
    """
    Write bindings indexed by OS on their respective files:

      Default (Linux).sublime-keymap
      Default (Windows).sublime-keymap
      Default (OSX).sublime-keymap
    """

    for os in per_os_bindings:
        bindings = per_os_bindings[os]
        if len(bindings) < 1:
            continue

        file_name = 'Default (%s).sublime-keymap' % os
        destination = join(build_dir, file_name)
        final_string = (
            keymap_header(src_dir)
            + to_json_string(bindings, indent=True)
        )

        write_text_file(destination, final_string)
        log_debug('File generated: %s' % package_relpath(destination))


def write_shared_keymap(bindings, src_dir, build_dir):
    """
    Write bindings shared by all OSs on:

      Default.sublime-keymap
    """

    if len(bindings) < 1:
        return

    destination = join(build_dir, 'Default.sublime-keymap')
    final_string = (
        keymap_header(src_dir)
        + to_json_string(bindings, indent=True)
    )

    write_text_file(destination, final_string)
    log_debug('File generated: %s' % package_relpath(destination))
