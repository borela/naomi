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

from .visitors import (
    ExecuteFunctionCall,
    ResolveVariableRequest,
)

from ..ast import Node
from .Path import Path
from collections import OrderedDict

def transform(root):
    visitors = {
        'FunctionCall': ExecuteFunctionCall(),
        'VariableRequest': ResolveVariableRequest(),
    }
    visit(Path(node=root), visitors)

# Visit each node in the tree allowing visitors to modify it. The visitors
# dictionary follows the format:
#
#     {
#         # TODO: Visit all nodes.
#         '*': VisitorInstance,
#
#         # Visit only NodeType.
#         'NodeType': VisitorInstance,
#
#         # TODO: Visit only NodeTypeA and NodeTypeB.
#         'NodeTypeA | NodeTypeB': VisitorInstance,
#     }
def visit(path, visitors, visited=None):
    if not isinstance(path.node, Node):
        return

    if visited is None:
        visited = {}

    node = path.node
    node_hash = hash(node)

    if node_hash not in visited:
        visited[node_hash] = True
    else:
        return

    name = node.__class__.__name__
    visitor = visitors.get(name, None)

    # Enter.
    if visitor:
        visitor.enter(path)

        # Node changed, revisit.
        if path.node is not node:
            return visit(path, visitors, visited)

    # Visit the subnodes.
    for subnode_path in node.get_subnodes():
        subnode = getattr(node, subnode_path)

        if not isinstance(subnode, (Node, OrderedDict, list)):
            continue

        # Subnode is a simple node.
        if isinstance(subnode, Node):
            visit(
                Path(
                    parent=node,
                    node_path=subnode_path,
                    node=subnode,
                ),
                visitors,
                visited,
            )
            continue

        # Subnode is actually multiple nodes.
        if isinstance(subnode, OrderedDict):
            subnodes = subnode.values()
        elif isinstance(subnode, list):
            subnodes = subnode
        else:
            raise ValueError('Unexpected node type: %s' % type(subnode))

        for i, subnode in enumerate(subnodes):
            if not isinstance(subnode, Node):
                continue

            visit(
                Path(
                    parent=node,
                    node_path=subnode_path,
                    node_index=i,
                    node=subnode,
                ),
                visitors,
                visited,
            )

    # Exit.
    if visitor:
        visitor.exit(path)

    # Node changed, revisit.
    if path.node is not node:
        return visit(path, visitors, visited)
