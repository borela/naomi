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

from .Node import Node
from collections import OrderedDict


class Syntax(Node):
    home_dir = None
    build_dir = None

    path = None
    parent_dir = None
    package_relpath = None

    settings = None
    raw = None

    entry = False
    name = None
    hidden = None
    scope = None
    scope_suffix = None
    file_extensions = None
    first_line_match = None

    variables = None
    contexts = None

    """
    Files used in the compilation indexed by their path. We are using a
    OrderedDict to be able to see the order in which the files were included
    which could be useful when debugging.
    """
    files = None

    """
    The file id will be prepended in all contexts to allow us to see the
    context’s origin.
    """
    files_ids = None


    def __init__(self):
        self.files = OrderedDict()
        self.files_ids = {}


    def index_file(self, syntax):
        path = syntax.path

        if path in self.files:
            return

        self.files[path] = syntax
        self.files_ids[path] = len(self.files)
