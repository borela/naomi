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

from .ast import (
    FunctionCall,
    Match,
)

from .parse_embed import parse_embed
from .parse_expression import parse_expression
from .parse_pop import parse_pop
from .parse_push import parse_push
from .parse_set import parse_set
from .ParsingError import ParsingError

def parse_match(context, raw):
    statement = Match(context)
    syntax = statement.syntax

    match_parsed = False
    scope_parsed = False
    captures_parsed = False

    for key, value in raw.items():
        # This key is processed by the embed statement and can be ignored if
        # one is present.
        if key == 'escape':
            if 'embed' not in raw:
                raise ParsingError(
                    '“escape” statement without embed.',
                    syntax,
                    key.lc,
                )
            statement.escape = value
            continue

        if key == 'match':
            if match_parsed:
                raise_multiple_match(syntax, key.lc)

            statement.pattern = parse_expression(value)
            match_parsed = True
            continue

        if key == 'match_word':
            if match_parsed:
                raise_multiple_match(syntax, key.lc)

            statement.pattern = FunctionCall('word', value)
            match_parsed = True
            continue

        if key == 'match_words':
            if match_parsed:
                raise_multiple_match(syntax, key.lc)

            statement.pattern = FunctionCall('words', value)
            match_parsed = True
            continue

        if key == 'scope':
            if captures_parsed:
                raise_multiple_scope(syntax, key.lc)
            statement.scope = value
            scope_parsed = True
            continue

        if key == 'captures':
            if scope_parsed:
                raise_multiple_scope(syntax, key.lc)
            statement.captures = value
            captures_parsed = True
            continue

        if key == 'with_prototype':
            statement.with_prototype = value
            continue

        if key in ['embed', 'pop', 'push', 'set']:
            if statement.stack_action:
                raise ParsingError(
                    'Multiple stack control statements.',
                    syntax,
                    key.lc,
                )

            if key == 'embed':
                statement.stack_action = parse_embed(
                    statement,
                    value,
                )
                continue

            if key == 'pop':
                statement.stack_action = parse_pop(
                    statement,
                    value,
                )
                continue

            if key == 'push':
                statement.stack_action = parse_push(
                    statement,
                    value,
                )
                continue

            if key == 'set':
                statement.stack_action = parse_set(
                    statement,
                    value,
                )
                continue

        raise ParsingError(
            'Unexpected statement: %s' % key,
            syntax,
            key.lc,
        )

    return statement

def raise_multiple_match(syntax, location):
    raise ParsingError(
        'Multiple match statements.',
        syntax,
        location,
    )

def raise_multiple_scope(syntax, location):
    raise ParsingError(
        'A match must not contain both “captures” and “scope” statements.',
        syntax,
        location,
    )
