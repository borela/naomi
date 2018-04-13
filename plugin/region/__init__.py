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

from .expand import (
  expand,
  expand_by_scope,
  expand_partial_comments,
  expand_partial_comments_with_jsx,
  expand_partial_lines
)
from .generate import (
  generate_comment_punctuation_region,
  generate_jsjsx_comment_punctuation_region,
  generate_region_for_scope
)
from .scan import (
  scan,
  scan_reverse,
  search_non_whitespace,
  search_non_whitespace_reverse
)
from .trim import trim_region

__all__ = [
  expand,
  expand_by_scope,
  expand_partial_comments,
  expand_partial_comments_with_jsx,
  expand_partial_lines,
  generate_comment_punctuation_region,
  generate_jsjsx_comment_punctuation_region,
  generate_region_for_scope,
  scan,
  scan_reverse,
  search_non_whitespace,
  search_non_whitespace_reverse,
  trim_region
]
