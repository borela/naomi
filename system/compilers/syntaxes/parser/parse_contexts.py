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

from .parse_context import parse_context


def parse_contexts(syntax):
    contexts = syntax.raw.get('contexts', {})

    for name, statements in contexts.items():
        syntax.index_context(parse_context(
            syntax,
            name,
            statements,
        ))
