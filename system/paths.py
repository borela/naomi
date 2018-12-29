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

from os.path import (
    join,
    relpath,
    splitext,
)

from Naomi.system.state import STORE


def change_base(path, old_base, new_base):
    relative = relpath(path, old_base)
    return join(new_base, relative)


def change_extension(file_path, new_extension):
    base = splitext(file_path)[0]
    return base + '.' + new_extension


def modify_path(path, old_base, new_base, new_extension=None):
    result = change_base(path, old_base, new_base)
    if new_extension is not None:
        result = change_extension(result, new_extension)
    return result


def package_path(path):
    """
    Calculates the relative path to the package’s root.
    """
    return relpath(path, STORE['directories']['naomi'])
