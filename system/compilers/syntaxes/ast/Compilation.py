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

from ..ParsingError import ParsingError
from .Node import Node
from .Resource import Resource
from .Syntax import Syntax
from collections import OrderedDict

class Statistics(Node):
    __slots__ = [
        'contexts',
        'files',
    ]

class Compilation(Node):
    __slots__ = [
        'settings',

        # str: Location where the compiled file will be saved.
        'build_dir',

        # Syntax: Entry syntax file.
        'entry',

        # OrderedDict: Files used in the compilation indexed by their path.
        'files',

        # dict: The file id will be prepended in all contexts to allow us to
        # see the context’s origin.
        'files_ids',
        # Some statements references external files or contexts, these are
        # added to this dictionary to speed up the path resolution.
        'resources',
        # Statistics: Data such as number of contexts, files used, etc...
        'statistics',
    ]

    def __init__(self, settings, build_dir):
        self.settings = settings
        self.build_dir = build_dir

        self.files = OrderedDict()
        self.files_ids = {}

        self.resources = OrderedDict()
        self.statistics = Statistics()

    def index_file(self, syntax, parent):
        if not isinstance(syntax, Syntax):
            raise ParsingError('Object is not a syntax file: %s' % syntax)

        path = syntax.path

        if path not in self.files:
            self.files[path] = syntax
            self.files_ids[path] = len(self.files)

    def index_resource(self, resource):
        if not isinstance(resource, Resource):
            raise ParsingError('Object is not a Resource: %s' % resource)

        self.resources[resource.path] = resource
