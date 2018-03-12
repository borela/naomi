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

   let [a=0,...b=0] = [1,2,3];
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.naomi
// ^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.declaration.variable.js
//     ^^^^^^^^^^^^ .meta.binding.destructuring.sequence.js
//                    ^^^^^^^ .meta.sequence.js
// ^^^ .storage.type.js
//     ^ .punctuation.section.brackets.begin.js
//      ^ .variable.other.readwrite.js
//       ^ .keyword.operator.other.assignment.js
//        ^ .constant.numeric.decimal.js
//         ^ .punctuation.separator.comma.js
//          ^^^ .keyword.operator.rest.js
//             ^ .variable.other.readwrite.js
//              ^ .keyword.operator.other.assignment.js
//               ^ .constant.numeric.decimal.js
//                ^ .punctuation.section.brackets.end.js
//                  ^ .keyword.operator.other.assignment.js
//                    ^ .punctuation.section.brackets.begin.js
//                     ^ .constant.numeric.decimal.js
//                      ^ .punctuation.separator.comma.js
//                       ^ .constant.numeric.decimal.js
//                        ^ .punctuation.separator.comma.js
//                         ^ .constant.numeric.decimal.js
//                          ^ .punctuation.section.brackets.end.js
//                           ^ .punctuation.terminator.js
   let [[a=0,...b=0],[a=0,...b=0]] = [1,2,3];
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.naomi
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.declaration.variable.js
//     ^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.binding.destructuring.sequence.js
// ^^^ .storage.type.js
//     ^^ .punctuation.section.brackets.begin.js
//       ^ .variable.other.readwrite.js
//        ^ .keyword.operator.other.assignment.js
//         ^ .constant.numeric.decimal.js
//          ^ .punctuation.separator.comma.js
//           ^^^ .keyword.operator.rest.js
//              ^ .variable.other.readwrite.js
//               ^ .keyword.operator.other.assignment.js
//                ^ .constant.numeric.decimal.js
//                 ^ .punctuation.section.brackets.end.js
//                  ^ .punctuation.separator.comma.js
//                   ^ .punctuation.section.brackets.begin.js
//                    ^ .variable.other.readwrite.js
//                     ^ .keyword.operator.other.assignment.js
//                      ^ .constant.numeric.decimal.js
//                       ^ .punctuation.separator.comma.js
//                        ^^^ .keyword.operator.rest.js
//                           ^ .variable.other.readwrite.js
//                            ^ .keyword.operator.other.assignment.js
//                             ^ .constant.numeric.decimal.js
//                              ^^ .punctuation.section.brackets.end.js
//                                 ^ .keyword.operator.other.assignment.js
//                                   ^ .punctuation.section.brackets.begin.js
//                                    ^ .constant.numeric.decimal.js
//                                     ^ .punctuation.separator.comma.js
//                                      ^ .constant.numeric.decimal.js
//                                       ^ .punctuation.separator.comma.js
//                                        ^ .constant.numeric.decimal.js
//                                         ^ .punctuation.section.brackets.end.js
//                                          ^ .punctuation.terminator.js
