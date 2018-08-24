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

from json import dumps as json_dumps
from lxml.etree import Element, SubElement, tostring as to_xml_string


def dict_to_plist_dict(target_dict):
    plist = []
    for key, value in target_dict.items():
        if isinstance(value, bool):
            plist.append({
              'key': key,
              'bool': value,
            })
            continue

        if isinstance(value, str):
            plist.append({
              'key': key,
              'string': value,
            })
            continue

        if isinstance(value, dict):
            value = dict_to_plist_dict(value)
            plist.append({
              'key': key,
              'dict': value,
            })
            continue

        raise ValueError('Unexpected type “%s”.' % type(value))
    return plist


def dict_to_plist_xml(value):
    plist = dict_to_plist_dict(value)
    plist = dict_to_xml(plist, 'plist')
    return plist


def dict_to_xml(value, tag):
    if isinstance(tag, str):
        tag = Element(tag)

    if isinstance(value, dict):
        for k, v in value.items():
            child = SubElement(tag, k)
            dict_to_xml(v, child)
        return tag

    elif isinstance(value, tuple) or isinstance(value, list):
        for v in value:
            dict_to_xml(v, tag)

    if isinstance(value, str):
        tag.text = value

    return tag


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
