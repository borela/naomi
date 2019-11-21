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
    stopped_watching_commands,
    stopped_watching_keymaps,
    stopped_watching_menus,
    stopped_watching_preferences,
    stopped_watching_syntaxes,

    watching_commands,
    watching_keymaps,
    watching_menus,
    watching_preferences,
    watching_syntaxes,
)

from Naomi.system import (
    EVENT_BUS,
    log_info,
    STATE_STORE,
)

from Naomi.system.compilers import (
    compile_configured_syntaxes,
    compile_integrated_commands,
    compile_integrated_keymaps,
    compile_integrated_menus,
    compile_integrated_preferences,
)

from sublime import set_timeout_async
from sublime_plugin import ApplicationCommand
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

COMPILERS = {
    'syntaxes': compile_configured_syntaxes,
    'commands': compile_integrated_commands,
    'keymaps': compile_integrated_keymaps,
    'menus': compile_integrated_menus,
    'preferences': compile_integrated_preferences,
}

STOPPED_EVENTS = {
    'commands': stopped_watching_commands,
    'keymaps': stopped_watching_keymaps,
    'menus': stopped_watching_menus,
    'preferences': stopped_watching_preferences,
    'syntaxes': stopped_watching_syntaxes,
}

WATCHING_EVENTS = {
    'commands': watching_commands,
    'keymaps': watching_keymaps,
    'menus': watching_menus,
    'preferences': watching_preferences,
    'syntaxes': watching_syntaxes,
}

class EventHandler(PatternMatchingEventHandler):
    patterns = ['*.yml']

    def __init__(self, compiler):
        self.compiler = compiler

    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)

    def process(self, event):
        set_timeout_async(lambda: self.compiler())

class NaomiWatchCommand(ApplicationCommand):
    def __init__(self):
        self.observers = {}

    def description(self, what):
        if STATE_STORE['watching'][what]:
            return 'Unwatch %s' % what.title()
        return 'Watch %s' % what.title()

    def run(self, what):
        if not STATE_STORE['watching'][what]:
            self.observers[what] = Observer()

            for integrated in STATE_STORE['integrated'][what]:
                self.observers[what].schedule(
                    EventHandler(COMPILERS[what]),
                    path=integrated['src_dir'],
                    recursive=True,
                )

            self.observers[what].start()
            EVENT_BUS.emit(WATCHING_EVENTS[what]())
            log_info('Started watching %s...' % what)
        else:
            self.observers[what].stop()
            EVENT_BUS.emit(STOPPED_EVENTS[what]())
            log_info('Stopped watching %s.' % what)
