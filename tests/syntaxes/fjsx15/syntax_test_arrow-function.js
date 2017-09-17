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

   () => {}
// ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//  ^ .punctuation.definition.function.parameters.end.js.fjsx15
//    ^^ .punctuation.definition.function.body.arrow.js.fjsx15
//       ^ .punctuation.definition.function.body.begin.js.fjsx15
//        ^ .punctuation.definition.function.body.end.js.fjsx15
   async () => {}
// ^^^^^ .storage.modifier.js.fjsx15
// ^^^^^ .keyword.other.async.js.fjsx15
//       ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//        ^ .punctuation.definition.function.parameters.end.js.fjsx15
//          ^^ .punctuation.definition.function.body.arrow.js.fjsx15
//             ^ .punctuation.definition.function.body.begin.js.fjsx15
//              ^ .punctuation.definition.function.body.end.js.fjsx15
   (param, ...param) => {}
// ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//  ^^^^^ .entity.name.variable.js.fjsx15
//       ^ .punctuation.definition.function.parameters.js.fjsx15
//         ^^^ .keyword.operator.other.rest.js.fjsx15
//            ^^^^^ .entity.name.variable.js.fjsx15
//                 ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                   ^^ .punctuation.definition.function.body.arrow.js.fjsx15
//                      ^ .punctuation.definition.function.body.begin.js.fjsx15
//                       ^ .punctuation.definition.function.body.end.js.fjsx15
   async (param, ...param) => {}
// ^^^^^ .storage.modifier.js.fjsx15
// ^^^^^ .keyword.other.async.js.fjsx15
//       ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//        ^^^^^ .entity.name.variable.js.fjsx15
//             ^ .punctuation.definition.function.parameters.js.fjsx15
//               ^^^ .keyword.operator.other.rest.js.fjsx15
//                  ^^^^^ .entity.name.variable.js.fjsx15
//                       ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                         ^^ .punctuation.definition.function.body.arrow.js.fjsx15
//                            ^ .punctuation.definition.function.body.begin.js.fjsx15
//                             ^ .punctuation.definition.function.body.end.js.fjsx15
   (param:number, ...param:string):number => {}
// ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//  ^^^^^ .entity.name.variable.js.fjsx15
//       ^ .keyword.operator.other.association.flowtype
//        ^^^^^^ .support.flowtype
//        ^^^^^^ .entity.name.type.flowtype
//              ^ .punctuation.definition.function.parameters.js.fjsx15
//                ^^^ .keyword.operator.other.rest.js.fjsx15
//                   ^^^^^ .entity.name.variable.js.fjsx15
//                        ^ .keyword.operator.other.association.flowtype
//                         ^^^^^^ .support.flowtype
//                         ^^^^^^ .entity.name.type.flowtype
//                               ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                                ^ .keyword.operator.other.association.flowtype
//                                 ^^^^^^ .support.flowtype
//                                 ^^^^^^ .entity.name.type.flowtype
//                                        ^^ .punctuation.definition.function.body.arrow.js.fjsx15
//                                           ^ .punctuation.definition.function.body.begin.js.fjsx15
//                                            ^ .punctuation.definition.function.body.end.js.fjsx15
   async (param:number, ...param:string):number => {}
// ^^^^^ .storage.modifier.js.fjsx15
// ^^^^^ .keyword.other.async.js.fjsx15
//       ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//        ^^^^^ .entity.name.variable.js.fjsx15
//             ^ .keyword.operator.other.association.flowtype
//              ^^^^^^ .support.flowtype
//              ^^^^^^ .entity.name.type.flowtype
//                    ^ .punctuation.definition.function.parameters.js.fjsx15
//                      ^^^ .keyword.operator.other.rest.js.fjsx15
//                         ^^^^^ .entity.name.variable.js.fjsx15
//                              ^ .keyword.operator.other.association.flowtype
//                               ^^^^^^ .support.flowtype
//                               ^^^^^^ .entity.name.type.flowtype
//                                     ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                                      ^ .keyword.operator.other.association.flowtype
//                                       ^^^^^^ .support.flowtype
//                                       ^^^^^^ .entity.name.type.flowtype
//                                              ^^ .punctuation.definition.function.body.arrow.js.fjsx15
//                                                 ^ .punctuation.definition.function.body.begin.js.fjsx15
//                                                  ^ .punctuation.definition.function.body.end.js.fjsx15
   <A,B,C>(param:A, ...param:B):C => {}
// ^ .punctuation.definition.template.parameters.begin.flowtype
//  ^ .entity.name.type.flowtype
//   ^ .punctuation.definition.template.parameters.flowtype
//    ^ .entity.name.type.flowtype
//     ^ .punctuation.definition.template.parameters.flowtype
//      ^ .entity.name.type.flowtype
//       ^ .punctuation.definition.template.parameters.end.flowtype
//        ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//         ^^^^^ .entity.name.variable.js.fjsx15
//              ^ .keyword.operator.other.association.flowtype
//               ^ .entity.name.type.flowtype
//                ^ .punctuation.definition.function.parameters.js.fjsx15
//                  ^^^ .keyword.operator.other.rest.js.fjsx15
//                     ^^^^^ .entity.name.variable.js.fjsx15
//                          ^ .keyword.operator.other.association.flowtype
//                           ^ .entity.name.type.flowtype
//                            ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                             ^ .keyword.operator.other.association.flowtype
//                              ^ .entity.name.type.flowtype
//                                ^^ .punctuation.definition.function.body.arrow.js.fjsx15
//                                   ^ .punctuation.definition.function.body.begin.js.fjsx15
//                                    ^ .punctuation.definition.function.body.end.js.fjsx15
