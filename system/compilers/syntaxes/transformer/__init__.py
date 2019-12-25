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

from collections import (
    defaultdict,
    OrderedDict,
)

from ..ast import Node
from .Path import Path
from borela import trim_whitespace

import re

def get_visitors(name, visitors):
    result = []

    any_visitor = visitors.get('*', None)
    if any_visitor:
        result.extend(any_visitor)

    type_visitor = visitors.get(name, None)
    if type_visitor:
        result.extend(type_visitor)

    return result

def prepare_visitors(visitors):
    result = defaultdict(list)

    for key, visitors in visitors.items():
        if '|' not in key:
            if isinstance(visitors, list):
                result[key].extend(visitors)
            else:
                result[key].append(visitors)
            continue

        for node_type in key.split('|'):
            node_type = trim_whitespace(node_type)

            if isinstance(visitors, list):
                result[node_type].extend(visitors)
            else:
                result[node_type].append(visitors)

    return result

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
#         # Visit all nodes.
#         '*': [VisitorInstance, ...],
#
#         # Visit only NodeType.
#         'NodeType': [VisitorInstance, ...],
#
#         # Visit only NodeTypeA and NodeTypeB.
#         'NodeTypeA | NodeTypeB': [VisitorInstance, ...],
#
#         # If there’s just one visitor, a list is not necessary.
#         'NodeType': VisitorInstance,
#
#     }
def visit(path, visitors, visited=None):
    if not isinstance(path.node, Node):
        return

    # This is the first node being visited.
    if visited is None:
        visited = {}
        visitors = prepare_visitors(visitors)

    node = path.node
    node_hash = hash(node)

    if node_hash not in visited:
        visited[node_hash] = True
    else:
        return

    name = node.__class__.__name__
    node_visitors = get_visitors(name, visitors)

    # Enter.
    if len(node_visitors):
        for visitor in node_visitors:
            visitor.enter(path)

            # Node changed, revisit.
            if path.node is not node:
                return visit(path, visitors, visited)

    # Visit the subnodes.
    for subnode_name in node.get_subnodes():
        subnode = getattr(node, subnode_name)

        if not isinstance(subnode, (Node, OrderedDict, list)):
            continue

        # Subnode is a simple node.
        if isinstance(subnode, Node):
            visit(
                Path(
                    parent=node,
                    node_name=subnode_name,
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
                    node_name=subnode_name,
                    node_index=i,
                    node=subnode,
                ),
                visitors,
                visited,
            )

    # Exit.
    if len(node_visitors):
        for visitor in node_visitors:
            visitor.exit(path)

            # Node changed, revisit.
            if path.node is not node:
                return visit(path, visitors, visited)
