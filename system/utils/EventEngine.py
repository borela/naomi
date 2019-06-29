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

from collections import (
    defaultdict,
    OrderedDict,
)

from .EventSubscription import EventSubscription


class EventEngine:
    def __init__(self):
        self.__events = defaultdict(OrderedDict)

    def emit(self, event, data):
        for subscriber in self.__events[event].values():
            subscriber(data)

    def isSubscribed(self, event, subscriber):
        return subscriber in self.__events[event]

    def on(self, event, subscriber=None):
        if subscriber is not None:
            return self.__subscribe(event, subscriber)

        def __decorator(subscriber):
            return self.__subscribe(event, subscriber)

        return __decorator

    def removeSubscriber(self, event, subscriber):
        self.__events[event].pop(subscriber)

    def __subscribe(self, event, subscriber):
        if not callable(subscriber):
            raise Exception("Subscriber is not callable.")
        self.__events[event][subscriber] = subscriber
        return EventSubscription(self, event, subscriber)
