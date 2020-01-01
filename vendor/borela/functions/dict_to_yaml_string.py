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

from collections import OrderedDict
from io import StringIO
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import walk_tree

def dict_to_yaml_string(target_dict):
    string_buffer = StringIO()

    walk_tree(target_dict)

    yaml = YAML()
    yaml.version = (1, 2)
    yaml.indent(mapping=2, sequence=4, offset=2)

    yaml.Representer.add_representer(
        OrderedDict,
        yaml.Representer.represent_dict,
    )

    yaml.dump(target_dict, string_buffer)
    return string_buffer.getvalue()
