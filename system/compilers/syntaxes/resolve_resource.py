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

from os.path import (
    dirname,
    join,
    realpath,
)

from .ast import Resource
from .parse_syntax import parse_syntax
from Naomi.system import packages_dir

def resolve_resource(compilation, resource):
    syntax = resource.syntax
    home_dir = syntax.home_dir
    path = resource.path

    # Normal sublime path.
    if path.startswith('Packages/'):
        path = join(packages_dir(), '..', path)
        path = realpath(path)
    # Relative to the syntax file.
    elif path.startswith('./'):
        syntax_dir = dirname(syntax.path)
        path = join(syntax_dir, path)
        path = realpath(path)
    # Relative to the home dir.
    elif path.startswith('~/'):
        path = path.replace('~/', '')
        path = join(home_dir, path)
        path = realpath(path)
    # Context in the syntax file.
    else:
        path = syntax.path + '#' + path

    # If not context is targeted, the “main” will be used.
    if '#' not in path:
        path += '#main'

    resource.resolved_path = path

    # The target context was loaded before.
    if path in compilation.resources:
        resource.resolved = compilation.resources[path].resolved
        return

    compilation.index_resource(resource)

    # Load the target syntax and context.
    target_syntax, _ = path.split('#')

    if target_syntax not in compilation.syntaxes:
        parse_syntax(
            compilation,
            home_dir,
            target_syntax,
        )

    resource.resolved = compilation.contexts[path]
