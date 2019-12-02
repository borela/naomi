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

from ..ast import Node
from .Path import Path
from .visitors import ExecuteFunctionCall
from collections import OrderedDict

def transform(root):
    visitors = {
        'FunctionCall': ExecuteFunctionCall(),
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

def visit(path, visitors):
    node = path.node
    name = node.__class__.__name__
    visitor = visitors.get(name, None)

    # Enter.
    if visitor:
        visitor.enter(path)

        # Node changed, revisit.
        if path.node is not node:
            return visit(path, visitors)

    # Visit the subnodes.
    for subnode_path in node.get_subnodes():
        subnode = getattr(node, subnode_path)

        if isinstance(subnode, (str, bool, int, float)):
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
            )
            continue

        # Subnode is actually multiple nodes.
        if isinstance(subnode, OrderedDict):
            subnodes = subnode.values()
        elif isinstance(subnode, list):
            subnodes = subnode

        for subnode in subnodes:
            visit(
                Path(
                    parent=node,
                    node_path=subnode_path,
                    node=subnode,
                ),
                visitors,
            )

    # Exit.
    if visitor:
        visitor.exit(path)

    # Node changed, revisit.
    if path.node is not node:
        return visit(path, visitors)
