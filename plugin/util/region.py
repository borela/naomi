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

import sublime
from sublime import Region

def expand_by_scope(view, region, target_scope):
  return Region(
    expand_by_scope_left(view, region.begin(), target_scope),
    expand_by_scope_right(view, region.end(), target_scope)
  )

def expand_by_scope_left(view, offset, target_scope):
  scopes = view.scope_name(offset)
  if target_scope not in scopes:
    return offset

  while True:
    offset -= 1
    scopes = view.scope_name(offset)

    if target_scope not in scopes:
      offset += 1
      break

    if offset <= 0:
      offset = 0
      break

  return offset

def expand_by_scope_right(view, offset, target_scope):
  scopes = view.scope_name(offset)
  if target_scope not in scopes:
    return offset

  while True:
    offset += 1
    scopes = view.scope_name(offset)

    if target_scope not in scopes:
      offset -= 1
      break

    if offset >= view.size():
      break

  return offset

# Returns the position for the first non whitespace character or the region’s
# beginning if none is found.
def find_non_whitespace(view, region, stop_on_line_feed = True):
  begin = region.begin()
  end = region.end()

  # Empty region.
  if begin == end:
    return begin

  offset = begin
  while True:
    char = view.substr(offset)

    if stop_on_line_feed and char == '\n':
      break

    if not char.isspace():
      break

    offset += 1
    if offset >= end:
      return begin

  return offset

def is_offset_valid(view, offset):
  return 0 < offset < view.size()
