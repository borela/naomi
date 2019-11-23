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

from ..Stack import Stack
from .indent_string import indent_string
from re import sub

class Node:
    __slots__ = [
        # Character that this node represents. An empty string means that it
        # is an optional group and “None” means the root node.
        'char',

        # Node level in the tree.
        'level',

        # Nodes.
        'parent',
        'children',
    ]

    def __init__(self, parent=None, char=None):
        self.char = char
        self.level = parent.level + 1 if parent else 0
        self.parent = parent
        self.children = []

    def __repr__(self):
        node_id = self.char

        if self.char == None:
            node_id = '[Root]'

        if self.char == '':
            node_id = '[Optional]'

        if len(self.children) < 1:
            return node_id

        children_string = ''

        for child in self.children:
            children_string += '\n>> ' + repr(child)

        return '%i: %s%s' % (
            self.level,
            node_id,
            indent_string(children_string),
        )

class Visitor:
    __slots__ = [
        'groups',
        'pattern',
    ]

    def __init__(self):
        self.groups = Stack()
        self.pattern = ''

    def on_enter(self, node):
        if node.char:
            self.pattern += node.char

        if len(node.children) > 1:
            self.groups.push(node)
            self.pattern += '(?>'
        elif node.char == '':
            self.groups.push(node)
            self.pattern += '(?:'

    def on_exit(self, node):
        if node != self.groups[-1]:
            self.pattern += '|'
            return

        self.groups.pop()
        self.pattern += ')'

        if node.char == '':
            self.pattern += '?'

# Groups a list of words by their first character and remove it from the them.
# This is used to construct the tree.
def extract_char(parent, words):
    if not words:
        return words

    if len(words) < 2 and not words[0]:
        return []

    char = None
    children = []

    for word in words:
        if char == None or char and not word.startswith(char):
            char = word[:1]
            node = Node(parent, char)
            children.append(node)

        if char:
            word = word[1:]

        if char or word:
            node.children.append(word)

    return children

# Transforms a list of words into an optimized regex, for example:
#
#     foo
#     bar
#     baz
#     foobar
#     foobaz
#
# becomes:
#
#    \b(?>ba(?>r|z)|foo(?:ba(?>r|z))?)\b
def make_words_regex(words):
    # Sorting is not necessary but it will be easier to debug.
    words.sort()
    # This will turn the words into a binary tree and extract the char that
    # connect each character of them.
    tree = words_to_tree(words)
    # Build the optimized regex.
    return tree_to_string(tree)

# Traverse the tree to generate the pattern using the visitor.
def tree_to_string(root):
    visitor = Visitor()
    visited = Stack()

    queue = Stack()
    queue.push(root)
    previous = root

    while queue:
        node = queue.pop()

        while node.level < previous.level:
            previous = visited.pop()
            visitor.on_exit(previous)

        visitor.on_enter(node)
        visited.push(node)

        if not node.children:
            visitor.on_exit(node)
            visited.pop()
        else:
            for child in reversed(node.children):
                queue.push(child)

        previous = node

    while visited:
        node = visited.pop()
        visitor.on_exit(node)

    pattern = visitor.pattern
    pattern = sub(r'\|+', '|', pattern)
    pattern = sub(r'\|\)', ')', pattern)

    return r'\b%s\b' % pattern

# Transforms the words into a tree:
#
#     foo
#     bar
#     baz
#     foobar
#     foobaz
#
# becomes:
#
#     0: [Root]
#        >> 1: b
#            >> 2: a
#                >> r
#                >> z
#        >> 1: f
#            >> 2: o
#                >> 3: o
#                    >> 4: [Optional]
#                        >> 5: b
#                            >> 6: a
#                                >> r
#                                >> z
def words_to_tree(words):
    root = Node()
    root.children = words

    queue = Stack()
    queue.push(root)

    while queue:
        node = queue.pop()
        node.children = extract_char(node, node.children)

        for child in node.children:
            queue.push(child)

    return root
