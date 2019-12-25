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

from ..TransformationError import TransformationError
from ..Visitor import Visitor
from borela.functions import make_words_regex

def join(arguments):
    return ''.join(arguments)

def word(argument):
    return '\b%s\b' % argument

def words(arguments):
    return make_words_regex(arguments)

FUNCTIONS = {
    'join': join,
    'word': word,
    'words': words,
}

class ExecuteFunctionCall(Visitor):
    def exit(self, path):
        node = path.node
        name = node.name
        arguments = node.arguments

        if name not in FUNCTIONS:
            raise TransformationError(
                message='Function not “%s” found.' % name,
                path=node.location.path,
                location=node.location,
            )

        path.replace_with(FUNCTIONS[name](arguments))
