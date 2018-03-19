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

import re

from sublime import Region
from .scan import *
from ..view import *

def expand(view, region, predicate):
  begin = scan_reverse(view, region.begin(), predicate)
  end = scan(view, region.end(), predicate)
  return Region(begin, end)

def expand_by_scope(view, region, scope):
  def __predicate(view, offset):
    scopes = view.scope_name(offset)
    return scope in scopes
  return expand(view, region, __predicate)

def expand_partial_comments(view, region):
  def __is_comment_begin(view, offset):
    scopes = view.scope_name(offset)
    return 'punctuation.definition.comment.begin' in scopes

  def __is_comment_end(view, offset):
    scopes = view.scope_name(offset)
    return 'punctuation.definition.comment.end' in scopes

  begin = region.begin()
  end = region.end()

  # When the cursor is at the punctuation, we need to move it to the body.
  begin_scope = search_scope(view, begin, 'punctuation\.definition\.comment\.\w+')

  if begin_scope is not None:
    begin = scan_reverse(view, begin, has_scope_predicate(begin_scope))
    if begin_scope == 'punctuation.definition.comment.end':
      begin -= 1

  if end == begin and __is_comment_begin(view, end):
    end = scan(view, end, __is_comment_begin) + 1
  else:
    end_scope = search_scope(view, end - 1, 'punctuation\.definition\.comment\.\w+')
    if end_scope is not None:
      end = scan(view, end, has_scope_predicate(end_scope))

  # Expand.
  begin = scan_reverse(view, begin, all_predicate([
    is_comment_predicate(),
    not_predicate(__is_comment_end)
  ]))

  end = scan(view, end, all_predicate([
    is_comment_predicate(),
    not_predicate(__is_comment_begin)
  ]))

  return Region(begin, end)

def expand_partial_comments_with_jsx(view, region):
  begin = region.begin()
  end = region.end()

  # If cursor is at a JSX interpolation brace, correct it if there’s a comment
  # inside.
  if is_jsx_open_brace(view, begin): begin += 1
  if is_jsx_open_brace(view, end): end += 1

  if is_jsx_close_brace(view, begin): begin -= 1
  if is_jsx_close_brace(view, end): end -= 1

  return expand_partial_comments(view, Region(begin, end))

def expand_partial_lines(view, region):
  def __predicate(view, offset):
    char = view.substr(offset)
    return char != '\n'

  begin = scan_reverse(view, region.begin(), __predicate)
  end = scan(view, region.end(), __predicate)

  return Region(begin, end)
