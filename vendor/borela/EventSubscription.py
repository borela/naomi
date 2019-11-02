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


class EventSubscription:
    def __init__(self, engine, event, subscriber):
        self._engine = engine
        self._event = event
        self._subscriber = subscriber

    def isActive(self):
        return self._engine.isSubscribed(
            self._subscriber,
            self._event,
        )

    def subscribe(self):
        if self.isActive():
            return
        return self.engine.on(
            self._event,
            self._subscriber,
        )

    def unsubscribe(self):
        self._engine.unsubscribe(
            self._subscriber,
            self._event,
        )
