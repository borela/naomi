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

   `Something is 'here'...`
// ^^^^^^^^^^^^^^^^^^^^^^^^ .string.template.js
// ^ .punctuation.definition.string.begin.js
//                        ^ .punctuation.definition.string.end.js
   `Something is "here"...`
// ^^^^^^^^^^^^^^^^^^^^^^^^ .string.template.js
// ^ .punctuation.definition.string.begin.js
//                        ^ .punctuation.definition.string.end.js
   `Something is \`here\`...`
// ^^^^^^^^^^^^^^^^^^^^^^^^^^ .string.template.js
// ^ .punctuation.definition.string.begin.js
//               ^^ .constant.character.escape.a.js
//                     ^^ .constant.character.escape.b.js
//                          ^ .punctuation.definition.string.end.js
   `Escaped: \\\b\f\n\r\t\v\x12\u1234\u{1234}`
// ^^^^^^^^^^^^^^^^^^^^^^^^^ .string.template.js
// ^ .punctuation.definition.string.begin.js
//           ^^ .constant.character.escape.a.js
//             ^^ .constant.character.escape.b.js
//               ^^ .constant.character.escape.a.js
//                 ^^ .constant.character.escape.b.js
//                   ^^ .constant.character.escape.a.js
//                     ^^ .constant.character.escape.b.js
//                       ^^ .constant.character.escape.a.js
//                         ^^^^ .constant.character.escape.b.js
//                             ^^^^^^ .constant.character.escape.a.js
//                                   ^^^^^^^^ .constant.character.escape.b.js
//                                           ^ .punctuation.definition.string.end.js
   `Embedded variable ${variable}`
// ^^^^^^^^^^^^^^^^^^^ .string.template.js
// ^ .punctuation.definition.string.begin.js
//                    ^^ - string.template.js
//                    ^^ .keyword.operator.other.embedded-expression.begin.js
//                      ^^^^^^^^ .variable.other.readwrite.js
//                              ^ - string.template.js
//                              ^ .keyword.operator.other.embedded-expression.end.js
//                               ^ .string.template.js
//                               ^ .punctuation.definition.string.end.js
   `A${`B${`C`}`}`
// ^^ .string.template.js
// ^ .punctuation.definition.string.begin.js
//   ^^ - string.template.js
//   ^^ .keyword.operator.other.embedded-expression.begin.js
//     ^^ .string.template.js
//     ^ .punctuation.definition.string.begin.js
//       ^^ - string.template.js
//       ^^ .keyword.operator.other.embedded-expression.begin.js
//         ^^^ .string.template.js
//         ^ .punctuation.definition.string.begin.js
//           ^ .punctuation.definition.string.end.js
//            ^ - string.template.js
//            ^ .keyword.operator.other.embedded-expression.end.js
//             ^ .string.template.js
//             ^ .punctuation.definition.string.end.js
//              ^ - string.template.js
//              ^ .keyword.operator.other.embedded-expression.end.js
//               ^ .string.template.js
//               ^ .punctuation.definition.string.end.js
