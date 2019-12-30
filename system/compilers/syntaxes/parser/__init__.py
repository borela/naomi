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

from borela.functions import (
    load_yaml,
    trim_whitespace,
)

from .ParsingError import ParsingError
from collections import OrderedDict

import re

def check_embed_exists(key, statement, raw):
    if 'embed' not in raw:
        raise ParsingError(
            '“%s” without embed.' % key,
            statement.syntax.package_relpath,
            key.lc,
        )

    if not statement.action:
        raise ParsingError(
            '“%s” must be after embed.' % key,
            statement.syntax.package_relpath,
            key.lc,
        )

def dict_to_function_calls(calls, syntax_path):
    result = []
    for name, args in calls.items():
        function_call = FunctionCall(name, args)
        function_call.location.path = syntax_path
        function_call.location.line = name.lc.line
        function_call.location.column = name.lc.col

        result.append(function_call)
    return result

def parse(settings, integrated_syntaxes):
    entry = settings.get('entry', None)

    if not isinstance(entry, str) or not entry:
        log_error('Configured syntax has no entry.')
        return

    names = settings.get('names', None)

    if not names:
        log_info('Compiling syntax: %s []' % (entry))
    else:
        log_info('Compiling syntax: %s %s' % (entry, names))

    entry_path, home_dir, build_dir = resolve_syntax_entry(
        entry,
        integrated_syntaxes,
    )

    compilation = Compilation(
        settings,
        build_dir,
    )

    compilation.entry = parse_syntax(
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

    statement.location.path = context.syntax.path
    statement.location.line = raw.lc.line
    statement.location.column = raw.lc.col

    return statement

def parse_context(syntax, name, raw):
    context = Context(syntax, name)

    context.location.path = syntax.path
    context.location.line = raw.lc.line
    context.location.column = raw.lc.col

    parse_context_statements(context, raw)

    return context

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
            context = Context(syntax)
            context.location.path = syntax.path
            context.location.line = item.lc.line
            context.location.column = item.lc.col
            result.append(context)

            parse_context_statements(context, item)
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
            statement.syntax.package_relpath,
            statement.lc,
        )

def parse_contexts(syntax):
    contexts = syntax.raw.get('contexts', {})

    for name, statements in contexts.items():
        parse_context(
            syntax,
            name,
            statements,
        )

VARIABLE_PATTERN = re.compile(r'(?<!\\){{(\w[\w-]*?)}}')
COMMENT = re.compile(r'#.*?\n')

def parse_expression(syntax, origin, pattern):
    nodes = []
    compilation = syntax.compilation

    # Function calls.
    if isinstance(pattern, (list, OrderedDict)):
        # Simple function calls.
        if isinstance(pattern, OrderedDict):
            nodes = dict_to_function_calls(pattern, syntax.path)
        # Function calls mixed with literals.
        else:
            for item in pattern:
                # Function call.
                if isinstance(item, OrderedDict):
                    nodes.extend(dict_to_function_calls(item, syntax.path))
                    continue
                # Literal.
                nodes.append(str(item))
    else:
        # Simple string pattern.
        for item in re.split(r'({{\w[\w-]*?}})', str(pattern)):
            # Remove comments and whitespaces.
            item = COMMENT.sub('', item)
            item = trim_whitespace(item)

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
        nodes.location.path = syntax.path
        nodes.location.line = origin.lc.line
        nodes.location.column = origin.lc.col
    elif len(nodes) == 1:
        nodes = nodes[0]
    else:
        nodes = ''

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

    statement.location.path = context.syntax.path
    statement.location.line = raw.lc.line
    statement.location.column = raw.lc.col

    return statement

def parse_match(context, raw):
    syntax = context.syntax

    statement = Match(context)
    statement.location.path = syntax.path
    statement.location.line = raw.lc.line
    statement.location.column = raw.lc.col

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

        if key in ['match_word', 'match_words']:
            if match_parsed:
                raise_multiple_match(syntax, key.lc)

            if key == 'match_word':
                statement.pattern = FunctionCall('word', value)
            elif key == 'match_words':
                statement.pattern = FunctionCall('words', value)

            statement.pattern.location.path = syntax.path
            statement.pattern.location.line = key.lc.line
            statement.pattern.location.column = key.lc.col
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
                    syntax.package_relpath,
                    key.lc,
                )

            if key == 'embed':
                statement.action = Embed(statement)
                statement.action.embed_context = value
            elif key == 'pop':
                statement.action = Pop(statement)
                statement.action.value = str(value)
            elif key == 'push':
                statement.action = Push(statement)
                statement.action.sequence = parse_context_sequence(
                    statement,
                    value,
                )
            elif key == 'set':
                statement.action = Set(statement)
                statement.action.sequence = parse_context_sequence(
                    statement,
                    value,
                )

            statement.action.location.path = syntax.path
            statement.action.location.line = key.lc.line
            statement.action.location.column = key.lc.col
            continue

        raise ParsingError(
            'Unexpected statement: %s' % key,
            syntax.package_relpath,
            key.lc,
        )

    return statement

def parse_meta_scope(context, raw):
    statement = SetMetaScope(context)
    statement.scope = raw['meta_scope']

    statement.location.path = context.syntax.path
    statement.location.line = raw.lc.line
    statement.location.column = raw.lc.col

    return statement

def parse_meta_content_scope(context, raw):
    statement = SetMetaContentScope(context)
    statement.scope = raw['meta_content_scope']

    statement.location.path = context.syntax.path
    statement.location.line = raw.lc.line
    statement.location.column = raw.lc.col

    return statement

def parse_syntax(compilation, home_dir, path):
    raw = load_yaml(path)

    syntax = Syntax(
        compilation,
        home_dir,
        path,
    )

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
    statement = Variable(syntax, name)
    statement.pattern = parse_expression(
        syntax=syntax,
        origin=name,
        pattern=value,
    )

    statement.location.path = syntax.path
    statement.location.line = name.lc.line
    statement.location.column = name.lc.col

    return statement

def parse_variables(syntax):
    variables = syntax.raw.get('variables', {})

    for name, value in variables.items():
        parse_variable(
            syntax,
            name,
            value,
        )

def raise_multiple_match(syntax, location):
    raise ParsingError(
        'Multiple match statements.',
        syntax.package_relpath,
        location,
    )

def raise_multiple_scope(syntax, location):
    raise ParsingError(
        'A match must not contain both “captures” and “scope” statements.',
        syntax.package_relpath,
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
            request.syntax.package_relpath,
            request.origin.lc,
        )
    else:
        request.resolved.references.append(request)

def resolve_variable_request(compilation, request):
    path = request.path
    request.resolved = compilation.variables.get(path, None)

    if not request.resolved:
        raise ParsingError(
            'Variable not found: %s' % path.split('#')[1],
            request.syntax.package_relpath,
            request.origin.lc,
        )
    else:
        request.resolved.references.append(request)

# Resolve relative paths to the syntaxes src directories being managed by
# the Naomi’s system.
def resolve_syntax_entry(path, integrated_syntaxes):
    if isfile(path):
        return realpath(path)

    dirs = [
        (integrated['src_dir'], integrated['build_dir'])
        for integrated in integrated_syntaxes
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
