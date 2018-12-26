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

class Bus:
    """ Generic communication bus. """

    def publish(self, message):
        all_listeners = self.__listeners['all']
        for listener in all_listeners:
            listener(message)

        topic = message['topic']
        specific_listeners = self.__listeners['specific'].get(topic, None)

        if specific_listeners is not None:
            for listener in specific_listeners:
                listener(message)


    def subscribe(self, *args, **kwargs):
        topic = None
        callback = None

        if kwargs:
            topic = kwargs.get('topic', None)
            callback = kwargs.get('callback', None)
        elif args:
            if len(args) < 2:
                callback = args[0]
            else:
                topic = args[0]
                callback = args[1]

        return self._subscribe(topic, callback)


    def _subscribe(self, topic, callback):
        if not callable(callback):
            raise ValueError('Invalid callback.')

        if topic is None:
            self.__listeners['all'].append(callback)
            return

        if topic not in self.__listeners['specific']:
            self.__listeners['specific'][topic] = []

        self.__listeners['specific'][topic].append(callback)


    """Stores listeners for specific topics and all of them."""
    __listeners = {
        'all': [],
        'specific': {},
    }
