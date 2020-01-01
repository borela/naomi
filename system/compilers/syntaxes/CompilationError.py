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

from ruamel.yaml.comments import LineCol

class CompilationError(Exception):
    def __init__(self, message, path=None, location=None):
        if path and location:
            if isinstance(location, LineCol):
                line = location.line
                column = location.col
            else:
                line = location.line
                column = location.column

            message = '%s (%i, %i): %s' % (
                path,
                line + 1,
                column + 1,
                message,
            )

        Exception.__init__(self, message)
