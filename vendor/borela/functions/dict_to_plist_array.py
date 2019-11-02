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

def dict_to_plist_array(target_dict):
    """
    Prepare a common dictionary into a structure that represents a plist and is
    simpler to convert to a XML tree:

    {'foo': true}
    {'bar': 'baz'}

    becomes:

    [{'key': 'foo', 'bool': true}]
    [{'key': 'bar', 'string': 'baz'}]

    The result is an array of the key value pairs.
    """
    plist = []
    for key, value in target_dict.items():
        if isinstance(value, bool):
            plist.append({
                'key': key,
                'bool': value,
            })
        elif isinstance(value, int):
            plist.append({
                'key': key,
                'integer': value,
            })
        elif isinstance(value, str):
            plist.append({
                'key': key,
                'string': value,
            })
        elif isinstance(value, dict):
            value = dict_to_plist_array(value)
            plist.append({
                'key': key,
                'dict': value,
            })
        else:
            raise ValueError('Unexpected type “%s”.' % type(value))
    return plist
