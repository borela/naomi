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
// ^^^ .storage.type.js.fjsx15
// ^^^ .keyword.declaration.variable.js.fjsx15
//     ^^^^^^ .entity.name.variable.js.fjsx15
//            ^ .keyword.operator.other.assignment.js.fjsx15
//              ^ .punctuation.delimiter.object.begin.js.fjsx15
    property:123,
//  ^^^^^^^^ .entity.name.variable.js.fjsx15
//          ^ .object.js.fjsx15
//          ^ .keyword.operator.other.association.js.fjsx15
//           ^^^ .constant.numeric.decimal.js.fjsx15
//              ^ .punctuation.delimiter.object.js.fjsx15
    [property]:123,
//  ^ .punctuation.delimiter.object.computed-property.begin.js.fjsx15
//   ^^^^^^^^ .entity.name.variable.js.fjsx15
//           ^ .punctuation.delimiter.object.computed-property.end.js.fjsx15
//            ^ .keyword.operator.other.association.js.fjsx15
//             ^^^ .constant.numeric.decimal.js.fjsx15
//                ^ .punctuation.delimiter.object.js.fjsx15
    [1 + 1 + 1]:123,
//  ^ .punctuation.delimiter.object.computed-property.begin.js.fjsx15
//   ^ .constant.numeric.decimal.js.fjsx15
//     ^ .keyword.operator.arithmetic.js.fjsx15
//       ^ .constant.numeric.decimal.js.fjsx15
//         ^ .keyword.operator.arithmetic.js.fjsx15
//           ^ .constant.numeric.decimal.js.fjsx15
//            ^ .punctuation.delimiter.object.computed-property.end.js.fjsx15
//             ^ .keyword.operator.other.association.js.fjsx15
//              ^^^ .constant.numeric.decimal.js.fjsx15
//                 ^ .punctuation.delimiter.object.js.fjsx15
   };
