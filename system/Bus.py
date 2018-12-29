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

        message_type = message['type']
        specific_listeners = self.__listeners['specific']
        specific_listeners = specific_listeners.get(message_type, None)

        if specific_listeners is not None:
            for listener in specific_listeners:
                listener(message)


    def subscribe(self, *args, **kwargs):
        message_type = None
        callback = None

        if kwargs:
            message_type = kwargs.get('type', None)
            callback = kwargs.get('callback', None)
        elif args:
            if len(args) < 2:
                callback = args[0]
            else:
                message_type = args[0]
                callback = args[1]

        return self._subscribe(message_type, callback)


    def _subscribe(self, message_type, callback):
        if not callable(callback):
            raise ValueError('Invalid callback.')

        if message_type is None:
            self.__listeners['all'].append(callback)
            return

        if message_type not in self.__listeners['specific']:
            self.__listeners['specific'][message_type] = []

        self.__listeners['specific'][message_type].append(callback)


    """Stores listeners for specific message types and all of them."""
    __listeners = {
        'all': [],
        'specific': {},
    }
