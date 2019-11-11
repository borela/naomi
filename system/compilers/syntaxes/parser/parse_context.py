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

from .ast import ContextDeclaration
from .parse_clear_scopes import parse_clear_scopes
from .parse_include import parse_include
from .parse_match import parse_match
from .parse_meta_content_scope import parse_meta_content_scope
from .parse_meta_scope import parse_meta_scope


def parse_context(syntax, name, raw):
    context = ContextDeclaration()
    context.syntax = syntax
    context.raw = raw
    context.name = name

    for statement in raw:
        if any(key in ['match', 'match_words'] for key in statement):
            context.statements.append(parse_match(
                syntax,
                context,
                statement,
            ))
            continue

        if 'include' in statement:
            context.statements.append(parse_include(
                syntax,
                context,
                statement,
            ))
            continue

        if 'meta_scope' in statement:
            context.statements.append(parse_meta_scope(
                syntax,
                context,
                statement,
            ))
            continue

        if 'meta_content_scope' in statement:
            context.statements.append(parse_meta_content_scope(
                syntax,
                context,
                statement,
            ))
            continue

        if 'clear_scopes' in statement:
            context.statements.append(parse_clear_scopes(
                syntax,
                context,
                statement,
            ))
            continue

        raise SyntaxError('Unexpected statement: %s (%i, %i)' % (
            statement,
            statement.lc.line,
            statement.lc.col,
        ))

    return context
