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
    stopped_watching_keymaps,
    watching_keymaps,
)

from Naomi.system import (
    EVENT_BUS,
    log_info,
    STATE_STORE,
)

from Naomi.system.compilers import compile_integrated_keymaps
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
        compile_integrated_keymaps()


class NaomiWatchKeymapsCommand(ApplicationCommand):
    def __init__(self):
        self.observer = None

    def description(self):
        if STATE_STORE['watching']['keymaps']:
            return 'Unwatch Keymaps'
        return 'Watch Keymaps'

    def run(self):
        if not STATE_STORE['watching']['keymaps']:
            self.observer = Observer()

            for integrated in STATE_STORE['integrated']['keymaps']:
                self.observer.schedule(
                    EventHandler(),
                    path=integrated['src_dir'],
                    recursive=True,
                )

            self.observer.start()
            EVENT_BUS.emit(watching_keymaps())
            log_info('Started watching keymaps...')
        else:
            self.observer.stop()
            EVENT_BUS.emit(stopped_watching_keymaps())
            log_info('Stopped watching keymaps.')
