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
        self.__engine = engine
        self.__event = event
        self.__subscriber = subscriber

    def isActive(self):
        return self.engine.isSubscribed(
            self.__event,
            self.__subscriber,
        )

    def subscribe(self):
        if self.isActive():
            return
        return self.engine.on(
            self.__event,
            self.__subscriber,
        )

    def unsubscribe(self):
        self.__engine.removeSubscriber(
            self.__event,
            self.__subscriber,
        )
