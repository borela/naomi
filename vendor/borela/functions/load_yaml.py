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

from ruamel.yaml import (
    scalarstring,
    YAML,
)

from ruamel.yaml.comments import LineCol
from ruamel.yaml.constructor import RoundTripConstructor


class DoubleQuotedScalarString(scalarstring.DoubleQuotedScalarString):
    pass


class PreservedScalarString(scalarstring.PreservedScalarString):
    pass


class ScalarString(scalarstring.ScalarString):
    pass


class SingleQuotedScalarString(scalarstring.SingleQuotedScalarString):
    pass


class YamlConstructor(RoundTripConstructor):
    def construct_scalar(self, node):
        result = None

        if node.style == '|':
            result = PreservedScalarString(node.value)
        elif node.style == "'":
            result = SingleQuotedScalarString(node.value)
        elif node.style == '"':
            result = DoubleQuotedScalarString(node.value)
        else:
            result = ScalarString(node.value)

        result.lc = LineCol()
        result.lc.line = node.start_mark.line
        result.lc.col = node.start_mark.column

        return result


def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        parser = YAML()
        parser.Constructor = YamlConstructor
        return parser.load(file)
