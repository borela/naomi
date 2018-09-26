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

from lxml.etree import (
    Element,
    SubElement,
    tostring as to_xml_string,
)

from json import dumps as json_dumps


def dict_to_plist_dict(target_dict):
    """
    Prepare a common dictionary into a structure that represents a plist and is
    simpler to convert to a XML tree.
    """
    plist = []
    for key, value in target_dict.items():
        if isinstance(value, bool):
            plist.append({
              'key': key,
              'bool': value,
            })
        elif isinstance(value, str):
            plist.append({
              'key': key,
              'string': value,
            })
        elif isinstance(value, dict):
            value = dict_to_plist_dict(value)
            plist.append({
              'key': key,
              'dict': value,
            })
        else:
            raise ValueError('Unexpected type “%s”.' % type(value))
    return plist


def plist_dict_to_xml(value, parent=None):
    """
    Convert a dictionary(previously prepared “dict_to_plist_dict”) to a XML
    tree that represents the plist.
    """
    if parent is None:
        parent = Element('plist')
        parent.attrib['version'] = '1.0'
        value = {
            'key': 'plist',
            'dict': value,
        }
    else:
        key = SubElement(parent, 'key')
        key.text = value['key']

    # Sublist.
    if isinstance(value, tuple) or isinstance(value, list):
        for v in value:
            plist_dict_to_xml(v, parent)
        return parent

    # Values.
    if 'string' in value:
        key_value = SubElement(parent, 'string')
        key_value.text = value['string']
    elif 'bool' in value:
        if value['bool']:
            SubElement(parent, 'true')
        else:
            SubElement(parent, 'false')
    elif 'dict' in value:
        key_value = SubElement(parent, 'dict')
        for item in value['dict']:
            plist_dict_to_xml(item, key_value)
    else:
        raise ValueError('Unsupported value “%s”.' % value)

    return parent


def to_json_string(value):
    """
    Convert a dictionary to an indented JSON string.
    """
    return json_dumps(
        value,
        indent=2,
        separators=(',', ': '),
    )


def to_plist_string(target_dict):
    """
    Convert a simple dictionary into a XML plist string.
    """
    # Prepare the dictionary.
    plist = dict_to_plist_dict(target_dict)
    # Convert to a XML tree.
    xml = plist_dict_to_xml(plist)
    # Convert to string.
    xml = to_xml_string(
        xml,
        encoding='utf-8',
        pretty_print=True,
    )
    xml = xml.decode('utf-8')
    return xml
