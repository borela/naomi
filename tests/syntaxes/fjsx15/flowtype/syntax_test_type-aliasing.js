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

   type Alias = SomeType;
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//            ^ .keyword.operator.other.assignment.flowtype
//              ^^^^^^^^ .entity.name.type.flowtype
//                      ^ .keyword.other.terminator.js.fjsx15
   type Alias = SomeType[];
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//            ^ .keyword.operator.other.assignment.flowtype
//              ^^^^^^^^ .entity.name.type.flowtype
//                      ^ .punctuation.definition.array.begin.flowtype
//                       ^ .punctuation.definition.array.end.flowtype
//                        ^ .keyword.other.terminator.js.fjsx15
   type Alias = SomeType<number>;
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//            ^ .keyword.operator.other.assignment.flowtype
//              ^^^^^^^^ .entity.name.type.flowtype
//                      ^ .punctuation.definition.template.arguments.begin.flowtype
//                       ^^^^^^ .support.flowtype
//                       ^^^^^^ .entity.name.type.flowtype
//                             ^ .punctuation.definition.template.arguments.end.flowtype
//                              ^ .keyword.other.terminator.js.fjsx15
   type Alias = SomeType<number[]>;
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//            ^ .keyword.operator.other.assignment.flowtype
//              ^^^^^^^^ .entity.name.type.flowtype
//                      ^ .punctuation.definition.template.arguments.begin.flowtype
//                       ^^^^^^ .support.flowtype
//                       ^^^^^^ .entity.name.type.flowtype
//                             ^ .punctuation.definition.array.begin.flowtype
//                              ^ .punctuation.definition.array.end.flowtype
//                               ^ .punctuation.definition.template.arguments.end.flowtype
//                                ^ .keyword.other.terminator.js.fjsx15
   type Alias = (param:number) => number;
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//            ^ .keyword.operator.other.assignment.flowtype
//              ^ .punctuation.definition.function.parameters.begin.flowtype
//               ^^^^^ .entity.name.variable.js.fjsx15
//                    ^ .keyword.operator.other.association.flowtype
//                     ^^^^^^ .support.flowtype
//                     ^^^^^^ .entity.name.type.flowtype
//                           ^ .punctuation.definition.function.parameters.end.flowtype
//                             ^^ .punctuation.definition.function.result.flowtype
//                                ^^^^^^ .support.flowtype
//                                ^^^^^^ .entity.name.type.flowtype
//                                      ^ .keyword.other.terminator.js.fjsx15
   type Alias = (param:number, param:string) => number;
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//            ^ .keyword.operator.other.assignment.flowtype
//              ^ .punctuation.definition.function.parameters.begin.flowtype
//               ^^^^^ .entity.name.variable.js.fjsx15
//                    ^ .keyword.operator.other.association.flowtype
//                     ^^^^^^ .support.flowtype
//                     ^^^^^^ .entity.name.type.flowtype
//                           ^ .punctuation.definition.function.parameters.flowtype
//                             ^^^^^ .entity.name.variable.js.fjsx15
//                                  ^ .keyword.operator.other.association.flowtype
//                                   ^^^^^^ .support.flowtype
//                                   ^^^^^^ .entity.name.type.flowtype
//                                         ^ .punctuation.definition.function.parameters.end.flowtype
//                                           ^^ .punctuation.definition.function.result.flowtype
//                                              ^^^^^^ .support.flowtype
//                                              ^^^^^^ .entity.name.type.flowtype
//                                                    ^ .keyword.other.terminator.js.fjsx15
   type Alias<A,B,C> = (param:A, param:B) => C;
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//           ^ .punctuation.definition.template.arguments.begin.flowtype
//            ^ .entity.name.type.flowtype
//             ^ .punctuation.definition.template.arguments.flowtype
//              ^ .entity.name.type.flowtype
//               ^ .punctuation.definition.template.arguments.flowtype
//                ^ .entity.name.type.flowtype
//                 ^ .punctuation.definition.template.arguments.end.flowtype
//                   ^ .keyword.operator.other.assignment.flowtype
//                     ^ .punctuation.definition.function.parameters.begin.flowtype
//                      ^^^^^ .entity.name.variable.js.fjsx15
//                           ^ .keyword.operator.other.association.flowtype
//                            ^ .entity.name.type.flowtype
//                             ^ .punctuation.definition.function.parameters.flowtype
//                               ^^^^^ .entity.name.variable.js.fjsx15
//                                    ^ .keyword.operator.other.association.flowtype
//                                     ^ .entity.name.type.flowtype
//                                      ^ .punctuation.definition.function.parameters.end.flowtype
//                                        ^^ .punctuation.definition.function.result.flowtype
//                                           ^ .entity.name.type.flowtype
//                                            ^ .keyword.other.terminator.js.fjsx15
   type Alias<A,B,C> = (param:A|B, param:B) => C|B;
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//           ^ .punctuation.definition.template.arguments.begin.flowtype
//            ^ .entity.name.type.flowtype
//             ^ .punctuation.definition.template.arguments.flowtype
//              ^ .entity.name.type.flowtype
//               ^ .punctuation.definition.template.arguments.flowtype
//                ^ .entity.name.type.flowtype
//                 ^ .punctuation.definition.template.arguments.end.flowtype
//                   ^ .keyword.operator.other.assignment.flowtype
//                     ^ .punctuation.definition.function.parameters.begin.flowtype
//                      ^^^^^ .entity.name.variable.js.fjsx15
//                           ^ .keyword.operator.other.association.flowtype
//                            ^ .entity.name.type.flowtype
//                             ^ .keyword.operator.other.union.flowtype
//                              ^ .entity.name.type.flowtype
//                               ^ .punctuation.definition.function.parameters.flowtype
//                                 ^^^^^ .entity.name.variable.js.fjsx15
//                                      ^ .keyword.operator.other.association.flowtype
//                                       ^ .entity.name.type.flowtype
//                                        ^ .punctuation.definition.function.parameters.end.flowtype
//                                          ^^ .punctuation.definition.function.result.flowtype
//                                             ^ .entity.name.type.flowtype
//                                              ^ .keyword.operator.other.union.flowtype
//                                               ^ .entity.name.type.flowtype
//                                                ^ .keyword.other.terminator.js.fjsx15
   type Alias<A,B,C> = (param:?(A|B), param:?B) => ?C;
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//           ^ .punctuation.definition.template.arguments.begin.flowtype
//            ^ .entity.name.type.flowtype
//             ^ .punctuation.definition.template.arguments.flowtype
//              ^ .entity.name.type.flowtype
//               ^ .punctuation.definition.template.arguments.flowtype
//                ^ .entity.name.type.flowtype
//                 ^ .punctuation.definition.template.arguments.end.flowtype
//                   ^ .keyword.operator.other.assignment.flowtype
//                     ^ .punctuation.definition.function.parameters.begin.flowtype
//                      ^^^^^ .entity.name.variable.js.fjsx15
//                           ^ .keyword.operator.other.association.flowtype
//                            ^ .keyword.operator.other.nullable.flowtype
//                             ^ .punctuation.definition.nullable.begin.flowtype
//                              ^ .entity.name.type.flowtype
//                               ^ .keyword.operator.other.union.flowtype
//                                ^ .entity.name.type.flowtype
//                                 ^ .punctuation.definition.nullable.end.flowtype
//                                  ^ .punctuation.definition.function.parameters.flowtype
//                                    ^^^^^ .entity.name.variable.js.fjsx15
//                                         ^ .keyword.operator.other.association.flowtype
//                                          ^ .keyword.operator.other.nullable.flowtype
//                                           ^ .entity.name.type.flowtype
//                                            ^ .punctuation.definition.function.parameters.end.flowtype
//                                              ^^ .punctuation.definition.function.result.flowtype
//                                                 ^ .keyword.operator.other.nullable.flowtype
//                                                  ^ .entity.name.type.flowtype
//                                                   ^ .keyword.other.terminator.js.fjsx15
   type Alias<A,B> = {a:?A, b:?B};
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//           ^ .punctuation.definition.template.arguments.begin.flowtype
//            ^ .entity.name.type.flowtype
//             ^ .punctuation.definition.template.arguments.flowtype
//              ^ .entity.name.type.flowtype
//               ^ .punctuation.definition.template.arguments.end.flowtype
//                 ^ .keyword.operator.other.assignment.flowtype
//                   ^ .punctuation.definition.object.begin.flowtype
//                    ^ .entity.name.variable.js.fjsx15
//                     ^ .keyword.operator.other.association.flowtype
//                      ^ .keyword.operator.other.nullable.flowtype
//                       ^ .entity.name.type.flowtype
//                        ^ .punctuation.definition.object.flowtype
//                          ^ .entity.name.variable.js.fjsx15
//                           ^ .keyword.operator.other.association.flowtype
//                            ^ .keyword.operator.other.nullable.flowtype
//                             ^ .entity.name.type.flowtype
//                              ^ .punctuation.definition.object.end.flowtype
//                               ^ .keyword.other.terminator.js.fjsx15
   type Alias<A,B,C> = {a:?(A|C), b:?B};
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//           ^ .punctuation.definition.template.arguments.begin.flowtype
//            ^ .entity.name.type.flowtype
//             ^ .punctuation.definition.template.arguments.flowtype
//              ^ .entity.name.type.flowtype
//               ^ .punctuation.definition.template.arguments.flowtype
//                ^ .entity.name.type.flowtype
//                 ^ .punctuation.definition.template.arguments.end.flowtype
//                   ^ .keyword.operator.other.assignment.flowtype
//                     ^ .punctuation.definition.object.begin.flowtype
//                      ^ .entity.name.variable.js.fjsx15
//                       ^ .keyword.operator.other.association.flowtype
//                        ^ .keyword.operator.other.nullable.flowtype
//                         ^ .punctuation.definition.nullable.begin.flowtype
//                          ^ .entity.name.type.flowtype
//                           ^ .keyword.operator.other.union.flowtype
//                            ^ .entity.name.type.flowtype
//                             ^ .punctuation.definition.nullable.end.flowtype
//                              ^ .punctuation.definition.object.flowtype
//                                ^ .entity.name.variable.js.fjsx15
//                                 ^ .keyword.operator.other.association.flowtype
//                                  ^ .keyword.operator.other.nullable.flowtype
//                                   ^ .entity.name.type.flowtype
//                                    ^ .punctuation.definition.object.end.flowtype
//                                     ^ .keyword.other.terminator.js.fjsx15
   type Alias<A,B> = {a:A} & {b:B};
// ^^^^ .keyword.declaration.type-aliasing.flowtype
//      ^^^^^ .entity.name.type.flowtype
//           ^ .punctuation.definition.template.arguments.begin.flowtype
//            ^ .entity.name.type.flowtype
//             ^ .punctuation.definition.template.arguments.flowtype
//              ^ .entity.name.type.flowtype
//               ^ .punctuation.definition.template.arguments.end.flowtype
//                 ^ .keyword.operator.other.assignment.flowtype
//                   ^ .punctuation.definition.object.begin.flowtype
//                    ^ .entity.name.variable.js.fjsx15
//                     ^ .keyword.operator.other.association.flowtype
//                      ^ .entity.name.type.flowtype
//                       ^ .punctuation.definition.object.end.flowtype
//                         ^ .keyword.operator.other.intersection.flowtype
//                           ^ .punctuation.definition.object.begin.flowtype
//                            ^ .entity.name.variable.js.fjsx15
//                             ^ .keyword.operator.other.association.flowtype
//                              ^ .entity.name.type.flowtype
//                               ^ .punctuation.definition.object.end.flowtype
//                                ^ .keyword.other.terminator.js.fjsx15
