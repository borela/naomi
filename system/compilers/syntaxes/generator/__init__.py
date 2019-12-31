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

from ..ast import (
    ClearScopes,
    Compilation,
    Context,
    ContextRequest,
    Embed,
    FunctionCall,
    Include,
    Match,
    Pop,
    Push,
    Set,
    SetMetaContentScope,
    SetMetaScope,
    Syntax,
    Variable,
)

from .GenerationError import GenerationError
from borela.functions import indent_string
from collections import OrderedDict
from ruamel.yaml.comments import CommentedMap
from Naomi.system.headers import syntax as syntax_header

def generate_action_sequence(sequence):
    result = []

    for action in sequence:
        if isinstance(action, str):
            result.append(action)
            continue

        if isinstance(action, Context):
            result.append(generate_context(action))
            continue

        raise GenerationError(
            'Unexpected action sequence type: %s' % type(action)
        )

    return result

def generate_context(context):
    result = []

    for statement in context.statements:
        # clear_scopes
        if isinstance(statement, ClearScopes):
            result.append({'clear_scopes': statement.value})
            continue

        # meta_scope
        if isinstance(statement, SetMetaScope):
            result.append({'meta_scope': statement.scope})
            continue

        # meta_content_scope
        if isinstance(statement, SetMetaContentScope):
            result.append({'meta_content_scope': statement.scope})
            continue

        # include
        if isinstance(statement, Include):
            result.append({'include': statement.context_request})
            continue

        # match
        if isinstance(statement, Match):
            match = OrderedDict()
            match['match'] = statement.pattern

            if statement.scope:
                match['scope'] = statement.scope

            if statement.captures:
                match['captures'] = OrderedDict()
                for i, scope in statement.captures.items():
                    match['captures'][i] = scope

            if statement.action:
                action = statement.action

                if isinstance(action, Pop):
                    match['pop'] = action.value

                if isinstance(action, Push):
                    match['push'] = generate_action_sequence(action.sequence)

                if isinstance(action, Set):
                    match['set'] = generate_action_sequence(action.sequence)

            result.append(match)

    return result

def generate_dict(compilation):
    entry = compilation.entry
    result = CommentedMap()
    result.yaml_set_start_comment('%s\n%s' % (
        syntax_header(entry.path),
        indent_string(
            'Statistics:\n%s\n ' % indent_string(
                text=str(compilation.statistics),
                amount=2,
            )
        ),
    ))

    result['name'] = entry.name

    if entry.scope:
        result['scope'] = entry.scope

    if entry.file_extensions:
        result['file_extensions'] = entry.file_extensions

    if entry.first_line_match:
        result['first_line_match'] = entry.first_line_match

    result['variables'] = OrderedDict()
    result['contexts'] = OrderedDict()

    for variable in compilation.variables.values():
        result['variables'][variable.short_name] = variable.pattern

    for context in compilation.contexts.values():
        result['contexts'][context.short_name] = generate_context(context)

    return result
