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

class ContextRequest(Node):
    __slots__ = [
        'statement',
        # Exact location of the request.
        'origin',
        # Path used to import the context without any modifcation.
        'path',
        # Full path to the context.
        'resolved_path',
        # The actual context.
        'resolved',
    ]

    def __init__(self, statement, origin, path):
        Node.__init__(self)
        self.statement = statement
        self.origin = origin
        self.path = path

    def __repr__(self):
        return '[ContextRequest]: %s' % self.path

    @property
    def compilation(self):
        return self.statement.compilation

    @property
    def context(self):
        return self.statement.context

    @property
    def syntax(self):
        return self.statement.syntax

    def get_subnodes(self):
        return ['resolved']
