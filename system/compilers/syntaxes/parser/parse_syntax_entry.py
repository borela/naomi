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

from Naomi.system import (
    log_debug,
    log_error,
    log_info,
    package_relpath,
    resolve_syntax_entry,
)

from .ast import Syntax
from .parse_variable_declaration import * # noqa
from .parse_context_declaration import * # noqa
from borela.functions import load_yaml
from os.path import dirname


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
