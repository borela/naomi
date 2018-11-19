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

  subscribers = {
    'all': [],
    'specific': [],
  }

  def publish(self, subject):
    for subscriber in self.subscribers['all']:
      subscriber(subject)

    subject_type = subject['type']
    specific_subscribers = self.subscribers['specific'].get(subject_type, None)

    if specific_subscribers is not None:
      for subscriber in specific_subscribers:
        subscriber(subject)


  def subcribe(self, arg):
    if callable(arg):
      return self._subscribe(callback=arg)
    return self._subscribe(**arg)


  def _subscribe(self, **kargs):
    subject_type = kargs.get('type', None)
    callback = kargs['callback']

    if subject_type is None:
      self.subscribers['all'].push(callback)
      return

    subscribers_list = self.subscribers['specific'].get(subject_type, [])
    subscribers_list.push(callback)

    self.subscribers['specific'][subject_type] = subscribers_list
