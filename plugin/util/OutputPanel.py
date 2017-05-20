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

import os
import sublime
import sublime_api
import sublime_plugin

class OutputPanel(object):
  def __init__(self, window, name):
    self.window = window
    self.panelName = name
    self.panel = window.create_output_panel(name)
    self.panel.settings().set('word_wrap', False)
    self.panel.settings().set('line_numbers', True)

  def append(self, text):
    self.panel.run_command('append', { 'characters': text + '\n' })

  def show(self):
      self.window.run_command('show_panel', { 'panel': 'output.' + self.panelName })
