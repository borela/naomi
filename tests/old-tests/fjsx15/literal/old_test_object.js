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

   var object = {
// ^^^ .storage.type.js
//     ^^^^^^ .variable.other.readwrite.js
//            ^ .keyword.operator.other.assignment.js
//              ^ .punctuation.section.block.begin.js
    property:123,
//  ^^^^^^^^ .variable.other.readwrite.js
//          ^ .object.js
//          ^ .punctuation.binding.js
//           ^^^ .constant.numeric.decimal.js
//              ^ .punctuation.separator.comma.js
    [property]:123,
//  ^ .punctuation.section.brackets.begin.js
//   ^^^^^^^^ .variable.other.readwrite.js
//           ^ .punctuation.section.brackets.end.js
//            ^ .punctuation.binding.js
//             ^^^ .constant.numeric.decimal.js
//                ^ .punctuation.separator.comma.js
    [1 + 1 + 1]:123,
//  ^ .punctuation.section.brackets.begin.js
//   ^ .constant.numeric.decimal.js
//     ^ .keyword.operator.arithmetic.js
//       ^ .constant.numeric.decimal.js
//         ^ .keyword.operator.arithmetic.js
//           ^ .constant.numeric.decimal.js
//            ^ .punctuation.section.brackets.end.js
//             ^ .punctuation.binding.js
//              ^^^ .constant.numeric.decimal.js
//                 ^ .punctuation.separator.comma.js
   };
// ^ .punctuation.section.block.end.js
//  ^ .punctuation.terminator.js
   var object = {
// ^^^ .storage.type.js
//     ^^^^^^ .variable.other.readwrite.js
//            ^ .keyword.operator.other.assignment.js
//              ^ .punctuation.section.block.begin.js
   @decorator
// ^ .punctuation.definition.decorator.js
//  ^^^^^^^^^ .entity.name.decorator.js
   @decorator(1,'2')
// ^ .punctuation.definition.decorator.js
//  ^^^^^^^^^ .entity.name.decorator.js
//           ^ .punctuation.definition.decorator.arguments.begin.js
//            ^ .constant.numeric.decimal.js
//             ^ .punctuation.definition.decorator.arguments.js
//              ^^^ .string.quoted.single.js
//              ^ .punctuation.definition.string.begin.js
//                ^ .punctuation.definition.string.end.js
//                 ^ .punctuation.definition.decorator.arguments.end.js
    constructor(){},
//  ^^^^^^^^^^^ .support.js
//  ^^^^^^^^^^^ .entity.name.function.js
//             ^ .punctuation.section.group.begin.js
//              ^ .punctuation.section.group.end.js
//               ^ .punctuation.section.block.begin.js
//                ^ .punctuation.section.block.end.js
//                 ^ .punctuation.separator.comma.js
    method(){},
//  ^^^^^^ .entity.name.function.js
//        ^ .punctuation.section.group.begin.js
//         ^ .punctuation.section.group.end.js
//          ^ .punctuation.section.block.begin.js
//           ^ .punctuation.section.block.end.js
//            ^ .punctuation.separator.comma.js
    *method(){},
//  ^ .storage.modifier.js
//   ^^^^^^ .entity.name.function.js
//         ^ .punctuation.section.group.begin.js
//          ^ .punctuation.section.group.end.js
//           ^ .punctuation.section.block.begin.js
//            ^ .punctuation.section.block.end.js
//             ^ .punctuation.separator.comma.js
    get property(){},
//  ^^^ .storage.modifier.js
//      ^^^^^^^^ .entity.name.function.js
//              ^ .punctuation.section.group.begin.js
//               ^ .punctuation.section.group.end.js
//                ^ .punctuation.section.block.begin.js
//                 ^ .punctuation.section.block.end.js
//                  ^ .punctuation.separator.comma.js
    set property(){},
//  ^^^ .storage.modifier.js
//      ^^^^^^^^ .entity.name.function.js
//              ^ .punctuation.section.group.begin.js
//               ^ .punctuation.section.group.end.js
//                ^ .punctuation.section.block.begin.js
//                 ^ .punctuation.section.block.end.js
//                  ^ .punctuation.separator.comma.js
    async method(){},
//  ^^^^^ .storage.modifier.js
//        ^^^^^^ .entity.name.function.js
//              ^ .punctuation.section.group.begin.js
//               ^ .punctuation.section.group.end.js
//                ^ .punctuation.section.block.begin.js
//                 ^ .punctuation.section.block.end.js
//                  ^ .punctuation.separator.comma.js
    static method(){},
//  ^^^^^^ .storage.modifier.js
//         ^^^^^^ .entity.name.function.js
//               ^ .punctuation.section.group.begin.js
//                ^ .punctuation.section.group.end.js
//                 ^ .punctuation.section.block.begin.js
//                  ^ .punctuation.section.block.end.js
//                   ^ .punctuation.separator.comma.js
    static get property(){},
//  ^^^^^^ .storage.modifier.js
//         ^^^ .storage.modifier.js
//             ^^^^^^^^ .entity.name.function.js
//                     ^ .punctuation.section.group.begin.js
//                      ^ .punctuation.section.group.end.js
//                       ^ .punctuation.section.block.begin.js
//                        ^ .punctuation.section.block.end.js
//                         ^ .punctuation.separator.comma.js
    static set property(){},
//  ^^^^^^ .storage.modifier.js
//         ^^^ .storage.modifier.js
//             ^^^^^^^^ .entity.name.function.js
//                     ^ .punctuation.section.group.begin.js
//                      ^ .punctuation.section.group.end.js
//                       ^ .punctuation.section.block.begin.js
//                        ^ .punctuation.section.block.end.js
//                         ^ .punctuation.separator.comma.js
    static async method(){},
//  ^^^^^^ .storage.modifier.js
//         ^^^^^ .storage.modifier.js
//               ^^^^^^ .entity.name.function.js
//                     ^ .punctuation.section.group.begin.js
//                      ^ .punctuation.section.group.end.js
//                       ^ .punctuation.section.block.begin.js
//                        ^ .punctuation.section.block.end.js
//                         ^ .punctuation.separator.comma.js
   };
// ^ .punctuation.section.block.end.js
//  ^ .punctuation.terminator.js
