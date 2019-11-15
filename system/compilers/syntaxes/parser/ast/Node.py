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

from borela.functions import indent_string


class Node:
    def __repr__(self):
        body = ''

        for member in vars(self):
            if member in ['syntax', 'context', 'statement', 'raw']:
                value = '...'
            else:
                value = getattr(self, member)

            if body:
                body += '\n'

            body += '%s: %s' % (member, repr(value))

        return '%s {\n%s\n}' % (
            self.__class__.__name__,
            indent_string(body),
        )

    def get_sub_nodes(self):
        """
        This method is used by the traversal function to collect and visit
        the tree nodes without using recursion.
        """
        raise None
