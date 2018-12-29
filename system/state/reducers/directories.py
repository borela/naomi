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

from os.path import (
    dirname,
    join,
    realpath,
)


NAOMI_DIR = realpath(join(dirname(__file__), '..', '..', '..'))
SYSTEM_DIR = realpath(join(dirname(__file__), '..', '..'))
SCHEMES_DIR = join(NAOMI_DIR, 'schemes')
SYNTAXES_DIR = join(NAOMI_DIR, 'syntaxes')

INTEGRATION_DIR = join(NAOMI_DIR, 'integration')
COMMANDS_DIR = join(INTEGRATION_DIR, 'commands')
KEYMAPS_DIR = join(INTEGRATION_DIR, 'keymaps')
MENUS_DIR = join(INTEGRATION_DIR, 'menus')
PREFERENCES_DIR = join(INTEGRATION_DIR, 'preferences')

INITIAL_STATE = {
  'naomi': NAOMI_DIR,
  'system': {
    'root': SYSTEM_DIR,
    'headers': join(SYSTEM_DIR, 'headers'),
  },
  'syntaxes': {
    'root': SYNTAXES_DIR,
    'src': join(SYNTAXES_DIR, 'src'),
    'build': join(SYNTAXES_DIR, 'build'),
  },
  'integration': {
    'root': join(NAOMI_DIR, 'integration'),
    'commands': {
      'root': COMMANDS_DIR,
      'src': join(COMMANDS_DIR, 'src'),
      'build': join(COMMANDS_DIR, 'build'),
    },
    'keymaps': {
      'root': KEYMAPS_DIR,
      'src': join(KEYMAPS_DIR, 'src'),
      'build': join(KEYMAPS_DIR, 'build'),
    },
    'menus': {
      'root': MENUS_DIR,
      'src': join(MENUS_DIR, 'src'),
      'build': join(MENUS_DIR, 'build'),
    },
    'preferences': {
      'root': PREFERENCES_DIR,
      'src': join(PREFERENCES_DIR, 'src'),
      'build': join(PREFERENCES_DIR, 'build'),
    },
  },
}

def reducer(state=INITIAL_STATE, event=None):
  return state
