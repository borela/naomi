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

from .statements import (
    ContextDeclaration,
    VariableDeclaration,
)

from Naomi.system import (
    EVENT_BUS,
    log_debug,
    log_error,
    log_info,
    package_relpath,
    resolve_syntax_entry,
    STATE_STORE,
)

from Naomi.system.events import (
    building_syntaxes,
    finished_building_syntaxes,
)

from .statements import (
    ClearScopes,
    Include,
    Match,
    Pop,
    Push,
    Set,
    SetMetaContentScope,
    SetMetaScope,
    WithPrototype,
)

from borela.functions import (
    load_yaml,
    make_regex_to_match_words,
)

from .Syntax import Syntax
from os.path import dirname


def compile_syntaxes():
    EVENT_BUS.emit(building_syntaxes())

    for settings in STATE_STORE['settings']['syntaxes']:
        syntax = parse_syntax_entry(settings)
        save_to_file(syntax)
        # TODO: Save to a file.

    EVENT_BUS.emit(finished_building_syntaxes())


def make_contextual_statement(statement, syntax, context, raw):
    statement.syntax = syntax
    statement.context = context
    statement.raw = raw
    return statement


def parse_clear_scopes_statement(syntax, context, raw):
    statement = make_contextual_statement(
        ClearScopes(),
        syntax,
        context,
        raw,
    )
    statement.value = raw['clear_scopes']
    return statement


def parse_context_declaration(syntax, name, raw):
    context = ContextDeclaration()
    context.syntax = syntax
    context.raw = raw
    context.name = name

    for statement in raw:
        if any(key in ['match', 'match_words'] for key in statement):
            context.statements.append(parse_match_statement(
                syntax,
                context,
                statement,
            ))
            continue

        if 'include' in statement:
            context.statements.append(parse_include_statement(
                syntax,
                context,
                statement,
            ))
            continue

        if 'meta_scope' in statement:
            context.statements.append(parse_meta_scope_statement(
                syntax,
                context,
                statement,
            ))
            continue

        if 'meta_content_scope' in statement:
            context.statements.append(parse_meta_content_scope_statement(
                syntax,
                context,
                statement,
            ))
            continue

        if 'clear_scopes' in statement:
            context.statements.append(parse_clear_scopes_statement(
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


def parse_include_statement(syntax, context, raw):
    statement = make_contextual_statement(
        Include(),
        syntax,
        context,
        raw,
    )
    # TODO.
    statement.value = raw['include']
    return statement


def parse_match_statement(syntax, context, raw):
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
            statement.with_prototype = parse_with_prototype_statement(
                syntax,
                context,
                value,
            )
            continue

        if key in ['push', 'set', 'pop']:
            if statement.stack_control:
                raise SyntaxError(
                    'Multiple stack control statements. (%i, %i)' %
                    value.lc.line,
                    value.lc.col,
                )

            if key == 'push':
                statement.stack_control = parse_push_statement(
                    syntax,
                    context,
                    value,
                )
                continue

            if key == 'set':
                statement.stack_control = parse_set_statement(
                    syntax,
                    context,
                    value,
                )
                continue

            if key == 'pop':
                statement.stack_control = parse_pop_statement(
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


def parse_meta_content_scope_statement(syntax, context, raw):
    statement = make_contextual_statement(
        SetMetaContentScope(),
        syntax,
        context,
        raw,
    )
    statement.value = raw['meta_content_scope']
    return statement


def parse_meta_scope_statement(syntax, context, raw):
    statement = make_contextual_statement(
        SetMetaScope(),
        syntax,
        context,
        raw,
    )
    # TODO.
    statement.value = raw['meta_scope']
    return statement


def parse_pop_statement(syntax, context, raw):
    statement = make_contextual_statement(
        Pop(),
        syntax,
        context,
        raw,
    )
    # TODO.
    return statement


def parse_push_statement(syntax, context, raw):
    statement = make_contextual_statement(
        Push(),
        syntax,
        context,
        raw,
    )
    # TODO.
    return statement


def parse_set_statement(syntax, context, raw):
    statement = make_contextual_statement(
        Set(),
        syntax,
        context,
        raw,
    )
    # TODO.
    return statement


def parse_syntax_entry(settings):
    entry = settings.get('entry', None)

    if not isinstance(entry, str) or not entry:
        log_error('Configured syntax has no entry.')
        return

    names = settings.get('names', None)

    if not names:
        log_info('Compiling syntax: %s []' % (entry))
    else:
        log_info('Compiling syntax: %s %s' % (entry, names))

    entry, src_dir, build_dir = resolve_syntax_entry(entry)

    syntax = Syntax()
    syntax.settings = settings

    syntax.home_dir = src_dir
    syntax.build_dir = build_dir

    syntax.path = entry
    syntax.parent_dir = dirname(entry)
    syntax.package_relpath = package_relpath(entry)

    log_debug('Loading syntax file: %s' % syntax.package_relpath)

    raw = load_yaml(syntax.path)
    syntax.raw = raw

    log_debug('Done loading syntax file: %s' % syntax.package_relpath)

    syntax.name = raw.get('name', '')
    syntax.hidden = raw.get('hidden', '')
    syntax.scope = raw.get('scope', '')
    syntax.scope_suffix = raw.get('scope_suffix', '')
    syntax.file_extensions = raw.get('file_extensions', [])
    syntax.first_line_match = raw.get('first_line_match', '')

    for name, raw in syntax.raw.get('variables', {}).items():
        syntax.variables.append(parse_variable_declaration(syntax, name, raw))

    for name, raw in syntax.raw.get('contexts', {}).items():
        syntax.contexts.append(parse_context_declaration(syntax, name, raw))

    return syntax


def parse_variable_declaration(syntax, name, raw):
    statement = VariableDeclaration()
    statement.syntax = syntax
    statement.raw = raw
    statement.name = name
    statement.pattern = raw
    return statement


def parse_with_prototype_statement(syntax, context, raw):
    statement = make_contextual_statement(
        WithPrototype(),
        syntax,
        context,
        raw,
    )
    # TODO.
    return statement


def save_to_file(syntax):
    pass
