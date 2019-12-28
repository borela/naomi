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

class Variable(Node):
    __slots__ = [
        'syntax',
        'name',
        'pattern',
        # References to this context. This can be used to eliminate unused
        # contexts.
        'references',
    ]

    def __init__(self, syntax, name):
        Node.__init__(self)
        self.name = name
        self.references = []

        self.syntax = syntax
        self.syntax.index_variable(self)

    def __repr__(self):
        return '[Variable]: %s' % self.name

    @property
    def compilation(self):
        return self.syntax.compilation

    @property
    def full_path(self):
        path = self.syntax.path
        name = self.name
        return '%s#%s' % (path, name)

    def get_subnodes(self):
        return ['pattern']
