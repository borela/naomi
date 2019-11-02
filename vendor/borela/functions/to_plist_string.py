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

from .dict_to_plist_array import dict_to_plist_array
from .plist_array_to_xml import plist_array_to_xml
from .to_xml_string import to_xml_string


def to_plist_string(target_dict):
    """
    Convert a simple dictionary into a XML plist string.
    """
    # Prepare the dictionary.
    plist_array = dict_to_plist_array(target_dict)
    # Convert to a XML tree.
    xml = plist_array_to_xml(plist_array)
    # Convert to a binary string.
    xml = to_xml_string(
        xml,
        indent=True,
    )
    # Convert back to a normal string.
    xml = xml.decode('utf-8')
    return xml
