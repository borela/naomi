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

from Naomi.system.paths import (
    COMMANDS_SRC_DIR,
    COMMANDS_BUILD_DIR,
)

from Naomi.system.compilers.commands import compile_commands
from Naomi.system.logging import get_logger
from sublime_plugin import ApplicationCommand
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


class EventHandler(PatternMatchingEventHandler):
    patterns = ['*.yml']

    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)

    def process(self, event):
        compile_commands(COMMANDS_SRC_DIR, COMMANDS_BUILD_DIR)


class NaomiWatchCommandsCommand(ApplicationCommand):
    def __init__(self):
        self.watching = False

    def run(self):
        logger = get_logger()

        if not self.watching:
            self.observer = Observer()
            self.observer.schedule(
                EventHandler(),
                path=COMMANDS_SRC_DIR,
                recursive=True,
            )
            self.observer.start()
            self.watching = True
            logger.info('Started watching commands...')
        else:
            self.observer.stop()
            self.watching = False
            logger.info('Stopped watching commands.')
