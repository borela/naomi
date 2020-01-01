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

class Statement(Node):
    __slots__ = 'context'

    def __init__(self, context):
        Node.__init__(self)
        self.context = context

    @property
    def compilation(self):
        return self.context.syntax.compilation

    @property
    def syntax(self):
        return self.context.syntax
