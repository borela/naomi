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

from .Node import Node

class Context(Node):
    __slots__ = [
        'syntax',
        'name',
        'statements',
        # References to this context. This can be used to eliminate unused
        # contexts.
        'references',
    ]

    def __init__(self, syntax, name=None):
        Node.__init__(self)

        self.syntax = syntax
        self.name = name
        self.statements = []
        self.references = []

        if name is not None:
            self.syntax.index_context(self)

    def __repr__(self):
        return '[Context]: %s {\n%s\n}' % (
            self.name,
            indent_string(
                iterable_repr(self.statements)
            ),
        )

    @property
    def compilation(self):
        return self.syntax.compilation

    @property
    def full_path(self):
        path = self.syntax.path
        name = self.name
        return '%s#%s' % (path, name)

    def get_subnodes(self):
        return ['statements']
