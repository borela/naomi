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


def all_predicate(predicates):
    def __predicate(view, offset):
        for predicate in predicates:
            if not predicate(view, offset):
                return False
        return True
    return __predicate


def any_predicate(predicates):
    def __predicate(view, offset):
        for predicate in predicates:
            if predicate(view, offset):
                return True
        return False
    return __predicate


def has_scope_predicate(scope):
    def __predicate(view, offset):
        scopes = view.scope_name(offset)
        return scope in scopes
    return __predicate


def has_all_scopes_predicate(target_scopes):
    def __predicate(view, offset):
        scopes = view.scope_name(offset)
        return all(x in scopes for x in target_scopes)
    return __predicate


def has_any_scope_predicate(target_scopes):
    def __predicate(view, offset):
        scopes = view.scope_name(offset)
        return any(x in scopes for x in target_scopes)
    return __predicate


def is_comment_predicate():
    comment_scopes = ['comment.block', 'comment.line']
    return has_any_scope_predicate(comment_scopes)


def is_comment_begin_predicate():
    return has_scope_predicate('punctuation.definition.comment.begin')


def is_comment_end_predicate():
    return has_scope_predicate('punctuation.definition.comment.end')


def not_comment_predicate():
    return not_predicate(is_comment_predicate())


def not_predicate(predicate):
    def __predicate(view, offset):
        return not predicate(view, offset)
    return __predicate
