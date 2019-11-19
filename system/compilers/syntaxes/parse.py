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
    log_error,
    log_info,
    resolve_syntax_entry,
)

from .ast import Compilation
from .parse_syntax import parse_syntax
from .resolve_resource import resolve_resource

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

    syntax = parse_syntax(
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

    return compilation
