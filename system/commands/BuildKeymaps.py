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

from Naomi.system.paths import (
    KEYMAPS_BUILD_DIR,
    KEYMAPS_SRC_DIR,
    package_path,
)

from Naomi.system.headers import keymap as keymap_header
from Naomi.system.logging import get_logger
from Naomi.system.util import to_json_string
from os.path import join
from sublime_plugin import ApplicationCommand


def build():
    logger = get_logger()
    logger.info('Cleaning: %s' % package_path(KEYMAPS_BUILD_DIR))

    delete_dir_contents(KEYMAPS_BUILD_DIR)

    shared, by_os = get_keymaps()

    logger.info('Building shared keymaps...')

    if len(shared) > 0:
        write_file(
            join(KEYMAPS_BUILD_DIR, 'Default.sublime-keymap'),
            keymap_header() + to_json_string(shared),
        )

    for os in by_os:
        logger.info('Building keymaps for %s...' % os)

        keymaps = by_os[os]
        if len(keymaps) > 0:
            write_file(
                join(KEYMAPS_BUILD_DIR, 'Default (%s).sublime-keymap' % os),
                keymap_header() + to_json_string(keymaps),
            )

    logger.info('Done building keymaps.')


def get_keymaps():
    logger = get_logger()
    logger.info('Processing keymaps...')

    shared = []
    by_os = {}
    for file in list_files(KEYMAPS_SRC_DIR):
        data = load_yaml(file)

        # Empty file.
        if data is None:
            logger.debug('Empty file: %s' % package_path(file))
            continue

        logger.debug(package_path(file))

        bindings = data['bindings']

        # OS is not required and we will assume that the file is valid for all
        # of them.
        if 'oss' not in data:
            shared += bindings
            continue

        oss = data['oss']
        if isinstance(oss, str):
            oss = [oss]

        for os in oss:
            validate_os(os, file)
            if os not in by_os:
                by_os[os] = []
            by_os[os] += bindings

    return shared, by_os


def validate_os(os, file):
    valid_os = [
        'Linux',
        'Windows',
        'OSX',
    ]

    if os not in valid_os:
        raise ValueError('Invalid OS “%s” for file: %s' % (os, file))


class NaomiBuildKeymapsCommand(ApplicationCommand):
    def run(self):
        build()
