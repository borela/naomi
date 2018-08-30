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
    MENUS_BUILD_DIR,
    MENUS_SRC_DIR,
    package_path,
)

from Naomi.system.headers import menu as menu_header
from Naomi.system.logging import get_logger
from Naomi.system.util import to_json_string
from os.path import join
from sublime_plugin import ApplicationCommand


logger = get_logger()


def build():
    logger.info('Cleaning: %s' % package_path(MENUS_BUILD_DIR))

    delete_dir_contents(MENUS_BUILD_DIR)

    menus = get_menus()
    for group in menus:
        logger.info('Building menus for %s...' % group)

        write_file(
            join(MENUS_BUILD_DIR, '%s.sublime-menu' % group),
            menu_header() + to_json_string(menus[group]),
        )

    logger.info('Done building menus.')


def get_menus():
    result = {}

    logger.info('Processing menus...')

    for file in list_files(MENUS_SRC_DIR):
        data = load_yaml(file)

        # Empty file.
        if data is None:
            logger.debug('Empty file: %s' % package_path(file))
            continue

        logger.debug(package_path(file))

        if 'locations' not in data:
            raise ValueError('Missing “locations” for menu: %s' % file)

        locations = data['locations']
        if isinstance(locations, str):
            locations = [locations]

        for location in locations:
            validate_location(location, file)
            if location not in result:
                result[location] = []
            result[location] = data['menus']

    return result


def validate_location(location, file):
    valid_locations = [
        'Context',
        'Encoding',
        'Find in Files',
        'Indentation',
        'Line Endings',
        'Main',
        'Side Bar Mount Point',
        'Side Bar',
        'Syntax',
        'Tab Context',
        'Widget Context',
    ]

    if location not in valid_locations:
        message = 'Invalid location “%s” for file: %s' % (location, file)
        raise ValueError(message)


class NaomiBuildMenusCommand(ApplicationCommand):
    def run(self):
        build()
