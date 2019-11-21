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

from .ast import FunctionCall
from collections import OrderedDict

def dict_to_function_calls(calls):
    result = []
    for name, args in calls.items():
        result.append(FunctionCall(name, args))
    return result

LITERAL_TYPES = (
    bool,
    complex,
    float,
    int,
    str,
)

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
