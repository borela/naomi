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

def expand(view, region, predicate):
  return Region(
    scan_reverse(view, region.begin(), predicate),
    scan(view, region.end(), predicate)
  )

def expand_by_scope(view, region, scope):
  def __predicate(view, offset):
    scopes = view.scope_name(offset)
    return scope in scopes
  return expand(view, region, __predicate)

def expand_partial_comments(view, region):
  comment_scopes = [ 'comment.block', 'comment.line' ]

  def __not_comment_begin(view, offset):
    scopes = view.scope_name(offset)
    if any(x in scopes for x in comment_scopes):
      return 'punctuation.definition.comment.begin' not in scopes
    return False

  def __not_comment_end(view, offset):
    scopes = view.scope_name(offset)
    if any(x in scopes for x in comment_scopes):
      return 'punctuation.definition.comment.end' not in scopes
    return False

  begin = region.begin()
  end = region.end() - 1

  if end < begin:
    end = begin

  begin = scan_reverse(view, begin, __not_comment_begin) + 1
  end = scan(view, end, __not_comment_end)

  return Region(
    scan_reverse(view, begin, __not_comment_end) + 1,
    scan(view, end, __not_comment_begin)
  )

def expand_partial_lines(view, region):
  def __predicate(view, offset):
    char = view.substr(offset)
    return char == '\n'

  return Region(
    scan_reverse(view, region.begin(), __predicate) + 1,
    scan(view, region.end(), __predicate)
  )

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
  return 0 <= offset <= view.size() - 1

def scan(view, offset, predicate, limit = -1):
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
      offset -= 1
      break

  return offset

def scan_reverse(view, offset, predicate):
  if not predicate(view, offset):
    return offset

  while True:
    offset -= 1
    if offset < 0:
      offset = 0
      break

    if not predicate(view, offset):
      offset += 1
      break

  return offset
