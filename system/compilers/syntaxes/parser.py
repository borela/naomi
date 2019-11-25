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
    resolve_syntax_entry,
)

from os.path import (
    dirname,
    isdir,
    isfile,
    join,
    realpath,
)

from .ParsingError import ParsingError
from borela.functions import load_yaml
from collections import OrderedDict

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

    resources = compilation.queued_resources

    while len(resources):
        resolve_resource(
            compilation,
            resources.pop(),
        )

    log_info('Done parsing syntax.')
    return compilation

def dict_to_function_calls(calls):
    result = []
    for name, args in calls.items():
        result.append(FunctionCall(name, args))
    return result

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
            result.append(compilation.enqueue_resource(
                statement,
                item, 
                str(item),
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

def parse_expression(value):
    # Function calls.
    if isinstance(value, (list, OrderedDict)):
        nodes = []

        # Simple function calls.
        if isinstance(value, OrderedDict):
            nodes = dict_to_function_calls(value)
        # Function calls mixed with literals.
        else:
            for item in value:
                if isinstance(item, str):
                    nodes.append(item)
                    continue

                if isinstance(item, OrderedDict):
                    nodes.extend(dict_to_function_calls(item))

        if len(nodes) > 1:
            nodes = FunctionCall('join', nodes)

        return nodes

    # Literal pattern.
    return str(value)

def parse_include(context, raw):
    compilation = context.compilation
    path = str(raw['include'])

    statement = Include(context)
    statement.path = path
    statement.resource = compilation.enqueue_resource(
        statement,
        raw, 
        path,
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

    syntax.name = raw.get('name', '')
    syntax.hidden = raw.get('hidden', '')
    syntax.scope = raw.get('scope', '')
    syntax.scope_suffix = raw.get('scope_suffix', '')
    syntax.file_extensions = raw.get('file_extensions', [])
    syntax.first_line_match = raw.get('first_line_match', '')

    parse_variables(syntax)
    parse_contexts(syntax)

    log_debug('Done parsing: %s' % syntax.package_relpath)

    return syntax

def parse_variable(syntax, name, value):
    statement = Variable()
    statement.syntax = syntax
    statement.name = name
    statement.pattern = value
    statement.pattern = parse_expression(value)
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

def resolve_resource(compilation, resource):
    syntax = resource.syntax
    home_dir = syntax.home_dir
    path = resource.path

    # Normal sublime path.
    if path.startswith('Packages/'):
        path = join(packages_dir(), '..', path)
    # Relative to the syntax file_path.
    elif path.startswith('./'):
        path = join(syntax.parent_dir, path)
    # Relative to the home dir.
    elif path.startswith('~/'):
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
    resource.resolved_path = path = '%s#%s' % (file_path, context)

    # The target context was loaded before.
    if path in compilation.resources:
        resource.resolved = compilation.resources[path].resolved
        return

    compilation.index_resource(resource)

    if file_path not in compilation.syntaxes:
        parse_syntax(
            compilation,
            home_dir,
            file_path,
        )

    resource.resolved = compilation.contexts.get(path, None)

    if not resource.resolved:
        raise ParsingError(
            'Context not found: %s' % package_relpath(path),
            resource.syntax,
            resource.origin.lc,
        )
