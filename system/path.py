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
    isfile,
    join,
    realpath,
    relpath,
)

from .state_store import STATE_STORE


def locate_syntax_file(path):
    """
    Resolve relative paths to the syntaxes src directories being managed by
    the Naomi’s system.
    """

    if isabs(path):
        return realpath(path)

    src_dirs = [
        integrated['src_dir']
        for integrated in STATE_STORE['integrated']['syntaxes']
    ]

    # Allow external packages to override Naomi’s syntax files.
    src_dirs.reverse()

    # Try to find a file with the integrated src directories.
    for src_dir in src_dirs:
        resolved_path = join(src_dir, path)

        if isfile(resolved_path):
            return resolved_path

    raise RuntimeError('File not found: %s' % path)


def package_relpath(path):
    """
    Calculates the relative path to the package’s root.
    """
    return relpath(path, join(dirname(__file__), '..', '..'))
