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

from .ast import Include
from .resolve_resource import resolve_resource

def parse_include(context, raw):
    statement = Include(context)
    statement.path = raw['include']
    statement.resource = resolve_resource(
        context.syntax,
        statement,
        statement.path,
    )
    return statement
