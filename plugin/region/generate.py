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

from ..view import *
from sublime import Region

def generate_comment_punctuation_region(view, offset, include_one_whitespace = True):
  result = generate_region_for_scope(view, offset, 'punctuation\.definition\.comment\.\w+')
  next_char = view.substr(result.end())
  if next_char.isspace() and next_char != '\n':
    return Region(result.begin(), result.end() + 1)
  return result

def generate_region_for_scope(view, offset, scope_pattern):
  scope = search_scope(view, offset, scope_pattern)
  if scope is None:
    return None
  return expand_by_scope(view, Region(offset), scope)