// ^ .punctuation.delimiter.object.end.js.fjsx15
//  ^ .keyword.operator.other.terminator.js.fjsx15
   var object = {
// ^^^ .storage.type.js.fjsx15
// ^^^ .keyword.declaration.variable.js.fjsx15
//     ^^^^^^ .entity.name.variable.js.fjsx15
//            ^ .keyword.operator.other.assignment.js.fjsx15
//              ^ .punctuation.delimiter.object.begin.js.fjsx15
   @decorator
// ^ .punctuation.delimiter.decorator.js.fjsx15
//  ^^^^^^^^^ .entity.name.decorator.js.fjsx15
   @decorator(1,'2')
// ^ .punctuation.delimiter.decorator.js.fjsx15
//  ^^^^^^^^^ .entity.name.decorator.js.fjsx15
//           ^ .punctuation.delimiter.decorator.arguments.begin.js.fjsx15
//            ^ .constant.numeric.decimal.js.fjsx15
//             ^ .punctuation.delimiter.decorator.arguments.js.fjsx15
//              ^^^ .string.quoted.single.js.fjsx15
//              ^ .punctuation.delimiter.string.begin.js.fjsx15
//                ^ .punctuation.delimiter.string.end.js.fjsx15
//                 ^ .punctuation.delimiter.decorator.arguments.end.js.fjsx15
    constructor(){},
//  ^^^^^^^^^^^ .support.js.fjsx15
//  ^^^^^^^^^^^ .entity.name.function.js.fjsx15
//             ^ .punctuation.delimiter.function.parameters.begin.js.fjsx15
//              ^ .punctuation.delimiter.function.parameters.end.js.fjsx15
//               ^ .punctuation.delimiter.function.body.begin.js.fjsx15
//                ^ .punctuation.delimiter.function.body.end.js.fjsx15
//                 ^ .punctuation.delimiter.object.js.fjsx15
    method(){},
//  ^^^^^^ .entity.name.function.js.fjsx15
//        ^ .punctuation.delimiter.function.parameters.begin.js.fjsx15
//         ^ .punctuation.delimiter.function.parameters.end.js.fjsx15
//          ^ .punctuation.delimiter.function.body.begin.js.fjsx15
//           ^ .punctuation.delimiter.function.body.end.js.fjsx15
//            ^ .punctuation.delimiter.object.js.fjsx15
    *method(){},
//  ^ .storage.modifier.js.fjsx15
//  ^ .keyword.operator.other.generator.js.fjsx15
//   ^^^^^^ .entity.name.function.js.fjsx15
//         ^ .punctuation.delimiter.function.parameters.begin.js.fjsx15
//          ^ .punctuation.delimiter.function.parameters.end.js.fjsx15
//           ^ .punctuation.delimiter.function.body.begin.js.fjsx15
//            ^ .punctuation.delimiter.function.body.end.js.fjsx15
//             ^ .punctuation.delimiter.object.js.fjsx15
    get property(){},
//  ^^^ .storage.modifier.js.fjsx15
//  ^^^ .keyword.other.proxy.js.fjsx15
//      ^^^^^^^^ .entity.name.function.js.fjsx15
//              ^ .punctuation.delimiter.function.parameters.begin.js.fjsx15
//               ^ .punctuation.delimiter.function.parameters.end.js.fjsx15
//                ^ .punctuation.delimiter.function.body.begin.js.fjsx15
//                 ^ .punctuation.delimiter.function.body.end.js.fjsx15
//                  ^ .punctuation.delimiter.object.js.fjsx15
    set property(){},
//  ^^^ .storage.modifier.js.fjsx15
//  ^^^ .keyword.other.proxy.js.fjsx15
//      ^^^^^^^^ .entity.name.function.js.fjsx15
//              ^ .punctuation.delimiter.function.parameters.begin.js.fjsx15
//               ^ .punctuation.delimiter.function.parameters.end.js.fjsx15
//                ^ .punctuation.delimiter.function.body.begin.js.fjsx15
//                 ^ .punctuation.delimiter.function.body.end.js.fjsx15
//                  ^ .punctuation.delimiter.object.js.fjsx15
    async method(){},
//  ^^^^^ .storage.modifier.js.fjsx15
//  ^^^^^ .keyword.other.async.js.fjsx15
//        ^^^^^^ .entity.name.function.js.fjsx15
//              ^ .punctuation.delimiter.function.parameters.begin.js.fjsx15
//               ^ .punctuation.delimiter.function.parameters.end.js.fjsx15
//                ^ .punctuation.delimiter.function.body.begin.js.fjsx15
//                 ^ .punctuation.delimiter.function.body.end.js.fjsx15
//                  ^ .punctuation.delimiter.object.js.fjsx15
    static method(){},
//  ^^^^^^ .storage.modifier.js.fjsx15
//  ^^^^^^ .keyword.other.access.js.fjsx15
//         ^^^^^^ .entity.name.function.js.fjsx15
//               ^ .punctuation.delimiter.function.parameters.begin.js.fjsx15
//                ^ .punctuation.delimiter.function.parameters.end.js.fjsx15
//                 ^ .punctuation.delimiter.function.body.begin.js.fjsx15
//                  ^ .punctuation.delimiter.function.body.end.js.fjsx15
//                   ^ .punctuation.delimiter.object.js.fjsx15
    static get property(){},
//  ^^^^^^ .storage.modifier.js.fjsx15
//  ^^^^^^ .keyword.other.access.js.fjsx15
//         ^^^ .storage.modifier.js.fjsx15
//         ^^^ .keyword.other.proxy.js.fjsx15
//             ^^^^^^^^ .entity.name.function.js.fjsx15
//                     ^ .punctuation.delimiter.function.parameters.begin.js.fjsx15
//                      ^ .punctuation.delimiter.function.parameters.end.js.fjsx15
//                       ^ .punctuation.delimiter.function.body.begin.js.fjsx15
//                        ^ .punctuation.delimiter.function.body.end.js.fjsx15
//                         ^ .punctuation.delimiter.object.js.fjsx15
    static set property(){},
//  ^^^^^^ .storage.modifier.js.fjsx15
//  ^^^^^^ .keyword.other.access.js.fjsx15
//         ^^^ .storage.modifier.js.fjsx15
//         ^^^ .keyword.other.proxy.js.fjsx15
//             ^^^^^^^^ .entity.name.function.js.fjsx15
//                     ^ .punctuation.delimiter.function.parameters.begin.js.fjsx15
//                      ^ .punctuation.delimiter.function.parameters.end.js.fjsx15
//                       ^ .punctuation.delimiter.function.body.begin.js.fjsx15
//                        ^ .punctuation.delimiter.function.body.end.js.fjsx15
//                         ^ .punctuation.delimiter.object.js.fjsx15
    static async method(){},
//  ^^^^^^ .storage.modifier.js.fjsx15
//  ^^^^^^ .keyword.other.access.js.fjsx15
//         ^^^^^ .storage.modifier.js.fjsx15
//         ^^^^^ .keyword.other.async.js.fjsx15
//               ^^^^^^ .entity.name.function.js.fjsx15
//                     ^ .punctuation.delimiter.function.parameters.begin.js.fjsx15
//                      ^ .punctuation.delimiter.function.parameters.end.js.fjsx15
//                       ^ .punctuation.delimiter.function.body.begin.js.fjsx15
//                        ^ .punctuation.delimiter.function.body.end.js.fjsx15
//                         ^ .punctuation.delimiter.object.js.fjsx15
   };
// ^ .punctuation.delimiter.object.end.js.fjsx15
//  ^ .keyword.operator.other.terminator.js.fjsx15
