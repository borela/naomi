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
    left = None
    right = None

    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left or []
        self.right = right or []

    def __repr__(self):
        body = '>> %s' % repr(self.left)
        body += '\n'
        body += '|| %s' % repr(self.right)

        return '%s {\n%s\n}' % (
            self.root,
            indent_string(body),
        )


class Left(Node):
    pass


class Right(Node):
    pass


def extract_root(words, constructor):
    if len(words) == 0:
        return None

    if len(words) == 1 and not words[0]:
        return None

    root = words[0][:1]

    if not root:
        return constructor('', words[1:])

    left = []
    right = []

    if root:
        for word in words:
            if word.startswith(root):
                left.append(word[1:])
            else:
                right.append(word)
    else:
        right = words[1:]

    return constructor(root, left, right)


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

    # Generate a queue to visit the nodes using postorder traversal.
    while len(temp) > 0:
        node = temp.pop()

        if isinstance(node.right, Node):
            temp.push(node.right)

        if isinstance(node.left, Node):
            temp.push(node.left)

        queue.push(node)

    # Collapse nodes while generating the pattern.
    for node in queue:
        if node.root == '':
            if node.left.root.startswith('(?'):
                node.root = node.left.root + '?'
            else:
                node.root = '(?:%s)?' % node.left.root
            continue

        left = node.left
        right = node.right

        if left and right:
            # This is not necessary but it will eliminate unnecessary atomic
            # groups resulting in a cleaner regex.
            if right.root.startswith('(?>'):
                right.root = right.root[3:-1]

            node.root = '(?>%s%s|%s)' % (
                node.root,
                left.root,
                right.root,
            )
            continue

        if isinstance(node, Left):
            if right and not left:
                node.root = '(?>%s|%s)' % (node.root, right.root)
                continue

        if isinstance(node, Right):
            if right and not left:
                node.root += '|' + right.root
                continue

        if left and not right:
            node.root += left.root

    # The last node visited will have the full pattern.
    return node.root


def words_to_binary_tree(words):
    main = extract_root(words, Node)
    node = None
    queue = [main]

    while len(queue) > 0:
        node = queue.pop(0)
        node.left = extract_root(node.left, Left)
        node.right = extract_root(node.right, Right)

        if isinstance(node.left, Node):
            queue.append(node.left)

        if isinstance(node.right, Node):
            queue.append(node.right)

    return main
