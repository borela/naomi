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

from os.path import dirname, join
from sublime import active_window, Region, set_clipboard
from unittest import TestCase
import sys


class NaomiTestCase(TestCase):
    def loadFixture(self, *relative_path):
        if self.fixture_loaded:
            raise RuntimeError("Fixture already loaded.")

        base_path = dirname(sys.modules[self.__class__.__module__].__file__)
        full_path = join(base_path, *relative_path)

        # Load fixture.
        fixture_content = ""
        with open(full_path, "r") as file:
            fixture_content = file.read()

        self.setViewText(fixture_content)
        self.setCursorPosition(0)
        self.fixture_loaded = True

    def setCursorPosition(self, offset):
        self.view.sel().clear()
        self.view.sel().add(Region(offset))

    def setViewText(self, text):
        self.view.run_command("insert", {"characters": text})

    def setUp(self):
        set_clipboard("")
        self.view = active_window().new_file()
        self.view.set_scratch(True)
        self.fixture_loaded = False

    def tearDown(self):
        if self.view:
            self.view.close()
