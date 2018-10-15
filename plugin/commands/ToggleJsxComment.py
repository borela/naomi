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

from Naomi.plugin.region import (
    expand_partial_comments_with_jsx,
    expand_partial_lines,
    generate_comment_punctuation_region,
    generate_jsjsx_comment_punctuation_region,
    scan_reverse,
    search_non_whitespace,
    trim_region
)
from Naomi.plugin.region.scan.predicates import (
    has_scope_predicate,
    not_predicate
)
from Naomi.plugin.view import (
    is_comment, is_whitespace,
    is_jsx_open_brace,
    is_jsx_close_brace
)
from sublime import Region
from sublime_plugin import TextCommand
import sys


def can_comment(view, region):
    region = region.begin()
    scopes = view.scope_name(region)

    while 'string' in scopes:
        region = region - 1

        if region < 0:
          return False

        if view.substr(region) == '\n':
          return False

        if 'punctuation.definition.string.begin' not in scopes:
            return True
    return True


def comment_block(view, edit, region):
    begin = region.begin()
    end = region.end()
    empty_line = False

    # Added to ensure that the cursor won’t be moved after the comment.
    if begin == end:
        view.replace(edit, Region(end), '!')
        empty_line = True

    comment_type = resolve_required_comment_type(view, begin)

    if comment_type == 'jsx':
        if empty_line:
            view.insert(edit, end + 1, ' */}')
            view.erase(edit, Region(end, end + 1))
        else:
            view.insert(edit, end, ' */}')
        view.insert(edit, begin, "{/* ")
    else:
        if empty_line:
            view.insert(edit, end + 1, ' */')
            view.erase(edit, Region(end, end + 1))
        else:
            view.insert(edit, end, ' */')
        view.insert(edit, begin, "/* ")


def comment_lines(view, edit, region):
    lines = view.lines(region)

    # Calculate the margin.
    margin = sys.maxsize
    for line in lines:
        non_whitespace_pos = search_non_whitespace(view, line)
        line_begin = line.begin()
        margin = min(
            non_whitespace_pos - line_begin,
            margin
        )

    # Analyse the type of comment that must be used for the entire block.
    first_line = lines[0]
    comment_type = resolve_required_comment_type(view, first_line.begin())

    # Comment.
    for line in reversed(lines):
        begin = line.begin() + margin
        end = max(line.end(), begin)
        empty_line = False

        # Added to ensure that the cursor won’t be moved after the comment.
        if begin == end:
            view.replace(edit, Region(end), '!')
            empty_line = True

        if comment_type == 'jsx':
            # JSX comment.
            if empty_line:
                view.insert(edit, end + 1, ' */}')
                view.erase(edit, Region(end, end + 1))
            else:
                view.insert(edit, end, ' */}')
            view.insert(edit, begin, "{/* ")
        else:
            # Normal JS comment.
            view.insert(edit, begin, "// ")
            if empty_line:
                view.erase(edit, Region(begin + 3, begin + 4))


def must_comment(view, region):
    """ Returns true if the region must be commented or not. """
    non_whitespace_pos = search_non_whitespace(
        view, region, stop_on_line_feed=False
    )

    # The entire line is blank, a comment must be inserted in the region.
    if is_whitespace(view, non_whitespace_pos):
        return True

    # If it is the JSX open brace, we just need to check the next character.
    if is_jsx_open_brace(view, non_whitespace_pos):
        non_whitespace_pos += 1

    # If the cursor is at a comment, it means that the user wants to remove it.
    return not is_comment(view, non_whitespace_pos)


def resolve_required_comment_type(view, offset):
    """
    Returns the comment type that must be applied calculed at the offset.
    """
    scopes = view.scope_name(offset)

    unfenced_scopes = ['source.jsx', 'punctuation.definition.tag.begin']
    unfenced_tag = all(x in scopes for x in unfenced_scopes) and \
        'meta.jsx-fence' not in scopes

    meta_tag_scopes = ['source.jsx', 'meta.tag']
    meta_tag = all(x in scopes for x in meta_tag_scopes)

    comment_type = 'js'
    if unfenced_tag or ('source.jsx' in scopes and not meta_tag):
        comment_type = 'jsx'

    return comment_type


def uncomment_region(view, edit, region):
    begin = region.begin()
    end = region.end() - 1

    # We will loop backwards, this means that it will hit the closing
    # punctuation for block comments first.
    i = end + 1
    while i > begin:
        i -= 1
        scopes = view.scope_name(i)

        # Not a punctuation, ignore it.
        if 'punctuation.definition.comment' not in scopes:
            continue

        # Found the second forward slash for the “// ” comment.
        if 'comment.line' in scopes:
            punctuation_region = generate_comment_punctuation_region(view, i)
            view.erase(edit, punctuation_region)
            i = punctuation_region.begin()
            continue

        # We found the beginning of the block comment first, this means that
        # there’s no end to it and we can easily remove it. It can be “/* ”,
        # “/** ”, “{/* ” or “{/** ”.
        if 'punctuation.definition.comment.begin' in scopes:
            punctuation_region = generate_jsjsx_comment_punctuation_region(
                view, i
            )

            view.erase(edit, punctuation_region)
            i = punctuation_region.begin()
            continue

        # We are looping backwards, so it is expected to find the closing
        # punctuation first which can be “ */” or “ */}”.
        possible_jsx_comment = False
        if i < view.size() and is_jsx_close_brace(view, i + 1):
            possible_jsx_comment = True

        closing_punctuation_region = generate_comment_punctuation_region(
            view, i
        )

        # Move the cursor 1 character after the beginning punctuation.
        i = scan_reverse(view, i, not_predicate(has_scope_predicate(
            'punctuation.definition.comment.begin'
        )))

        open_punctuation_region = generate_comment_punctuation_region(
            view, i - 1
        )

        # Correct the regions to include the JSX braces if necessary.
        if possible_jsx_comment:
            if is_jsx_open_brace(view, open_punctuation_region.begin() - 1):
                open_punctuation_region = Region(
                    open_punctuation_region.begin() - 1,
                    open_punctuation_region.end()
                )
                closing_punctuation_region = Region(
                    closing_punctuation_region.begin(),
                    closing_punctuation_region.end() + 1
                )

        view.erase(edit, closing_punctuation_region)
        view.erase(edit, open_punctuation_region)

        # Move the cursor to the beginning of the block to “consume” it.
        i = open_punctuation_region.begin()


class NaomiToggleJsxCommentCommand(TextCommand):
    """ Actual command to toggle the comment lines and blocks. """
    def __init__(self, view):
        self.view = view

    def run(self, edit, block):
        view = self.view

        # Expand regions.
        expanded_regions = []
        for region in self.view.sel():
            region = expand_partial_comments_with_jsx(view, region)

            if block:
                region = trim_region(view, region)
            else:
                region = expand_partial_lines(view, region)
                region = expand_partial_comments_with_jsx(view, region)

            expanded_regions.append(region)

        # Consolidate regions.
        consolidated_regions = []
        previous_region = None

        for region in expanded_regions:
            if previous_region is None:
                previous_region = region
                continue

            if previous_region.intersects(region):
                previous_region.cover(region)
                continue

            consolidated_regions.append(previous_region)
            previous_region = region

        consolidated_regions.append(previous_region)

        # Toggle comments.
        for region in reversed(consolidated_regions):
            if not must_comment(view, region):
                uncomment_region(view, edit, region)
                continue

            if not can_comment(view, region):
                continue

            if block:
                comment_block(view, edit, region)
            else:
                comment_lines(view, edit, region)
