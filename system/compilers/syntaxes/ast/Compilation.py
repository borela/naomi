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
from .Context import Context
from .Node import Node
from .Resource import Resource
from .Syntax import Syntax
from .Variable import Variable
from borela import Stack
from collections import OrderedDict

class Statistics(Node):
    __slots__ = [
        'contexts',
        'files',
    ]

class Compilation(Node):
    __slots__ = [
        'settings',

        # Location where the compiled file will be saved.
        'build_dir',

        # Entry syntax file.
        'entry',

        # Files used in the compilation indexed by their path.
        'syntaxes',

        # The file id will be prepended in all contexts to allow us to see the
        # context’s origin.
        'syntaxes_ids',

        # Contexts indexed by their full path.
        'contexts',

        # Variables indexed by their full path.
        'variables',

        # Some statements references internal/external files or contexts.
        'resources',
        'queued_resources',

        # Data such as number of contexts, files used, etc...
        'statistics',
    ]

    def __init__(self, settings, build_dir):
        self.settings = settings
        self.build_dir = build_dir

        self.syntaxes = OrderedDict()
        self.syntaxes_ids = OrderedDict()

        self.contexts = OrderedDict()
        self.variables = OrderedDict()

        self.resources = OrderedDict()
        self.queued_resources = Stack()

        self.statistics = Statistics()

    def enqueue_resource(self, statement, origin, path):
        self.queued_resources.push(Resource(
            statement,
            origin,
            path,
        ))

    def index_context(self, context):
        if not isinstance(context, Context):
            raise ParsingError('Object is not a Context: %s' % context)

        path = context.syntax.path
        name = context.name

        self.contexts['%s#%s' % (path, name)] = context

    def index_syntax(self, syntax):
        if not isinstance(syntax, Syntax):
            raise ParsingError('Object is not a syntax file: %s' % syntax)

        path = syntax.path

        if path not in self.syntaxes:
            self.syntaxes[path] = syntax
            self.syntaxes_ids[path] = len(self.syntaxes)

    def index_resource(self, resource):
        if not isinstance(resource, Resource):
            raise ParsingError('Object is not a Resource: %s' % resource)

        self.resources[resource.path] = resource

    def index_variable(self, variable):
        if not isinstance(variable, Variable):
            raise ParsingError('Object is not a Variable: %s' % variable)

        path = variable.syntax.path
        name = variable.name

        self.variables['%s#%s' % (path, name)] = variable
