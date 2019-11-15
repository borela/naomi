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


class Resource(Node):
    syntax = None
    context = None
    statement = None

    """
    Path used to import the resource without any modifcation.
    """
    path = None

    """
    Full path to the resource.
    """
    resolved_path = None

    """
    The actual resource.
    """
    resolved = None

    def __init__(self, syntax, context, statement, path):
        self.syntax = syntax
        self.context = context
        self.statement = statement
        self.path = path

        syntax.index_resource(self)
