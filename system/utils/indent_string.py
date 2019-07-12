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

from re import split


def indent_string(text, amount=1, spacer='    '):
    result = ''
    spacer = spacer * amount

    for line in split(r'\r?\n', text):
        if result != '':
            result += '\n'
        result += '%s%s' % (spacer, line)

    return result
