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
    isabs,
    join,
    realpath,
)

from Naomi.system.state import STORE


def resolve_path(path):
    """
    Resolve relative paths to the syntaxes src directory.
    """
    if not isabs(path):
        path = join(STORE['directories']['syntaxes']['src'], path)
    return realpath(path)
