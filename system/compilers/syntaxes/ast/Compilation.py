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

from borela.functions import (
    indent_string,
    iterable_repr,
)

from ..ParsingError import ParsingError
from .Context import Context
from .ContextRequest import ContextRequest
from .Node import Node
from .Syntax import Syntax
from .Variable import Variable
from .VariableRequest import VariableRequest
from borela import Stack
from collections import OrderedDict

class Statistics(Node):
    __slots__ = [
        'contexts',
        'contexts_inlined',
        'contexts_removed',
        'files',
        'variables',
        'variables_removed',
    ]

    def __init__(self):
        Node.__init__(self)
        self.contexts = 0
        self.contexts_inlined = 0
        self.contexts_removed = 0
        self.files = 0
        self.variables = 0
        self.variables_removed = 0

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

        # Variables and contexts that need to be resolved after parsing the
        # syntax.
        'context_requests',
        'variable_requests',

        # Data such as number of contexts, files used, etc...
        'statistics',
    ]

    def __init__(self, settings, build_dir):
        Node.__init__(self)

        self.settings = settings
        self.build_dir = build_dir

        self.syntaxes = OrderedDict()
        self.syntaxes_ids = OrderedDict()

        self.contexts = OrderedDict()
        self.variables = OrderedDict()

        self.context_requests = Stack()
        self.variable_requests = Stack()

        self.statistics = Statistics()

    def __repr__(self):
        return '[Compilation] {\n%s\n}' % indent_string(
            iterable_repr(self.syntaxes.values())
        )

    def enqueue_context_request(self, statement, origin, path):
        request = ContextRequest(
            statement,
            origin,
            path,
        )
        self.context_requests.push(request)
        return request

    def enqueue_variable_request(self, syntax, origin, path):
        request = VariableRequest(
            syntax,
            origin,
            path,
        )
        self.variable_requests.push(request)
        return request

    def get_subnodes(self):
        return ['entry']

    def index_context(self, context):
        if not isinstance(context, Context):
            raise ParsingError('Object is not a Context: %s' % context)

        path = context.syntax.path
        name = context.name

        self.contexts['%s#%s' % (path, name)] = context
        self.statistics.contexts += 1

    def index_syntax(self, syntax):
        if not isinstance(syntax, Syntax):
            raise ParsingError('Object is not a syntax file: %s' % syntax)

        path = syntax.path

        if path not in self.syntaxes:
            self.syntaxes[path] = syntax
            self.syntaxes_ids[path] = len(self.syntaxes)
            self.statistics.files += 1

        syntax.syntax_id = self.syntaxes_ids[path]

    def index_variable(self, variable):
        if not isinstance(variable, Variable):
            raise ParsingError('Object is not a Variable: %s' % variable)

        path = variable.syntax.path
        name = variable.name

        self.variables['%s#%s' % (path, name)] = variable
        self.statistics.variables += 1
