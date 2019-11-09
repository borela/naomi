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

from .Pop import Pop
from .Push import Push
from .Set import Set
from .Statement import Statement
from .WithPrototype import WithPrototype
from borela.functions import make_regex_to_match_words


class Match(Statement):
    pattern = None
    captures = None
    scope = None
    stack_control = None
    with_prototype = None

    def __init__(self, raw):
        Statement.__init__(self, raw)

        for key, value in raw.items():
            if key == 'match':
                self.pattern = value
                continue

            if key == 'match_words':
                self.pattern = make_regex_to_match_words(value)
                print(self.pattern)
                continue

            if key == 'scope':
                self.scope = value
                continue

            if key == 'captures':
                self.captures = value
                continue

            if key == 'with_prototype':
                self.with_prototype = WithPrototype(value)
                continue

            if key in ['push', 'set', 'pop']:
                if self.stack_control:
                    raise SyntaxError(
                        'Multiple stack control statements. (%i, %i)' %
                        value.lc.line,
                        value.lc.col,
                    )

                if key == 'push':
                    self.stack_control = Push(value)
                    continue

                if key == 'set':
                    self.stack_control = Set(value)
                    continue

                if key == 'pop':
                    self.stack_control = Pop(value)
                    continue

            raise SyntaxError('Unexpected statement: %s (%i, %i)' % (
                key,
                value.lc.line,
                value.lc.col,
            ))
