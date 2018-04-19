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

from Naomi.plugin.region.expand import expand_by_scope
from Naomi.plugin.view import (
    is_jsx_open_brace,
    is_jsx_close_brace,
    search_scope
)
from sublime import Region


ANY_COMMENT_SCOPE = 'punctuation\.definition\.comment\.\w+'
COMMENT_SCOPE = 'punctuation.definition.comment'
COMMENT_BEGIN_SCOPE = 'punctuation.definition.comment.begin'
COMMENT_END_SCOPE = 'punctuation.definition.comment.end'


def generate_comment_punctuation_region(
    view, offset, include_one_whitespace=True
):
    result = generate_region_for_scope(view, offset, ANY_COMMENT_SCOPE)
    begin = result.begin()
    end = result.end()
    scopes = view.scope_name(begin)

    if COMMENT_BEGIN_SCOPE in scopes:
        next_char = view.substr(end)
        if next_char.isspace() and next_char != '\n':
            if COMMENT_SCOPE not in view.scope_name(end + 1):
                end += 1

    if COMMENT_END_SCOPE in scopes:
        previous_char = view.substr(begin - 1)
        if previous_char.isspace() and previous_char != '\n':
            if COMMENT_SCOPE not in view.scope_name(begin - 2):
                begin -= 1

    return Region(begin, end)


def generate_jsjsx_comment_punctuation_region(
    view, offset, include_one_whitespace=True
):
    result = generate_comment_punctuation_region(
        view, offset, include_one_whitespace
    )

    begin = result.begin()
    end = result.end()

    if is_jsx_open_brace(view, begin - 1):
        begin -= 1
    if is_jsx_close_brace(view, end + 1):
        end += 1

    return Region(begin, end)


def generate_region_for_scope(view, offset, scope_pattern):
    scope = search_scope(view, offset, scope_pattern)
    if scope is None:
        return None
    return expand_by_scope(view, Region(offset), scope)
