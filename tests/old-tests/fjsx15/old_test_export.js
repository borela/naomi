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

export var myVariable = 123
export default var myVariable = 123

export let myVariable = 123
export default let myVariable = 123

export const MY_CONSTANT = 123
export default const MY_CONSTANT = 123

export function myFunction() {}
export default function myFunction() {}

export class MyClass {}
export default class MyClass {}

export type MyObject = {}
export default type MyObject = {}

export typeof target
export default typeof target

export interface MyInterface {}
export default interface MyInterface {}

export default 1 + 1
export { target, target }
export { target as alias, target as alias }

export * from '...'
export { target, target } from '...'
export { target as alias, target as alias } from '...'
export { default as alias } from '...'
