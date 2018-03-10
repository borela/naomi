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
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//            ^ .keyword.operator.other.assignment.flow
//              ^^^^^^^^ .entity.name.type.flow
//                      ^ .punctuation.terminator.js
   type Alias = SomeType[];
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//            ^ .keyword.operator.other.assignment.flow
//              ^^^^^^^^ .entity.name.type.flow
//                      ^ .punctuation.definition.array.begin.flow
//                       ^ .punctuation.definition.array.end.flow
//                        ^ .punctuation.terminator.js
   type Alias = SomeType<number>;
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//            ^ .keyword.operator.other.assignment.flow
//              ^^^^^^^^ .entity.name.type.flow
//                      ^ .punctuation.section.generic.begin.flow
//                       ^^^^^^ .support.type.primitive.flow
//                       ^^^^^^ .entity.name.type.flow
//                             ^ .punctuation.section.generic.end.flow
//                              ^ .punctuation.terminator.js
   type Alias = SomeType<number[]>;
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//            ^ .keyword.operator.other.assignment.flow
//              ^^^^^^^^ .entity.name.type.flow
//                      ^ .punctuation.section.generic.begin.flow
//                       ^^^^^^ .support.type.primitive.flow
//                       ^^^^^^ .entity.name.type.flow
//                             ^ .punctuation.definition.array.begin.flow
//                              ^ .punctuation.definition.array.end.flow
//                               ^ .punctuation.section.generic.end.flow
//                                ^ .punctuation.terminator.js
   type Alias = (param:number) => number;
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//            ^ .keyword.operator.other.assignment.flow
//              ^ .punctuation.section.group.begin.flow
//               ^^^^^ .variable.other.readwrite.js
//                    ^ .punctuation.binding.flow
//                     ^^^^^^ .support.type.primitive.flow
//                     ^^^^^^ .entity.name.type.flow
//                           ^ .punctuation.section.group.end.flow
//                             ^^ .punctuation.definition.function.result.flow
//                                ^^^^^^ .support.type.primitive.flow
//                                ^^^^^^ .entity.name.type.flow
//                                      ^ .punctuation.terminator.js
   type Alias = (param:number, param:string) => number;
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//            ^ .keyword.operator.other.assignment.flow
//              ^ .punctuation.section.group.begin.flow
//               ^^^^^ .variable.other.readwrite.js
//                    ^ .punctuation.binding.flow
//                     ^^^^^^ .support.type.primitive.flow
//                     ^^^^^^ .entity.name.type.flow
//                           ^ .punctuation.definition.function.parameters.flow
//                             ^^^^^ .variable.other.readwrite.js
//                                  ^ .punctuation.binding.flow
//                                   ^^^^^^ .support.type.primitive.flow
//                                   ^^^^^^ .entity.name.type.flow
//                                         ^ .punctuation.section.group.end.flow
//                                           ^^ .punctuation.definition.function.result.flow
//                                              ^^^^^^ .support.type.primitive.flow
//                                              ^^^^^^ .entity.name.type.flow
//                                                    ^ .punctuation.terminator.js
   type Alias<A,B,C> = (param:A, param:B) => C;
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//           ^ .punctuation.section.generic.begin.flow
//            ^ .entity.name.type.flow
//             ^ .punctuation.separator.comma.flow
//              ^ .entity.name.type.flow
//               ^ .punctuation.separator.comma.flow
//                ^ .entity.name.type.flow
//                 ^ .punctuation.section.generic.end.flow
//                   ^ .keyword.operator.other.assignment.flow
//                     ^ .punctuation.section.group.begin.flow
//                      ^^^^^ .variable.other.readwrite.js
//                           ^ .punctuation.binding.flow
//                            ^ .entity.name.type.flow
//                             ^ .punctuation.definition.function.parameters.flow
//                               ^^^^^ .variable.other.readwrite.js
//                                    ^ .punctuation.binding.flow
//                                     ^ .entity.name.type.flow
//                                      ^ .punctuation.section.group.end.flow
//                                        ^^ .punctuation.definition.function.result.flow
//                                           ^ .entity.name.type.flow
//                                            ^ .punctuation.terminator.js
   type Alias<A,B,C> = (param:A|B, param:B) => C|B;
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//           ^ .punctuation.section.generic.begin.flow
//            ^ .entity.name.type.flow
//             ^ .punctuation.separator.comma.flow
//              ^ .entity.name.type.flow
//               ^ .punctuation.separator.comma.flow
//                ^ .entity.name.type.flow
//                 ^ .punctuation.section.generic.end.flow
//                   ^ .keyword.operator.other.assignment.flow
//                     ^ .punctuation.section.group.begin.flow
//                      ^^^^^ .variable.other.readwrite.js
//                           ^ .punctuation.binding.flow
//                            ^ .entity.name.type.flow
//                             ^ .keyword.operator.other.union.flow
//                              ^ .entity.name.type.flow
//                               ^ .punctuation.definition.function.parameters.flow
//                                 ^^^^^ .variable.other.readwrite.js
//                                      ^ .punctuation.binding.flow
//                                       ^ .entity.name.type.flow
//                                        ^ .punctuation.section.group.end.flow
//                                          ^^ .punctuation.definition.function.result.flow
//                                             ^ .entity.name.type.flow
//                                              ^ .keyword.operator.other.union.flow
//                                               ^ .entity.name.type.flow
//                                                ^ .punctuation.terminator.js
   type Alias<A,B,C> = (param:?(A|B), param:?B) => ?C;
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//           ^ .punctuation.section.generic.begin.flow
//            ^ .entity.name.type.flow
//             ^ .punctuation.separator.comma.flow
//              ^ .entity.name.type.flow
//               ^ .punctuation.separator.comma.flow
//                ^ .entity.name.type.flow
//                 ^ .punctuation.section.generic.end.flow
//                   ^ .keyword.operator.other.assignment.flow
//                     ^ .punctuation.section.group.begin.flow
//                      ^^^^^ .variable.other.readwrite.js
//                           ^ .punctuation.binding.flow
//                            ^ .keyword.operator.other.nullable.flow
//                             ^ .punctuation.definition.nullable.begin.flow
//                              ^ .entity.name.type.flow
//                               ^ .keyword.operator.other.union.flow
//                                ^ .entity.name.type.flow
//                                 ^ .punctuation.definition.nullable.end.flow
//                                  ^ .punctuation.definition.function.parameters.flow
//                                    ^^^^^ .variable.other.readwrite.js
//                                         ^ .punctuation.binding.flow
//                                          ^ .keyword.operator.other.nullable.flow
//                                           ^ .entity.name.type.flow
//                                            ^ .punctuation.section.group.end.flow
//                                              ^^ .punctuation.definition.function.result.flow
//                                                 ^ .keyword.operator.other.nullable.flow
//                                                  ^ .entity.name.type.flow
//                                                   ^ .punctuation.terminator.js
   type Alias<A,B> = {a:?A, b:?B};
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//           ^ .punctuation.section.generic.begin.flow
//            ^ .entity.name.type.flow
//             ^ .punctuation.separator.comma.flow
//              ^ .entity.name.type.flow
//               ^ .punctuation.section.generic.end.flow
//                 ^ .keyword.operator.other.assignment.flow
//                   ^ .punctuation.section.block.begin.flow
//                    ^ .variable.other.readwrite.js
//                     ^ .punctuation.binding.flow
//                      ^ .keyword.operator.other.nullable.flow
//                       ^ .entity.name.type.flow
//                        ^ .punctuation.separator.comma.flow
//                          ^ .variable.other.readwrite.js
//                           ^ .punctuation.binding.flow
//                            ^ .keyword.operator.other.nullable.flow
//                             ^ .entity.name.type.flow
//                              ^ .punctuation.section.block.end.flow
//                               ^ .punctuation.terminator.js
   type Alias<A,B,C> = {a:?(A|C), b:?B};
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//           ^ .punctuation.section.generic.begin.flow
//            ^ .entity.name.type.flow
//             ^ .punctuation.separator.comma.flow
//              ^ .entity.name.type.flow
//               ^ .punctuation.separator.comma.flow
//                ^ .entity.name.type.flow
//                 ^ .punctuation.section.generic.end.flow
//                   ^ .keyword.operator.other.assignment.flow
//                     ^ .punctuation.section.block.begin.flow
//                      ^ .variable.other.readwrite.js
//                       ^ .punctuation.binding.flow
//                        ^ .keyword.operator.other.nullable.flow
//                         ^ .punctuation.definition.nullable.begin.flow
//                          ^ .entity.name.type.flow
//                           ^ .keyword.operator.other.union.flow
//                            ^ .entity.name.type.flow
//                             ^ .punctuation.definition.nullable.end.flow
//                              ^ .punctuation.separator.comma.flow
//                                ^ .variable.other.readwrite.js
//                                 ^ .punctuation.binding.flow
//                                  ^ .keyword.operator.other.nullable.flow
//                                   ^ .entity.name.type.flow
//                                    ^ .punctuation.section.block.end.flow
//                                     ^ .punctuation.terminator.js
   type Alias<A,B> = {a:A} & {b:B};
// ^^^^ .keyword.declaration.type-aliasing.flow
//      ^^^^^ .entity.name.type.flow
//           ^ .punctuation.section.generic.begin.flow
//            ^ .entity.name.type.flow
//             ^ .punctuation.separator.comma.flow
//              ^ .entity.name.type.flow
//               ^ .punctuation.section.generic.end.flow
//                 ^ .keyword.operator.other.assignment.flow
//                   ^ .punctuation.section.block.begin.flow
//                    ^ .variable.other.readwrite.js
//                     ^ .punctuation.binding.flow
//                      ^ .entity.name.type.flow
//                       ^ .punctuation.section.block.end.flow
//                         ^ .keyword.operator.other.intersection.flow
//                           ^ .punctuation.section.block.begin.flow
//                            ^ .variable.other.readwrite.js
//                             ^ .punctuation.binding.flow
//                              ^ .entity.name.type.flow
//                               ^ .punctuation.section.block.end.flow
//                                ^ .punctuation.terminator.js
