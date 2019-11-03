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

from Naomi.system.compilers.preferences import compile_preferences
from Naomi.system.event_bus import EVENT_BUS
from Naomi.system.logging import log_info
from Naomi.system.state import STORE
from sublime_plugin import ApplicationCommand
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from Naomi.system.events import (
    not_watching_preferences,
    watching_preferences,
)


class EventHandler(PatternMatchingEventHandler):
    patterns = ['*.yml']

    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)

    def process(self, event):
        compile_preferences(
            STORE['directories']['integration']['preferences']['src'],
            STORE['directories']['integration']['preferences']['build'],
        )


class NaomiWatchPreferencesCommand(ApplicationCommand):
    def __init__(self):
        self.observer = None

    def description(self):
        if STORE['watching']['preferences']:
            return 'Unwatch Preferennces'
        return 'Watch Preferennces'

    def run(self):
        if not STORE['watching']['preferences']:
            self.observer = Observer()
            self.observer.schedule(
                EventHandler(),
                path=STORE['directories']['integration']['preferences']['src'],
                recursive=True,
            )
            self.observer.start()
            EVENT_BUS.emit(watching_preferences())
            log_info('Started watching preferences...')
        else:
            self.observer.stop()
            EVENT_BUS.emit(not_watching_preferences())
            log_info('Stopped watching preferences.')
