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

from .ast import Context
from .parse_clear_scopes import parse_clear_scopes
from .parse_include import parse_include
from .parse_match import parse_match
from .parse_meta_content_scope import parse_meta_content_scope
from .parse_meta_scope import parse_meta_scope
from .ParsingError import ParsingError

def parse_context(syntax, name, raw):
    context = Context(syntax)
    context.name = name

    for statement in raw:
        if 'clear_scopes' in statement:
            context.statements.append(parse_clear_scopes(
                context,
                statement,
            ))
            continue

        if 'include' in statement:
            context.statements.append(parse_include(
                context,
                statement,
            ))
            continue

        if any(key in ['match', 'match_words'] for key in statement):
            context.statements.append(parse_match(
                context,
                statement,
            ))
            continue

        if 'meta_content_scope' in statement:
            context.statements.append(parse_meta_content_scope(
                context,
                statement,
            ))
            continue

        if 'meta_scope' in statement:
            context.statements.append(parse_meta_scope(
                context,
                statement,
            ))
            continue

        raise ParsingError(
            'Unexpected statement: %s' % statement,
            statement,
        )

    return context
