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
    isabs,
    isdir,
    isfile,
    join,
    realpath,
    relpath,
)

from .state_store import STATE_STORE

# Calculates the relative path to the package’s root.
def package_relpath(path):
    return relpath(path, join(dirname(__file__), '..', '..'))

def packages_dir():
    return realpath(join(dirname(__file__), '..', '..'))

# Resolve relative paths to the syntaxes src directories being managed by
# the Naomi’s system.
def resolve_syntax_entry(path):
    if isfile(path):
        return realpath(path)

    dirs = [
        (integrated['src_dir'], integrated['build_dir'])
        for integrated in STATE_STORE['integrated']['syntaxes']
    ]

    # Allow external packages to override Naomi’s syntax files.
    dirs.reverse()

    # Try to find a file with the integrated src directories.
    for src_dir, build_dir in dirs:
        resolved_path = join(src_dir, path)

        if isdir(resolved_path):
            resolved_path = join(resolved_path, 'index.yml')

        print(resolved_path)

        if isfile(resolved_path):
            return resolved_path, src_dir, build_dir

    raise RuntimeError('File not found: %s' % path)
