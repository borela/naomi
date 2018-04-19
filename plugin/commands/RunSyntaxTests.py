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

from ..window import OutputPanel
from sublime import packages_path
from sublime_api import run_syntax_test
from sublime_plugin import WindowCommand
import os


class NaomiRunSyntaxTestsCommand(WindowCommand):
    def __init__(self, sublime_window):
        self.sublime_window = sublime_window

    def run(self):
        totalFiles = 0
        totalAssertions = 0
        totalFailedAssertions = 0
        testsPath = packages_path() + '/Naomi/tests/syntaxes'

        self.outputPanel = OutputPanel(self.sublime_window, {'name': 'naomi'})
        self.outputPanel.show()
        self.outputPanel.append('Naomi: Running syntax tests...')

        # Find the test files and run them.
        for path, directories, files in os.walk(testsPath):
            for file in files:
                # Get the full path to the file.
                target = os.path.join(path, file)
                # Remove anything before "Packages/Naomi".
                target = target[target.index('Packages/Naomi'):]
                # Run the tests.
                assertionsFound, messagesFound = run_syntax_test(target)
                # Print the error messages and update the counters.
                if messagesFound != '':
                    for message in messagesFound:
                        self.outputPanel.append(message)
                        totalFailedAssertions += 1
                totalFiles += 1
                totalAssertions += assertionsFound

        if totalFailedAssertions < 1:
            self.outputPanel.append(
                'Success: %d assertion(s) in %d file(s).' % (
                    totalAssertions, totalFiles
                )
            )
        else:
            self.outputPanel.append(
                'Error: %d/%d assertion(s) in %d file(s) failed.' % (
                    totalFailedAssertions, totalAssertions, totalFiles
                )
            )
