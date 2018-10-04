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
    load_yaml,
    list_files,
    write_file,
)

from Naomi.system.headers import menu as menu_header
from Naomi.system.logging import log
from Naomi.system.paths import package_path
from Naomi.system.utils import to_json_string
from os.path import join


def compile_menus(dir_path, dest_dir_path):
    log.debug('Cleaning: %s' % package_path(dest_dir_path))

    delete_dir_contents(dest_dir_path)

    files = [file for file in list_files(dir_path)]
    menus = load_menus(files)

    for group in menus:
        log.info('Building menus for %s...' % group)

        destination = join(dest_dir_path, '%s.sublime-menu' % group)
        final_string = menu_header() + to_json_string(menus[group])
        write_file(destination, final_string)

    log.info('Done building menus.')


def load_menus(files_paths):
    """
    Load all menu sources and returns the result indexed by the destination.
    """

    result = {}
    loaded_files = [
        load_menus_from_file(file_path)
        for file_path in files_paths
    ]

    for loaded_menus in loaded_files:
        # Files can be empty.
        if load_menus is None:
            continue

        for location in loaded_menus:
            if location not in result:
                result[location] = {}
            result[location] = loaded_menus[location]

    return result


def load_menus_from_file(file_path):
    """
    Load menus from a single source and returns the result indexed by
    destination.
    """

    relative_file_path = package_path(file_path)
    data = load_yaml(file_path)
    result = {}

    # Empty file.
    if data is None:
        log.debug('Empty file: %s' % relative_file_path)
        return None

    log.debug('Loading: %s' % relative_file_path)

    if 'location' not in data:
        message = 'Missing “location” for menu: %s' % relative_file_path
        raise ValueError(message)

    locations = data['location']

    # Single location.
    if isinstance(locations, str):
        locations = [locations]

    for location in locations:
        validate_location(location, file_path)
        if location not in result:
            result[location] = []
        result[location] = data['menus']

    log.debug('Done processing: %s' % relative_file_path)
    return result


def validate_location(location, file_path):
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
        message = 'Invalid location “%s” for file: %s' % (location, file_path)
        raise ValueError(message)
