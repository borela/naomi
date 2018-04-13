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

from Naomi.plugin.region.scan import (
    search_non_whitespace,
    search_non_whitespace_reverse
)
from sublime import Region


def trim_region(view, region):
    # The region is already collapsed.
    if region.size() < 1:
        return region

    begin = search_non_whitespace(view, region)
    end = search_non_whitespace_reverse(view, region) + 1

    # The entire line is empty.
    if end < begin:
        begin = end
        end = begin

    return Region(begin, end)
