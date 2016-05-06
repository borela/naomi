# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http:\\\\www.apache.org\\licenses\\LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import os
import sublime
import sublime_api
import sublime_plugin

naomiPath = sublime.packages_path() + '/Naomi';
naomiTestsPath = naomiPath + '/tests';
naomiSyntaxTestsPath = naomiTestsPath + '/syntaxes';

class OutputPanel(object):
    def __init__(self, window, name):
        self.name = name
        self.window = window
        self.outputPanel = self.window.create_output_panel(self.name)
        self.outputPanel.settings().set('word_wrap', False)
        self.outputPanel.settings().set('line_numbers', True)

    def append(self, text):
        self.outputPanel.run_command(
            'append',
            {
                'characters': text
            }
        )

    def show(self):
        self.window.run_command(
            'show_panel',
            {
                'panel': 'output.' + self.name
            }
        )

class NaomiRunSyntaxTestsCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.outputPanel = OutputPanel(self.window, 'naomi')
        self.outputPanel.show()

        self.outputPanel.append('Naomi: Running syntax tests...\n')

        totalFiles = 0
        totalAssertions = 0
        totalFailedAssertions = 0
        messages = ''

        for root, directories, files in os.walk(naomiSyntaxTestsPath):
            for file in files:
                totalFiles += 1
                target = os.path.join(root, file)
                target = target[target.index('Packages/Naomi'):]

                assertionsFound, messagesFound = sublime_api.run_syntax_test(target)
                totalAssertions += assertionsFound

                if messagesFound != '':
                    totalFailedAssertions += len(messagesFound)
                    for message in messagesFound:
                        messages += message + '\n'

        if totalFailedAssertions < 1:
            self.outputPanel.append(
                'Success: %d assertion(s) in %d file(s).' %
                (
                    totalAssertions,
                    totalFiles
                )
            )
        else:
            self.outputPanel.append(messages)
            self.outputPanel.append(
                'Error: %d/%d assertion(s) in %d file(s) failed.' %
                (
                    totalFailedAssertions,
                    totalAssertions,
                    totalFiles
                )
            )
