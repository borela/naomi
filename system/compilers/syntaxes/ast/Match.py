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

from borela.functions import (
    indent_string,
    iterable_repr,
)

from .Statement import Statement

class Match(Statement):
    __slots__ = [
        # The actual match pattern.
        'pattern',
        # Scope to be applied to the entire pattern.
        'scope',
        # An optional action to the stack: embed, pop, push, set.
        'action',
        # Applies scopes to capturing groups.
        'captures',
        # Creates a copy of the entire graph of contexts with the rules
        # defined here.
        'with_prototype',
    ]

    def __init__(self, context):
        Statement.__init__(self, context)
        self.pattern = None
        self.scope = None
        self.action = None
        self.captures = None
        self.with_prototype = None

    def __repr__(self):
        body = 'Pattern: ' + repr(self.pattern)

        if self.scope:
            body += '\nScope: ' + repr(self.scope)

        if self.captures:
            body += '\nCaptures: ' + repr(self.captures)

        if self.action:
            body += '\n' + repr(self.action)

        if self.with_prototype:
            body += '\n' + repr(self.with_prototype)

        return '[Match] {\n%s\n}' % indent_string(body)

    def get_subnodes(self):
        return [
            'pattern',
            'action',
            'with_prototype',
        ]
