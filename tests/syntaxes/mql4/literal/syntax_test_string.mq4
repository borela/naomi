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

    "Something is 'here'..."
//  ^^^^^^^^^^^^^^^^^^^^^^^^ string.quoted.double.mql.4
//   ^^^^^^^^^^^^^^^^^^^^^^ string.content.mql.4
//  ^ punctuation.delimiter.string.begin.mql.4
//                         ^ punctuation.delimiter.string.end.mql.4
    "Something is \"here\"..."
//  ^^^^^^^^^^^^^^^^^^^^^^^^^^ string.quoted.double.mql.4
//   ^^^^^^^^^^^^^^^^^^^^^^^^ string.content.mql.4
//  ^ punctuation.delimiter.string.begin.mql.4
//                ^^ constant.character.escape.a.mql.4
//                      ^^ constant.character.escape.b.mql.4
//                           ^ punctuation.delimiter.string.end.mql.4
    "Escaped: \\\"\n\r\t\x0065\d65535"
//            ^^ constant.character.escape.a.mql.4
//              ^^ constant.character.escape.b.mql.4
//                ^^ constant.character.escape.a.mql.4
//                  ^^ constant.character.escape.b.mql.4
//                    ^^ constant.character.escape.a.mql.4
//                      ^^^^^^ constant.character.escape.b.mql.4
//                            ^^^^^^^ constant.character.escape.a.mql.4
