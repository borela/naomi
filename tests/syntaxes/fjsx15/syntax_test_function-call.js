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

   super(1,2);
// ^^^^^ support.js.fjsx15
// ^^^^^ entity.name.function.js.fjsx15
//      ^ punctuation.delimiter.function.arguments.begin.js.fjsx15
//       ^ constant.numeric.decimal.js.fjsx15
//        ^ punctuation.delimiter.function.arguments.js.fjsx15
//         ^ constant.numeric.decimal.js.fjsx15
//          ^ punctuation.delimiter.function.arguments.end.js.fjsx15
//           ^ keyword.operator.other.terminator.js.fjsx15
   foo<A,B>(1,2);
// ^^^ entity.name.function.js.fjsx15
//    ^ punctuation.delimiter.template.arguments.begin.flowtype
//     ^ entity.name.type.flowtype
//      ^ punctuation.delimiter.template.arguments.flowtype
//       ^ entity.name.type.flowtype
//        ^ punctuation.delimiter.template.arguments.end.flowtype
//         ^ punctuation.delimiter.function.arguments.begin.js.fjsx15
//          ^ constant.numeric.decimal.js.fjsx15
//           ^ punctuation.delimiter.function.arguments.js.fjsx15
//            ^ constant.numeric.decimal.js.fjsx15
//             ^ punctuation.delimiter.function.arguments.end.js.fjsx15
//              ^ keyword.operator.other.terminator.js.fjsx15
   foo<A|B>(1,2);
// ^^^ entity.name.function.js.fjsx15
//    ^ punctuation.delimiter.template.arguments.begin.flowtype
//     ^ entity.name.type.flowtype
//      ^ keyword.operator.other.union.flowtype
//       ^ entity.name.type.flowtype
//        ^ punctuation.delimiter.template.arguments.end.flowtype
//         ^ punctuation.delimiter.function.arguments.begin.js.fjsx15
//          ^ constant.numeric.decimal.js.fjsx15
//           ^ punctuation.delimiter.function.arguments.js.fjsx15
//            ^ constant.numeric.decimal.js.fjsx15
//             ^ punctuation.delimiter.function.arguments.end.js.fjsx15
//              ^ keyword.operator.other.terminator.js.fjsx15
   foo<{a:A} & {b:B}>(1,2);
// ^^^ entity.name.function.js.fjsx15
//    ^ punctuation.delimiter.template.arguments.begin.flowtype
//     ^ punctuation.delimiter.object.begin.flowtype
//      ^ entity.name.variable.js.fjsx15
//       ^ keyword.operator.other.association.flowtype
//        ^ entity.name.type.flowtype
//         ^ punctuation.delimiter.object.end.flowtype
//           ^ keyword.operator.other.intersection.flowtype
//             ^ punctuation.delimiter.object.begin.flowtype
//              ^ entity.name.variable.js.fjsx15
//               ^ keyword.operator.other.association.flowtype
//                ^ entity.name.type.flowtype
//                 ^ punctuation.delimiter.object.end.flowtype
//                  ^ punctuation.delimiter.template.arguments.end.flowtype
//                   ^ punctuation.delimiter.function.arguments.begin.js.fjsx15
//                    ^ constant.numeric.decimal.js.fjsx15
//                     ^ punctuation.delimiter.function.arguments.js.fjsx15
//                      ^ constant.numeric.decimal.js.fjsx15
//                       ^ punctuation.delimiter.function.arguments.end.js.fjsx15
//                        ^ keyword.operator.other.terminator.js.fjsx15
