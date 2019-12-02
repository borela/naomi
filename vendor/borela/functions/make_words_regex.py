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

from .indent_string import indent_string

class Node:
    __slots__ = [
        # Character that this node represents. An empty string means that it
        # is an optional group and “None” means the root node.
        'char',
        'children',
    ]

    def __init__(self, char=None):
        self.char = char
        self.children = []

    def __repr__(self):
        node_id = self.char

        if self.char is None:
            node_id = '[Root]'

        if self.char == '':
            node_id = '[Optional]'

        if len(self.children) < 1:
            return node_id

        children_string = ''
        for child in self.children:
            children_string += '\n>> ' + repr(child)

        return '%s%s' % (
            node_id,
            indent_string(children_string),
        )

def generate_pattern(node):
    children_string = ''

    for child in node.children:
        if children_string:
            children_string += '|'
        children_string += generate_pattern(child)

    if len(node.children) > 1:
        children_string = '(?>%s)' % children_string

    if node.char is None:
        return r'\b%s\b' % children_string

    if node.char == '':
        if children_string.startswith('('):
            return children_string + '?'
        else:
            return '(?:%s)?' % children_string

    return node.char + children_string

# Groups a list of words by their first character and remove it from the them.
# This is used to construct the tree.
def group_words(words):
    if not words:
        return words

    if len(words) < 2 and not words[0]:
        return []

    # Optional group.
    if words[0] == '':
        node = Node('')
        node.children = words[1:]
        return [node]

    char = None
    node = None
    result = []

    for word in words:
        if char is None or not word.startswith(char):
            char = word[:1]
            node = Node(char)
            result.append(node)

        word = word[1:]

        if word == '' and node.children:
            if node.children[0] == '':
                # The only sittuation we will get here is if there are
                # duplicated words.
                continue

        node.children.append(word)

    return result

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
    words.sort()
    # This will turn the words into a tree grouping their parts by the left
    # most character until each node is a single character.
    tree = words_to_tree(words)
    # Build the optimized regex.
    return generate_pattern(tree)

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
#     [Root]
#         >> b
#             >> a
#                 >> r
#                 >> z
#         >> f
#             >> o
#                 >> o
#                     >> [Optional]
#                         >> b
#                             >> a
#                                 >> r
#                                 >> z
def words_to_tree(words):
    root = Node()
    root.children = words

    def group_children(node):
        node.children = group_words(node.children)
        for node in node.children:
            group_children(node)

    group_children(root)
    return root
