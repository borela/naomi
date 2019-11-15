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
from .Variable import Variable
from collections import OrderedDict


class Syntax(Node):
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

    """
    Variables indexed by their name.
    """
    variables = None

    """
    Contexts indexed by their name.
    """
    contexts = None

    """
    Files used in the compilation indexed by their path.
    """
    files = None

    """
    The file id will be prepended in all contexts to allow us to see the
    context’s origin.
    """
    files_ids = None

    """
    Some statements references external files or contexts, these are added to
    this dictionary to speed up the path resolution.
    """
    resources = None

    def __init__(self, settings):
        self.settings = settings

        self.variables = OrderedDict()
        self.contexts = OrderedDict()

        self.files = OrderedDict()
        self.files_ids = {}

        self.resources = OrderedDict()

    def get_sub_nodes(self):
        return self.variables + self.contexts

    def index_context(self, context):
        if not isinstance(context, Context):
            raise ParsingError('Object is not a context: %s' % context)

        self.contexts[context.name] = Context

    def index_file(self, syntax):
        if not isinstance(syntax, Syntax):
            raise ParsingError('Object is not a syntax file: %s' % syntax)

        path = syntax.path

        if path in self.files:
            return

        self.files[path] = syntax
        self.files_ids[path] = len(self.files)

    def index_resource(self, resource):
        if not isinstance(resource, Resource):
            raise ParsingError('Object is not a Resource: %s' % resource)

        self.resources[resource.path] = resource

    def index_variable(self, variable):
        if not isinstance(variable, Variable):
            raise ParsingError('Object is not a variable: %s' % variable)

        self.variables[variable.name] = variable
