// SYNTAX TEST "Packages/Naomi/syntaxes/naomi.mql4.sublime-syntax"

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

    'a'
//  ^^^ string.quoted.single.mql.mql4
    '\\'
//  ^^^^ string.quoted.single.mql.mql4
//   ^^ constant.character.escape.a.mql.mql4
//  ^ punctuation.definition.string.begin.mql.mql4
//     ^ punctuation.definition.string.end.mql.mql4
    '\n'
//  ^^^^ string.quoted.single.mql.mql4
//   ^^ constant.character.escape.a.mql.mql4
//  ^ punctuation.definition.string.begin.mql.mql4
//     ^ punctuation.definition.string.end.mql.mql4
    '\t'
//  ^^^^ string.quoted.single.mql.mql4
//   ^^ constant.character.escape.a.mql.mql4
//  ^ punctuation.definition.string.begin.mql.mql4
//     ^ punctuation.definition.string.end.mql.mql4
    '\r'
//  ^^^^ string.quoted.single.mql.mql4
//   ^^ constant.character.escape.a.mql.mql4
//  ^ punctuation.definition.string.begin.mql.mql4
//     ^ punctuation.definition.string.end.mql.mql4
    '\x0065'
//  ^^^^^^^^ string.quoted.single.mql.mql4
//   ^^^^^^ constant.character.escape.a.mql.mql4
//  ^ punctuation.definition.string.begin.mql.mql4
//         ^ punctuation.definition.string.end.mql.mql4
    '\d65535'
//  ^^^^^^^^^ string.quoted.single.mql.mql4
//   ^^^^^^^ constant.character.escape.a.mql.mql4
//  ^ punctuation.definition.string.begin.mql.mql4
//          ^ punctuation.definition.string.end.mql.mql4
