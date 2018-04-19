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

   let {[a + b]:abc=0, abc:abc, ...abc=0} = {a:1};
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.naomi
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.declaration.variable.js
//                                               ^ - .meta.declaration.variable.js
//     ^ .meta.binding.destructuring.mapping.js
//      ^^^^^^^ - .meta.binding.destructuring.mapping.js
//      ^^^^^^^ .meta.binding.destructuring.mapping.key.computed.js
//                     ^^^ .meta.binding.destructuring.mapping.key.js
//                     ^^^ .meta.object-literal.key.js
//                        ^^^^^^^^^^^^^^ .meta.binding.destructuring.mapping.js
//                                          ^^^^^ .meta.object-literal.js
// ^^^ .storage.type.js
//     ^ .punctuation.section.block.begin.js
//      ^ .punctuation.section.brackets.begin.js
//       ^ variable.other.readwrite.js
//         ^ keyword.operator.arithmetic.js
//           ^ variable.other.readwrite.js
//            ^ .punctuation.section.brackets.end.js
//             ^ .punctuation.binding.js
//              ^^^ variable.other.readwrite.js
//                 ^ .keyword.operator.other.assignment.js
//                  ^ .constant.numeric.decimal.js
//                   ^ .punctuation.separator.comma.js
//                        ^ .punctuation.binding.js
//                         ^^^ variable.other.readwrite.js
//                            ^ .punctuation.separator.comma.js
//                              ^^^ .keyword.operator.rest.js
//                                 ^^^ variable.other.readwrite.js
//                                    ^ .keyword.operator.other.assignment.js
//                                     ^ .constant.numeric.decimal.js
//                                      ^ .punctuation.section.block.end.js
//                                        ^ .keyword.operator.other.assignment.js
//                                          ^ .punctuation.section.block.begin.js
//                                           ^ string.unquoted.js
//                                            ^ .punctuation.separator.key-value.js
//                                             ^ .constant.numeric.decimal.js
//                                              ^ .punctuation.section.block.end.js
//                                               ^ .punctuation.terminator.js
