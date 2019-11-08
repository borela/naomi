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


def word_binary_tree_to_string(node):
    root = node['root']
    left = node['left']
    right = node['right']

    left_pattern = ''
    if isinstance(left, list):
        if len(left) > 0:
            left_pattern = '(?>%s)' % '|'.join(left)
    else:
        left_pattern = word_binary_tree_to_string(left)

    right_pattern = ''
    if len(right) < 1:
        return root + left_pattern

    right_pattern = word_binary_tree_to_string(right)

    if not left_pattern:
        return '(?:%s)?' % (root + right_pattern)

    return '(?>%s|%s)' % ((root + left_pattern), right_pattern)
