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


def has_any_scope(view, offset, target_scopes):
    scopes = view.scope_name(offset)
    return any(x in scopes for x in target_scopes)


def has_all_scopes(view, offset, target_scopes):
    scopes = view.scope_name(offset)
    return all(x in scopes for x in target_scopes)


def is_comment(view, offset):
    comment_scopes = ['comment.block', 'comment.line']
    scopes = view.scope_name(offset)
    return any(x in scopes for x in comment_scopes)


def is_comment_begin(view, offset):
    return 'punctuation.definition.comment.begin' in view.scope_name(offset)


def is_comment_end(view, offset):
    return 'punctuation.definition.comment.end' in view.scope_name(offset)


def is_jsx_open_brace(view, offset):
    open_brace_scopes = [
        'source.jsx',
        'punctuation.definition.template-expression.begin'
    ]
    scopes = view.scope_name(offset)
    return all(x in scopes for x in open_brace_scopes)


def is_jsx_close_brace(view, offset):
    close_brace_scopes = [
        'source.jsx',
        'punctuation.definition.template-expression.end'
    ]
    scopes = view.scope_name(offset)
    return all(x in scopes for x in close_brace_scopes)


def is_offset_valid(view, offset):
    return 0 <= offset <= view.size() - 1


def is_whitespace(view, offset):
    return view.substr(offset).isspace()


def not_comment(view, offset):
    return not is_comment(view, offset)


def search_scope(view, offset, pattern):
    """ Returns the string that matches the pattern. """
    scopes = view.scope_name(offset)
    matched = re.search(pattern, scopes)
    return None if matched is None else matched.group(0)
