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
)

from .ast import Resource
from Naomi.system import packages_dir

def resolve_resource(syntax, statement, path):
    # Normal sublime path.
    if path.startswith('Packages/'):
        resolved_path = join(packages_dir(), '..', path)
    # Relative to the syntax file.
    elif path.startswith('./'):
        resolved_path = join(dirname(syntax.path), path)
    # Relative to the home dir.
    elif path.startswith('~/'):
        resolved_path = join(syntax.home_dir, path)
    # Context in the syntax file.
    else:
        resolved_path = syntax.path + '#' + path

    resource = Resource(
        statement,
        statement.path,
    )

    resource.resolved_path = path
    syntax.compilation.index_resource(resource)
