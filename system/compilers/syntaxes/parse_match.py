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
    Embed,
    FunctionCall,
    Match,
    Pop,
    Push,
    Set,
)

from .parse_expression import parse_expression
from .ParsingError import ParsingError

def check_embed_exists(key, statement, raw):
  if 'embed' not in raw:
      raise ParsingError(
          '“%s” without embed.' % key,
          statement.syntax,
          key.lc,
      )

  if not statement.action:
      raise ParsingError(
          '“%s” must be after embed.' % key,
          statement.syntax,
          key.lc,
      )

def parse_context_sequence(value):
    return []

def parse_match(context, raw):
    statement = Match(context)
    syntax = statement.syntax

    match_parsed = False
    scope_parsed = False

    for key, value in raw.items():
        if key == 'escape':
            check_embed_exists(key, statement, raw)
            statement.action.escape = value
            continue

        if key == 'embed_scope':
            check_embed_exists(key, statement, raw)
            statement.action.embed_scope = value
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
            if scope_parsed:
                raise_multiple_scope(syntax, key.lc)
            statement.scope = value
            scope_parsed = True
            continue

        if key == 'captures':
            if scope_parsed:
                raise_multiple_scope(syntax, key.lc)
            statement.captures = value
            scope_parsed = True
            continue

        if key == 'with_prototype':
            statement.with_prototype = value
            continue

        if key in ['embed', 'pop', 'push', 'set']:
            if statement.action:
                raise ParsingError(
                    'Multiple stack actions.',
                    syntax,
                    key.lc,
                )

            if key == 'embed':
                statement.action = Embed(statement)
                statement.action.embed_context = value
                continue

            if key == 'pop':
                statement.action = Pop(statement)
                statement.action.value = str(value)
                continue

            if key == 'push':
                statement.action = Push(statement)
                statement.sequence = parse_context_sequence(value)
                continue

            if key == 'set':
                statement.action = Set(statement)
                statement.sequence = parse_context_sequence(value)
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
