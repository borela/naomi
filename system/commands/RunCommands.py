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

from sublime import run_command
from sublime_plugin import TextCommand


class NaomiRunCommandsCommand(TextCommand):
    def run(self, edit, commands = None):
        # Ignore empty commands.
        if commands is None:
            return

        for command in commands:
            if 'type' not in command:
                command['type'] = 'view'

            command_receiver = None
            command_type = command['type']

            if command_type == 'app':
                command_receiver = sublime
            elif command_type == 'window':
                command_receiver = self.view.window
            elif command_type == 'view':
                command_receiver = self.view
            else:
                raise ValueError('Invalid command type “%s”.' %s)

            command_receiver.run_command(
                command['command'],
                command['args']
            )
