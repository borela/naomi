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

from .EventSubscription import EventSubscription

class AnyEventSubscription(EventSubscription):
    def __init__(self, engine, subscriber):
        super(AnyEventSubscription, self).__init__(
            engine=engine,
            event=None,
            subscriber=subscriber,
        )

    def is_active(self):
        return self._engine.is_subscribed(self._subscriber)

    def subscribe(self):
        if self.is_active():
            return
        return self._engine.on_any(self._subscriber)

    def unsubscribe(self):
        self._engine.unsubscribe(self._subscriber)
