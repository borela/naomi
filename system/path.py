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
    dirname,
    join,
    realpath,
    relpath,
)

from .state_store import STATE_STORE

# Calculates the relative path to the package’s root.
def package_relpath(path):
    return relpath(path, join(dirname(__file__), '..', '..'))

def packages_dir():
    return realpath(join(dirname(__file__), '..', '..'))

