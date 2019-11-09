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
    stopped_watching_menus,
    watching_menus,
)

from Naomi.system import (
    EVENT_BUS,
    log_info,
    STATE_STORE,
)

from Naomi.system.compilers import compile_menus
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
        compile_menus()


class NaomiWatchMenusCommand(ApplicationCommand):
    def __init__(self):
        self.observer = None

    def description(self):
        if STATE_STORE['watching']['menus']:
            return 'Unwatch Menus'
        return 'Watch Menus'

    def run(self):
        src_dir = (
            STATE_STORE['directories']['integration']['menus']['src']
        )

        if not STATE_STORE['watching']['menus']:
            self.observer = Observer()

            for integrated in STATE_STORE['integrated']['menus']:
                self.observer.schedule(
                    EventHandler(),
                    path=integrated['src_dir'],
                    recursive=True,
                )

            self.observer.start()
            EVENT_BUS.emit(watching_menus())
            log_info('Started watching menus...')
        else:
            self.observer.stop()
            EVENT_BUS.emit(stopped_watching_menus())
            log_info('Stopped watching menus.')
