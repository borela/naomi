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
    """
    This command can be used in key bindings to run multiple commands.
    """
    def run(self, edit, commands = None):
        # Ignore empty commands.
        if commands is None:
            return

        for command in commands:
            if 'on' not in command:
                command['on'] = 'view'

            command_receiver = None
            command_on = command['on']

            if command_on == 'app':
                command_receiver = sublime
            elif command_on == 'window':
                command_receiver = self.view.window
            elif command_on == 'view':
                command_receiver = self.view
            else:
                raise ValueError('Invalid command destination “%s”.' % command_on)

            command_receiver.run_command(
                command['command'],
                command['args']
            )
