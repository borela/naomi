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

from Naomi.system.events import (
    stopped_watching_syntaxes,
    watching_syntaxes,
)

from Naomi.system import (
    EVENT_BUS,
    log_info,
    STATE_STORE,
)

# from Naomi.system.compilers import compile_syntaxes
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
        # compile_syntaxes(
        #     STATE_STORE['directories']['syntaxes']['src'],
        #     STATE_STORE['directories']['syntaxes']['build'],
        # )
        pass


class NaomiWatchSyntaxesCommand(ApplicationCommand):
    def __init__(self):
        self.observer = None

    def description(self):
        if STATE_STORE['watching']['syntaxes']:
            return 'Unwatch Syntaxes'
        return 'Watch Syntaxes'

    def run(self):
        if not STATE_STORE['watching']['syntaxes']:
            self.observer = Observer()
            self.observer.schedule(
                EventHandler(),
                path=STATE_STORE['directories']['syntaxes']['src'],
                recursive=True,
            )
            self.observer.start()
            EVENT_BUS.emit(watching_syntaxes())
            log_info('Started watching syntaxes...')
        else:
            self.observer.stop()
            EVENT_BUS.emit(stopped_watching_syntaxes())
            log_info('Stopped watching syntaxes.')
