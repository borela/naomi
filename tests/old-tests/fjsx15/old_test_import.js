// SYNTAX TEST "Packages/Naomi/syntaxes/naomi.fjsx15.sublime-syntax"

// Licensed under the Apache License, Version 2.0 (the “License”); you may not
// use this file except in compliance with the License. You may obtain a copy of
// the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an “AS IS” BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations under
// the License.

import '...'

import { default as alias } from '...'

import * from '...'
import * as alias from '...'

import target from '...'
import target as alias from '...'

import { target, target } from '...'
import { target as alias, target as alias } from '...'

import target, { target, target } from '...'
import target as alias, { target as alias, target as alias } from '...'

import type target from '...'
import type target as alias from '...'

import type { target, target } from '...'
import type { target as alias, target as alias } from '...'

import type target, { target, target } from '...'
import type target as alias, { target as alias, target as alias } from '...'

import typeof target from '...'
import typeof { target } from '...'
import typeof { target as alias } from '...'

import { target, type target, typeof target } from '...'

declare module "C" {
  import type { DT } from "D";
  export type CT = { D: DT };
}
