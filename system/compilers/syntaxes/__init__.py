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

# from Naomi.system.fs import (
#     load_yaml,
#     write_file,
# )

# from os.path import (
#     isfile,
#     join,
#     realpath,
# )

from Naomi.system.logging import (
    # log_error,
    log_info,
)

# from Naomi.system.state import STORE
# from Naomi.system.headers import syntax as syntax_header
# from Naomi.system.paths import package_path


def compile_syntaxes(dir_path, dest_dir_path):
    log_info('Building syntaxes...')

    # syntaxes = get_setting('syntaxes', [])

    # for syntax in syntaxes:
    #     name = syntax['name']
    #     entry = syntax['entry']
    #     output = syntax['output']
    #     features = syntax['features']

    #     entry = realpath(join(dir_path, entry))
    #     if not isfile(entry):
    #         log_error('Entry not found: %s' % entry)
    #         continue

    #     output = realpath(join(dest_dir_path, output))


def resolve_path(current_dir, target_path):
    pass
