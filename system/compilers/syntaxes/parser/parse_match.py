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

from .ast import Match
from .make_contextual_statement import make_contextual_statement
from .parse_push import * # noqa
from .parse_pop import * # noqa
from .parse_set import * # noqa
from borela.functions import make_regex_to_match_words


def parse_match(syntax, context, raw):
    statement = make_contextual_statement(
        Match(),
        syntax,
        context,
        raw,
    )

    for key, value in raw.items():
        if key == 'match':
            statement.pattern = value
            continue

        if key == 'match_words':
            statement.pattern = make_regex_to_match_words(value)
            print(statement.pattern)
            continue

        if key == 'scope':
            statement.scope = value
            continue

        if key == 'captures':
            statement.captures = value
            continue

        if key == 'with_prototype':
            statement.with_prototype = value
            continue

        if key in ['push', 'set', 'pop']:
            if statement.stack_control:
                raise SyntaxError(
                    'Multiple stack control statements. (%i, %i)' %
                    value.lc.line,
                    value.lc.col,
                )

            if key == 'push':
                statement.stack_control = parse_push(
                    syntax,
                    context,
                    value,
                )
                continue

            if key == 'set':
                statement.stack_control = parse_set(
                    syntax,
                    context,
                    value,
                )
                continue

            if key == 'pop':
                statement.stack_control = parse_pop(
                    syntax,
                    context,
                    value,
                )
                continue

        raise SyntaxError('Unexpected statement: %s (%i, %i)' % (
            key,
            value.lc.line,
            value.lc.col,
        ))

    return statement
