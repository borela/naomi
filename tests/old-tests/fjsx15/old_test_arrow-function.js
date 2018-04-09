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

   () => {};
// ^ .punctuation.section.group.begin.js
//  ^ .punctuation.section.group.end.js
//    ^^ .punctuation.section.block.arrow.js
//       ^ .punctuation.section.block.begin.js
//        ^ .punctuation.section.block.end.js
//         ^ .punctuation.terminator.js
   async () => {};
// ^^^^^ .storage.modifier.js
// ^^^^^ .keyword.other.async.js
//       ^ .punctuation.section.group.begin.js
//        ^ .punctuation.section.group.end.js
//          ^^ .punctuation.section.block.arrow.js
//             ^ .punctuation.section.block.begin.js
//              ^ .punctuation.section.block.end.js
   (param, ...param) => {};
// ^ .punctuation.section.group.begin.js
//  ^^^^^ .variable.other.readwrite.js
//       ^ .punctuation.definition.function.parameters.js
//         ^^^ .keyword.operator.rest.js
//            ^^^^^ .variable.other.readwrite.js
//                 ^ .punctuation.section.group.end.js
//                   ^^ .punctuation.section.block.arrow.js
//                      ^ .punctuation.section.block.begin.js
//                       ^ .punctuation.section.block.end.js
   async (param, ...param) => {};
// ^^^^^ .storage.modifier.js
// ^^^^^ .keyword.other.async.js
//       ^ .punctuation.section.group.begin.js
//        ^^^^^ .variable.other.readwrite.js
//             ^ .punctuation.definition.function.parameters.js
//               ^^^ .keyword.operator.rest.js
//                  ^^^^^ .variable.other.readwrite.js
//                       ^ .punctuation.section.group.end.js
//                         ^^ .punctuation.section.block.arrow.js
//                            ^ .punctuation.section.block.begin.js
//                             ^ .punctuation.section.block.end.js
   (param:number, ...param:string):number => {};
// ^ .punctuation.section.group.begin.js
//  ^^^^^ .variable.other.readwrite.js
//       ^ .punctuation.binding.flow
//        ^^^^^^ .support.type.primitive.flow
//        ^^^^^^ .entity.name.type.flow
//              ^ .punctuation.definition.function.parameters.js
//                ^^^ .keyword.operator.rest.js
//                   ^^^^^ .variable.other.readwrite.js
//                        ^ .punctuation.binding.flow
//                         ^^^^^^ .support.type.primitive.flow
//                         ^^^^^^ .entity.name.type.flow
//                               ^ .punctuation.section.group.end.js
//                                ^ .punctuation.binding.flow
//                                 ^^^^^^ .support.type.primitive.flow
//                                 ^^^^^^ .entity.name.type.flow
//                                        ^^ .punctuation.section.block.arrow.js
//                                           ^ .punctuation.section.block.begin.js
//                                            ^ .punctuation.section.block.end.js
   async (param:number, ...param:string):number => {};
// ^^^^^ .storage.modifier.js
// ^^^^^ .keyword.other.async.js
//       ^ .punctuation.section.group.begin.js
//        ^^^^^ .variable.other.readwrite.js
//             ^ .punctuation.binding.flow
//              ^^^^^^ .support.type.primitive.flow
//              ^^^^^^ .entity.name.type.flow
//                    ^ .punctuation.definition.function.parameters.js
//                      ^^^ .keyword.operator.rest.js
//                         ^^^^^ .variable.other.readwrite.js
//                              ^ .punctuation.binding.flow
//                               ^^^^^^ .support.type.primitive.flow
//                               ^^^^^^ .entity.name.type.flow
//                                     ^ .punctuation.section.group.end.js
//                                      ^ .punctuation.binding.flow
//                                       ^^^^^^ .support.type.primitive.flow
//                                       ^^^^^^ .entity.name.type.flow
//                                              ^^ .punctuation.section.block.arrow.js
//                                                 ^ .punctuation.section.block.begin.js
//                                                  ^ .punctuation.section.block.end.js
   <A,B,C>(param:A, ...param:B):C => {};
// ^ .punctuation.definition.template.parameters.begin.flow
//  ^ .entity.name.type.flow
//   ^ .punctuation.definition.template.parameters.flow
//    ^ .entity.name.type.flow
//     ^ .punctuation.definition.template.parameters.flow
//      ^ .entity.name.type.flow
//       ^ .punctuation.definition.template.parameters.end.flow
//        ^ .punctuation.section.group.begin.js
//         ^^^^^ .variable.other.readwrite.js
//              ^ .punctuation.binding.flow
//               ^ .entity.name.type.flow
//                ^ .punctuation.definition.function.parameters.js
//                  ^^^ .keyword.operator.rest.js
//                     ^^^^^ .variable.other.readwrite.js
//                          ^ .punctuation.binding.flow
//                           ^ .entity.name.type.flow
//                            ^ .punctuation.section.group.end.js
//                             ^ .punctuation.binding.flow
//                              ^ .entity.name.type.flow
//                                ^^ .punctuation.section.block.arrow.js
//                                   ^ .punctuation.section.block.begin.js
//                                    ^ .punctuation.section.block.end.js
