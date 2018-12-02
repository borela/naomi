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

  def publish(self, topic):
    for listener in self._listeners['all']:
      listener(topic)

    topic_type = topic['type']
    specific__listeners = self._listeners['specific'].get(topic_type, None)

    if specific__listeners is not None:
      for listener in specific__listeners:
        listener(topic)


  def subcribe(self, arg):
    if callable(arg):
      return self._subscribe(callback=arg)
    return self._subscribe(**arg)


  def _subscribe(self, **args):
    topic_type = args.get('type', None)
    callback = args['callback']

    if topic_type is None:
      self._listeners['all'].push(callback)
      return

    _listeners_list = self._listeners['specific'].get(topic_type, [])
    _listeners_list.push(callback)

    self._listeners['specific'][topic_type] = _listeners_list


  """Stores listeners for specific topics and all of them."""
  _listeners = {
    'all': [],
    'specific': [],
  }
