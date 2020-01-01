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

from .StackAction import StackAction

class Set(StackAction):
    __slots__ = 'sequence'

    def __init__(self, match):
        StackAction.__init__(self, match)
        self.sequence = []

    def __repr__(self):
        return '[Set] [\n%s\n]' % indent_string(
            iterable_repr(self.sequence)
        )

    def get_subnodes(self):
        return ['sequence']
