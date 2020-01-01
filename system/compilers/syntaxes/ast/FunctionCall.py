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

class FunctionCall(Node):
    __slots__ = [
        'name',
        'arguments',
    ]

    def __init__(self, name, arguments=None):
        Node.__init__(self)
        self.name = name
        self.arguments = arguments or []

    def __repr__(self):
        return '[FunctionCall] %s (\n%s\n)' % (
            self.name,
            indent_string(
                iterable_repr(self.arguments)
            ),
        )

    def get_subnodes(self):
        return ['arguments']
