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

from collections import OrderedDict
from json import dumps as json_dumps


def dict_to_plist_dict(target_dict):
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


def dict_to_plist_xml(dict_value, parent = None):
    plist = dict_to_plist_dict(dict_value)
    return plist_to_xml(plist)


def plist_to_xml(value, parent = None):
    if parent == None:
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
            plist_to_xml(v, parent)
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
            plist_to_xml(item, key_value)

    return parent

def to_json_string(value):
    return json_dumps(
        value,
        indent = 2,
        separators = (',', ': '),
    )


def to_plist_string(target_object):
    xml = dict_to_plist_xml(target_object)
    xml = to_xml_string(
        xml,
        doctype = '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">',
        encoding = 'utf-8',
        pretty_print = True,
        xml_declaration = True,
    )
    xml = xml.decode('utf-8')
    return xml
