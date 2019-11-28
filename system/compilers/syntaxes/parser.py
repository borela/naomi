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
    ClearScopes,
    Compilation,
    Context,
    Embed,
    FunctionCall,
    Include,
    Match,
    SetMetaContentScope,
    SetMetaScope,
    Pop,
    Push,
    Set,
    Syntax,
    Variable,
)

from Naomi.system import (
    log_debug,
    log_error,
    log_info,
    packages_dir,
    package_relpath,
)

from os.path import (
    isdir,
    isfile,
    join,
    realpath,
)

from .ParsingError import ParsingError
from borela.functions import load_yaml
from collections import OrderedDict
from Naomi.system.state_store import STATE_STORE

import re

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

def dict_to_function_calls(calls):
    result = []
    for name, args in calls.items():
        result.append(FunctionCall(name, args))
    return result

def parse(settings):
    entry = settings.get('entry', None)

    if not isinstance(entry, str) or not entry:
        log_error('Configured syntax has no entry.')
        return

    names = settings.get('names', None)

    if not names:
        log_info('Compiling syntax: %s []' % (entry))
    else:
        log_info('Compiling syntax: %s %s' % (entry, names))

    entry_path, home_dir, build_dir = resolve_syntax_entry(entry)

    compilation = Compilation(
        settings,
        build_dir,
    )

    parse_syntax(
        compilation,
        home_dir,
        entry_path,
    )

    # Link context resquests.
    requests = compilation.context_requests
    while len(requests):
        resolve_context_request(
            compilation,
            requests.pop(),
        )

    # Link variable resquests.
    requests = compilation.variable_requests
    while len(requests):
        resolve_variable_request(
            compilation,
            requests.pop(),
        )

    log_info('Done parsing syntax.')
    return compilation

def parse_clear_scopes(context, raw):
    statement = ClearScopes(context)
    statement.value = raw['clear_scopes']
    return statement

def parse_context(syntax, name, raw):
    context = Context(syntax)
    context.name = name
    return parse_context_statements(context, raw)

def parse_context_sequence(statement, raw):
    syntax = statement.syntax
    compilation = statement.compilation

    # Context sequences are used in Set and Push actions, they can be a list
    # that contains references and inline contexts:
    #
    #     [
    #         string,                          # Reference.
    #         [OrderedDict, OrderedDict, ...]  # Context.
    #         ...
    #     ]
    #
    # Or just a single reference/context.
    if isinstance(raw, list):
        # At this point the list might be in the format we want or just be a
        # single inline context.
        if any(isinstance(item, OrderedDict) for item in raw):
            raw = [raw]
    else:
        # Anything else means that we are referencing a single context.
        raw = [raw]

    # Mixed, list containing references to or inline contexts.
    result = []

    for item in raw:
        # Inline context.
        if isinstance(item, list):
            result.append(parse_context_statements(
                Context(syntax),
                item,
            ))
        # Context reference.
        else:
            result.append(compilation.enqueue_context_request(
                statement=statement,
                origin=item,
                path=str(item),
            ))

    return result

def parse_context_statements(context, raw):
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

        MATCH_STATEMENTS = ['match', 'match_word', 'match_words']
        if any(key in MATCH_STATEMENTS for key in statement):
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
            statement.syntax,
            statement.lc,
        )

    return context

def parse_contexts(syntax):
    contexts = syntax.raw.get('contexts', {})

    for name, statements in contexts.items():
        syntax.index_context(parse_context(
            syntax,
            name,
            statements,
        ))

VARIABLE_PATTERN = re.compile(r'{{(\w[\w-]*?)}}')

def parse_expression(syntax, origin, pattern):
    nodes = []
    compilation = syntax.compilation

    # Function calls.
    if isinstance(pattern, (list, OrderedDict)):
        # Simple function calls.
        if isinstance(pattern, OrderedDict):
            nodes = dict_to_function_calls(pattern)
        # Function calls mixed with literals.
        else:
            for item in pattern:
                # Function call.
                if isinstance(item, OrderedDict):
                    nodes.extend(dict_to_function_calls(item))
                    continue
                # Literal.
                nodes.append(str(item))

    # Pattern.
    for item in re.split(r'({{\w[\w-]*?}})', str(pattern)):
        item = item.strip()
        if not item:
            continue

        found = VARIABLE_PATTERN.findall(item)

        # Literal.
        if not found:
            nodes.append(item)
            continue

        # Variable.
        name = '%s#%s' % (
            syntax.path,
            found[0],
        )

        variable = compilation.enqueue_variable_request(
            syntax,
            origin,
            name,
        )

        nodes.append(variable)

    if len(nodes) > 1:
        nodes = FunctionCall('join', nodes)

    return nodes

