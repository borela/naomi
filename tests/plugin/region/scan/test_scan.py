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

from ...NaomiTestCase import NaomiTestCase
from Naomi.plugin.region.scan import scan


def false_predicate(view, offset):
    return False


def true_predicate(view, offset):
    return True


class TestScanNoLimit(NaomiTestCase):
    def test_stop_at_the_beginning(self):
        self.loadFixture("fixtures", "lorem.txt")
        resulting_offset = scan(self.view, 0, false_predicate)
        self.assertEqual(resulting_offset, 0)

    def test_stop_at_the_last_char_pos(self):
        self.loadFixture("fixtures", "lorem.txt")
        resulting_offset = scan(self.view, 0, true_predicate)
        self.assertEqual(resulting_offset, self.view.size() - 1)
