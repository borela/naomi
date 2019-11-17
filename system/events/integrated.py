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

INTEGRATED_COMMANDS = 'INTEGRATED_COMMANDS'
INTEGRATED_KEYMAPS = 'INTEGRATED_KEYMAPS'
INTEGRATED_MENUS = 'INTEGRATED_MENUS'
INTEGRATED_PREFERENCES = 'INTEGRATED_PREFERENCES'
INTEGRATED_SYNTAXES = 'INTEGRATED_SYNTAXES'

def integrated_commands(src_dir, build_dir):
    return {
        'type': INTEGRATED_COMMANDS,
        'payload': {
            'src_dir': src_dir,
            'build_dir': build_dir,
        }
    }

def integrated_keymaps(src_dir, build_dir):
    return {
        'type': INTEGRATED_KEYMAPS,
        'payload': {
            'src_dir': src_dir,
            'build_dir': build_dir,
        }
    }

def integrated_menus(src_dir, build_dir):
    return {
        'type': INTEGRATED_MENUS,
        'payload': {
            'src_dir': src_dir,
            'build_dir': build_dir,
        }
    }

def integrated_preferences(src_dir, build_dir):
    return {
        'type': INTEGRATED_PREFERENCES,
        'payload': {
            'src_dir': src_dir,
            'build_dir': build_dir,
        }
    }

def integrated_syntaxes(src_dir, build_dir):
    return {
        'type': INTEGRATED_SYNTAXES,
        'payload': {
            'src_dir': src_dir,
            'build_dir': build_dir,
        }
    }
