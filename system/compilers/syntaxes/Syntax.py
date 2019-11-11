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


class Syntax:
    home_dir = None
    build_dir = None

    path = None
    parent_dir = None
    package_relpath = None

    settings = None
    raw = None

    name = None
    hidden = None
    scope = None
    scope_suffix = None
    file_extensions = None
    first_line_match = None

    variables = []
    contexts = []
