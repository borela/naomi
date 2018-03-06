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
import os
import sublime
import sublime_plugin

def comment_lines(view, edit, lines):
  first_line = lines[0]
  comment_type = 'js'

  if 'source.jsx' in view.scope_name(first_line.begin()):
    comment_type = 'jsx'

  for line in reversed(lines):
    begin = get_non_whitespace_pos(view, line)

    if comment_type == 'jsx':
      # JSX.
      view.insert(edit, line.end(), " */}")
      view.insert(edit, begin, "{/* ")
    else:
      # Normal JS comment.
      view.insert(edit, begin, "// ")

# Returns the position for the first non whitespace character on the target line
# or the line’s beginning if none is found.
def get_non_whitespace_pos(view, line):
  line_content = view.substr(line)
  match = re.match(r'^\s*(\S)', line_content)
  offset = 0
  if match is not None:
    offset = match.start(1)
  return line.begin() + offset

def match_to_region(offset, match, group = 1):
  group_offset = match.start(group)
  return sublime.Region(
    offset + group_offset,
    offset + group_offset + len(match.group(group))
  )

# TODO
def toggle_block(view, edit):
  for region in reversed(view.sel()):
    pass

# Toggle comment lines using single line comments.
def toggle_lines(view, edit):
  for region in reversed(view.sel()):
    lines = view.lines(region)
    first_line = lines[0]

    scopes = view.scope_name(first_line.begin())
    if 'string' in scopes:
      if 'punctuation.definition.string.begin' not in scopes:
        return

    # Comment’s begining will be “//”, “/*” or “{/*”, to simplify the detection we
    # can ignore the first character which will help detecting JSX comments too.
    scopes = view.scope_name(get_non_whitespace_pos(view, first_line) + 1)
    if 'comment' in scopes:
      uncomment_lines(view, edit, lines)
    else:
      comment_lines(view, edit, lines)

def uncomment_lines(view, edit, lines):
  block_begin = None
  block_end = None

  for line in reversed(lines):
    pass
    # cursor = get_non_whitespace_pos(view, line)
    # scopes = view.scope_name(cursor)

    # # We found the block’s end, now we need to find the beginning.
    # if block_end is not None:
    #   # Still inside the comment block.
    #   if 'comment.block' in scopes:
    #     continue
    #   # Find the beginning.

    # # We are in the middle of a block and we need to find the block’s end.
    # while 'comment.block' in scopes and 'punctuation.definition.comment.end' not in scopes:
    #   cursor += 1
    #   scopes = view.scope_name(cursor)

    # # Save the block’s end position.
    # comment_scopes = ['comment.block', 'punctuation.definition.comment.end']
    # if all(x in scopes for x in comment_scopes):
    #   block_end = cursor
    #   continue

    # # Remove the “// ”.
    # comment_scopes = ['comment.line', 'punctuation.definition.comment']
    # if all(x in scopes for x in comment_scopes):
    #   region = sublime.Region(cursor, cursor + 3)
    #   view.replace(edit, region, '')
    #   continue

    # line_content = view.substr(line)

    # # Remove the “/* */” when on the same line.
    # begin = re.match(r'^\s*(/\*\s*)', line_content)
    # end = re.match(r'^.*?(\s*\*/\s*)$', line_content)

    # if begin is not None and end is not None:
    #   view.replace(edit, match_to_region(line.begin(), end), '')
    #   view.replace(edit, match_to_region(line.begin(), begin), '')

    # # Remove the “{/* */}” when on the same line.
    # begin = re.match(r'^\s*(\{/\*\s*)', line_content)
    # end = re.match(r'^.*?(\s*\*/\s*\}\s*)$', line_content)

    # if begin is not None and end is not None:
    #   view.replace(edit, match_to_region(line.begin(), end), '')
    #   view.replace(edit, match_to_region(line.begin(), begin), '')

# Actual command to toggle the comment lines and blocks.
class NaomiToggleJsxCommentCommand(sublime_plugin.TextCommand):
  def __init__(self, view):
    self.view = view

  def run(self, edit, block):
    if block:
      # TODO
      toggle_block(self.view, edit)
    else:
      toggle_lines(self.view, edit)
