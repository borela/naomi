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

from .word_list_to_word_binary_tree import word_list_to_word_binary_tree
from .word_binary_tree_to_string import word_binary_tree_to_string


def make_regex_to_match_words(words):
    # Sorting is not necessary but it will be easier to debug.
    words.sort()
    # This will turn the words into a binary tree and extract the root that
    # connect each group of words.
    tree = word_list_to_word_binary_tree(words)
    # Build the optimized regex.
    result = word_binary_tree_to_string(tree)
    # Add a word boundary to to prevent partial matches.
    return '\\b%s\\b' %result