def parse_include(context, raw):
    compilation = context.compilation
    path = str(raw['include'])

    statement = Include(context)
    statement.path = path
    statement.context_request = compilation.enqueue_context_request(
        statement=statement,
        origin=raw,
        path=path,
    )

    return statement

def parse_match(context, raw):
    statement = Match(context)
    syntax = context.syntax

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
            statement.pattern = parse_expression(
                syntax=syntax,
                origin=key,
                pattern=value,
            )
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
                statement.action.sequence = parse_context_sequence(
                    statement,
                    value,
                )
                continue

            if key == 'set':
                statement.action = Set(statement)
                statement.action.sequence = parse_context_sequence(
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

def parse_meta_scope(context, raw):
    statement = SetMetaScope(context)
    statement.scope = raw['meta_scope']
    return statement

def parse_meta_content_scope(context, raw):
    statement = SetMetaContentScope(context)
    statement.scope = raw['meta_content_scope']
    return statement

def parse_syntax(compilation, home_dir, path):
    syntax = Syntax(
        compilation,
        home_dir,
        path,
    )

    compilation.index_syntax(syntax)

    raw = load_yaml(syntax.path)
    syntax.raw = raw

    syntax.name = raw.get('name', None)
    syntax.hidden = raw.get('hidden', False)
    syntax.scope = raw.get('scope', None)
    syntax.scope_prefix = raw.get('scope_prefix', None)
    syntax.scope_suffix = raw.get('scope_suffix', None)
    syntax.file_extensions = raw.get('file_extensions', [])
    syntax.first_line_match = raw.get('first_line_match', None)

    parse_variables(syntax)
    parse_contexts(syntax)

    log_debug('Done parsing: %s' % syntax.package_relpath)

    return syntax

def parse_variable(syntax, name, value):
    statement = Variable()
    statement.syntax = syntax
    statement.name = name
    statement.pattern = parse_expression(
        syntax=syntax,
        origin=name,
        pattern=value,
    )
    return statement

def parse_variables(syntax):
    variables = syntax.raw.get('variables', {})

    for name, value in variables.items():
        syntax.index_variable(parse_variable(
            syntax,
            name,
            value,
        ))

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

def resolve_context_request(compilation, request):
    syntax = request.syntax
    home_dir = syntax.home_dir
    path = request.path

    if path.startswith('Packages/'):
        # Normal sublime path.
        path = join(packages_dir(), '..', path)
    elif path.startswith('./'):
        # Relative to the syntax file_path.
        path = join(syntax.parent_dir, path)
    elif path.startswith('~/'):
        # Relative to the home dir.
        path = path.replace('~/', '')
        path = join(home_dir, path)
    else:
        # Context.
        path = '%s#%s' % (syntax.path, path)

    if '#' not in path:
        path += '#main'

    file_path, context = path.split('#')

    if isdir(file_path):
        file_path = join(file_path, 'index.yml')

    if not isfile(file_path) and not file_path.endswith('.yml'):
        file_path += '.yml'

    # Final file path.
    file_path = realpath(file_path)

    # Full path to the context.
    request.resolved_path = path = '%s#%s' % (file_path, context)

    # The target context was loaded before.
    if path not in compilation.contexts:
        if file_path not in compilation.syntaxes:
            parse_syntax(
                compilation,
                home_dir,
                file_path,
            )

    request.resolved = compilation.contexts.get(path, None)

    if not request.resolved:
        raise ParsingError(
            'Context not found: %s' % package_relpath(path),
            request.syntax,
            request.origin.lc,
        )

def resolve_variable_request(compilation, request):
    path = request.path
    request.resolved = compilation.variables.get(path, None)

    if not request.resolved:
        raise ParsingError(
            'Variable not found: %s' % path.split('#')[1],
            request.syntax,
            request.origin.lc,
        )

# Resolve relative paths to the syntaxes src directories being managed by
# the Naomi’s system.
def resolve_syntax_entry(path):
    if isfile(path):
        return realpath(path)

    dirs = [
        (integrated['src_dir'], integrated['build_dir'])
        for integrated in STATE_STORE['integrated']['syntaxes']
    ]

    # Allow external packages to override Naomi’s syntax files.
    dirs.reverse()

    # Try to find a file with the integrated src directories.
    for src_dir, build_dir in dirs:
        resolved_path = join(src_dir, path)

        if isdir(resolved_path):
            resolved_path = join(resolved_path, 'index.yml')
            return resolved_path, src_dir, build_dir
        elif isfile(resolved_path):
            return resolved_path, src_dir, build_dir
        else:
            resolved_path += '.yml'

            if isfile(resolved_path):
                return resolved_path, src_dir, build_dir

    raise ParsingError('Syntax entry not found: %s' % path)
