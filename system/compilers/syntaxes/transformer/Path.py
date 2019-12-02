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

class Path:
    __slots__ = [
        'parent',
        'node_path',
        'node_index',
        'node',
    ]

    def __init__(
        self,
        parent=None,
        node_path=None,
        node_index=-1,
        node=None,
    ):
        self.parent = parent
        self.node_path = node_path
        self.node_index = node_index
        self.node = node

    def replace_with(self, new_node):
        subnode_list = getattr(self.parent, self.node_path)

        if isinstance(subnode_list, list):
            subnode_list[self.node_index] = new_node
        else:
            setattr(self.parent, self.node_path, new_node)

        self.node = new_node
