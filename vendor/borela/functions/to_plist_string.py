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
)

from ..Stack import Stack
from .to_xml_string import to_xml_string
from collections import OrderedDict

# Prepare a common dictionary into a structure that represents a plist and is
# simpler to convert to a XML tree:
#
#     {
#       'foo': true,
#       'bar': 'baz'
#     }
#
# becomes:
#
#     [
#         ('key', 'foo'),
#         ('bool', 'true'),
#         ('key', 'bar'),
#         ('string', 'baz'),
#     }]
#
# The result is an array of the key value pairs.
def dict_to_plist_array(target_dict):
    if not isinstance(target_dict, OrderedDict):
        raise ValueError('Dictionary must be an OrderedDict.')

    plist = []

    # Queue containing a tupple: plist index, key, dictionary.
    dict_queue = Stack()
    dict_queue.push((0, None, target_dict))

    i = -1
    while len(dict_queue):
        temp_list = []
        j, dict_key, target_dict = dict_queue.pop()

        for key, value in target_dict.items():
            i += 1

            # Defer dictionaries to the next “while” loop.
            if isinstance(value, dict):
                dict_queue.push((i, key, value))
                continue

            # Simple key value pairs.
            if isinstance(value, bool):
                temp_list.append(('key', key))
                temp_list.append(('bool', value))
            elif isinstance(value, int):
                temp_list.append(('key', key))
                temp_list.append(('integer', value))
            elif isinstance(value, str):
                temp_list.append(('key', key))
                temp_list.append(('string', value))
            else:
                raise ValueError('Unexpected type “%s”.' % type(value))

        if dict_key:
            temp_list = [
                ('key', dict_key),
                ('dict', temp_list),
            ]

        plist[i:i] = temp_list

    return plist

# Convert a plist stack to a XML tree that represents the plist.
def plist_array_to_xml(nodes):
    plist = Element('plist')
    plist.attrib['version'] = '1.0'

    nodes_queue = Stack()
    nodes_queue.push((
        SubElement(plist, 'dict'),
        nodes
    ))

    while len(nodes_queue):
        parent, nodes = nodes_queue.pop()

        for node in nodes:
            tag, value = node
            node = SubElement(parent, tag)

            if tag == 'dict':
                nodes_queue.push((node, value))
                continue

            # Simple key value pairs.
            node.text = str(value)

    return plist

# Convert a simple dictionary into a XML plist string.
def to_plist_string(target_dict):
    # Prepare the dictionary.
    plist_array = dict_to_plist_array(target_dict)
    # Convert to a XML tree.
    xml = plist_array_to_xml(plist_array)
    # Finally convert to string.
    return to_xml_string(
        xml,
        indent=True,
    )
