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

from .ClearScopes import ClearScopes
from .Include import Include
from .Match import Match
from .Statement import Statement
from .SetMetaScope import SetMetaScope
from .SetMetaContentScope import SetMetaContentScope


class ContextDeclaration(Statement):
    name = None
    statements = []

    def __init__(self, name, raw):
        Statement.__init__(self, raw)
        self.name = name

        for statement in self.raw:
            if any(key in ['match', 'match_words'] for key in statement):
                self.statements.append(Match(statement))
                continue

            if 'include' in statement:
                self.statements.append(Include(statement))
                continue

            if 'meta_scope' in statement:
                self.statements.append(SetMetaScope(statement))
                continue

            if 'meta_content_scope' in statement:
                self.statements.append(SetMetaContentScope(statement))
                continue

            if 'clear_scopes' in statement:
                self.statements.append(ClearScopes(statement))
                continue

            raise SyntaxError('Unexpected statement: %s' % statement)
