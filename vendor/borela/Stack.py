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

class Stack(list):
    __slots__ = ['__i']

    def __getitem__(self, index):
        return list.__getitem__(self, len(self) - 1 - index)

    def __iter__(self):
        self.__i = -1
        return self

    def __next__(self):
        self.__i += 1

        if self.__i >= len(self):
            raise StopIteration()

        return self[self.__i]

    def __repr__(self):
        items = ''
        for item in self:
            if items:
                items += ','
            items += repr(item)
        return '[%s]' % items

    def push(self, value):
        self.append(value)

    def push_back(self, value):
        self.insert(0, value)
