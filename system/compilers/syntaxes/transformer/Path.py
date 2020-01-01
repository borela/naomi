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

from ..ast import (
    Context,
    Variable,
)

class Path:
    __slots__ = [
        'parent',
        'node_name',
        'node_index',
        'node',
    ]

    def __init__(
        self,
        parent=None,
        node_name=None,
        node_index=-1,
        node=None,
    ):
        self.parent = parent
        self.node_name = node_name
        self.node_index = node_index
        self.node = node

    def replace_with(self, new_node):
        subnode_list = getattr(self.parent, self.node_name)

        if isinstance(subnode_list, list):
            subnode_list[self.node_index] = new_node
        else:
            setattr(self.parent, self.node_name, new_node)

        self.node = new_node

    def remove_node(self):
        if isinstance(self.node, (Context, Variable)):
            if isinstance(self.node, Context) and self.node.name:
                self.node.compilation.remove_context(self.node.full_path)
            elif isinstance(self.node, Variable):
                self.node.compilation.remove_variable(self.node.full_path)
        else:
            subnode_list = getattr(self.parent, self.node_name)

            if isinstance(subnode_list, list):
                del subnode_list[self.node_index]
            else:
                delattr(self.parent, self.node_name)

        self.node = None
