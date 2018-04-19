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


def scan(view, offset, predicate, limit=-1):
    if not predicate(view, offset):
        return offset

    if limit < 1:
        limit = view.size() - 1

    while True:
        offset += 1
        if offset > limit:
            offset = limit
            break

        if not predicate(view, offset):
            break

    return offset


def scan_reverse(view, offset, predicate, limit=-1):
    if not predicate(view, offset):
        return offset

    if limit < 0:
        limit = 0

    while True:
        offset -= 1
        if offset < limit:
            offset = limit
            break

        if not predicate(view, offset):
            offset += 1
            break

    return offset


def search_non_whitespace(view, region, stop_on_line_feed=False):
    def __predicate(view, offset):
        char = view.substr(offset)
        if stop_on_line_feed and char == '\n':
            return False
        return char.isspace()

    begin = region.begin()
    end = region.end()

    if end < begin:
        end = begin

    return scan(view, begin, __predicate, end)


def search_non_whitespace_reverse(view, region, stop_on_line_feed=False):
    def __predicate(view, offset):
        char = view.substr(offset)
        if stop_on_line_feed and char == '\n':
            return False
        return char.isspace()

    begin = region.begin()
    end = region.end() - 1

    if end < begin:
        end = begin

    result = scan_reverse(view, end, __predicate, begin)
    if view.substr(result).isspace():
        result -= 1

    return result
