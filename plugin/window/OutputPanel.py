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


class OutputPanel(object):
    def __init__(self, sublime_window, settings):
        self.sublime_window = sublime_window
        self.settings = settings

        self.settings.setdefault('line_numbers', True)
        self.settings.setdefault('word_wrap', False)

        self.__create_panel()
        self.__configure_panel()

    def append(self, text):
        self.panel.run_command('append', {'characters': text + '\n'})

    def show(self):
        name = self.settings['name']
        self.sublime_window.run_command(
            'show_panel', {'panel': 'output.' + name}
        )

    def __configure_panel(self):
        panel_settings = self.panel.settings()
        for key, value in self.settings.items():
            panel_settings.set(key, value)

    def __create_panel(self):
        name = self.settings['name']
        self.panel = self.sublime_window.create_output_panel(name)
