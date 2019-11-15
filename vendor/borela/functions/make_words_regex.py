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
from borela import Stack
from collections import deque


class Node:
    root = None
    child = None
    orphan = None

    def __init__(self, root=None, child=None, orphan=None):
        self.root = root
        self.child = child or []
        self.orphan = orphan or []

    def __repr__(self):
        body = '>> %s' % repr(self.child)
        body += '\n'
        body += '|| %s' % repr(self.orphan)

        return '%s {\n%s\n}' % (
            self.root,
            indent_string(body),
        )


class Child(Node):
    pass


class Orphan(Node):
    pass


def extract_root(words, constructor):
    if len(words) == 0:
        return None

    if len(words) == 1 and not words[0]:
        return None

    root = words[0][:1]

    if not root:
        return constructor('', words[1:])

    child = []
    orphan = []

    if root:
        for word in words:
            if word.startswith(root):
                child.append(word[1:])
            else:
                orphan.append(word)
    else:
        orphan = words[1:]

    return constructor(root, child, orphan)


def make_words_regex(words):
    """
    Transforms a list of words into an optimized regex, for example:

        foo
        bar
        baz
        foobar
        foobaz

    becomes:

        \b(?>ba(?>r|z)|foo(?:ba(?>r|z))?)\b
    """

    # Sorting is not necessary but it will be easier to debug.
    words.sort()
    # This will turn the words into a binary tree and extract the root that
    # connect each character of them.
    tree = words_to_binary_tree(words)
    # Build the optimized regex.
    return '\\b%s\\b' % tree_to_string(tree)


def tree_to_string(tree):
    temp = Stack([tree])
    queue = Stack()

    # Generate a queue to visit the nodes using postorder traversal. The
    # “child” is left node and “orphan” is right node of the binary tree.
    while len(temp) > 0:
        node = temp.pop()

        if isinstance(node.orphan, Node):
            temp.push(node.orphan)

        if isinstance(node.child, Node):
            temp.push(node.child)

        queue.push(node)

    # Collapse nodes while generating the pattern.
    for node in queue:
        if node.root == '':
            if node.child.root.startswith('(?'):
                node.root = node.child.root + '?'
            else:
                node.root = '(?:%s)?' % node.child.root
            continue

        child = node.child
        orphan = node.orphan

        if child and orphan:
            # This is not necessary but it will eliminate unnecessary atomic
            # groups resulting in a cleaner regex.
            if orphan.root.startswith('(?>'):
                orphan.root = orphan.root[3:-1]

            node.root = '(?>%s%s|%s)' % (
                node.root,
                child.root,
                orphan.root,
            )
            continue

        if isinstance(node, Child):
            if orphan and not child:
                node.root = '(?>%s|%s)' % (node.root, orphan.root)
                continue

        if isinstance(node, Orphan):
            if orphan and not child:
                node.root += '|' + orphan.root
                continue

        if child and not orphan:
            node.root += child.root

    # The last node visited will have the full pattern.
    return node.root


def words_to_binary_tree(words):
    main = extract_root(words, Node)
    node = None
    queue = [main]

    while len(queue) > 0:
        node = queue.pop(0)
        node.child = extract_root(node.child, Child)
        node.orphan = extract_root(node.orphan, Orphan)

        if isinstance(node.child, Node):
            queue.append(node.child)

        if isinstance(node.orphan, Node):
            queue.append(node.orphan)

    return main
