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
from .Variable import Variable
from borela.functions import indent_string
from collections import OrderedDict
from Naomi.system import package_relpath
from os.path import dirname

class Syntax(Node):
    __slots__ = [
        'syntax_id',
        'compilation',

        'home_dir',
        'path',
        'parent_dir',
        'package_relpath',

        # Unmodified YAML data.
        'raw',

        'name',
        'hidden',
        'scope',
        'scope_prefix',
        'scope_suffix',
        'file_extensions',
        'first_line_match',

        # Variables indexed by their name.
        'variables',

        # Contexts indexed by their name.
        'contexts',
    ]

    def __init__(self, compilation, home_dir, path):
        self.syntax_id = -1
        self.compilation = compilation

        self.home_dir = home_dir
        self.path = path
        self.parent_dir = dirname(path)
        self.package_relpath = package_relpath(path)

        self.variables = OrderedDict()
        self.contexts = OrderedDict()

    def __repr__(self):
        variables = ''
        for _, variable in self.variables.items():
            if variables:
                variables += '\n'
            variables += repr(variable)

        contexts = ''
        for _, context in self.contexts.items():
            if contexts:
                contexts += '\n'
            contexts += repr(context)

        if variables:
            variables = 'Variables: [\n%s\n]' % indent_string(variables)
        else:
            variables = 'Variables: []'

        if contexts:
            contexts = 'Contexts: [\n%s\n]' % indent_string(contexts)
        else:
            contexts = 'Contexts: []'

        return '[Syntax]: %s (%i) {\n%s\n%s\n}' % (
            self.package_relpath,
            self.syntax_id,
            indent_string(variables),
            indent_string(contexts),
        )

    def get_subnodes(self):
        return [
            'variables',
            'contexts',
        ]

    def index_context(self, context):
        if not isinstance(context, Context):
            raise ParsingError('Object is not a Context: %s' % context)

        self.contexts[context.name] = context
        self.compilation.index_context(context)

    def index_variable(self, variable):
        if not isinstance(variable, Variable):
            raise ParsingError('Object is not a Variable: %s' % variable)

        self.variables[variable.name] = variable
        self.compilation.index_variable(variable)
