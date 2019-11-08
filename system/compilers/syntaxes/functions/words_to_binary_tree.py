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


def words_to_binary_tree(words):
    if all([len(word) == 1 for word in words]):
        return words

    node = {
        'root': '',
        'left': [],
        'right': [],
    }

    character = words[0][:1]

    if character:
        node['root'] += character

        for word in words:
            if word.startswith(character):
                node['left'].append(word[1:])
            else:
                node['right'].append(word)
    else:
        node['right'] = words[1:]

    node['left'] = words_to_binary_tree(node['left'])
    node['right'] = words_to_binary_tree(node['right'])

    return node
