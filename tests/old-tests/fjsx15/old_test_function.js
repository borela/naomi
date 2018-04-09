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

   function foo() {}
// ^^^^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^^^ .entity.name.function.js
//             ^ .punctuation.section.group.begin.js
//              ^ .punctuation.section.group.end.js
//                ^ .punctuation.section.block.begin.js
//                 ^ .punctuation.section.block.end.js
   function *foo() {}
// ^^^^^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^ .storage.modifier.js
//           ^^^ .entity.name.function.js
//              ^ .punctuation.section.group.begin.js
//               ^ .punctuation.section.group.end.js
//                 ^ .punctuation.section.block.begin.js
//                  ^ .punctuation.section.block.end.js
   function foo(param, ...param) {}
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^^^ .entity.name.function.js
//             ^ .punctuation.section.group.begin.js
//              ^^^^^ .variable.parameter.function.js
//                   ^ .punctuation.definition.function.parameters.js
//                     ^^^ .keyword.operator.rest.js
//                        ^^^^^ .variable.parameter.function.js
//                             ^ .punctuation.section.group.end.js
//                               ^ .punctuation.section.block.begin.js
//                                ^ .punctuation.section.block.end.js
   function *foo(param, ...param) {}
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^ .storage.modifier.js
//           ^^^ .entity.name.function.js
//              ^ .punctuation.section.group.begin.js
//               ^^^^^ .variable.parameter.function.js
//                    ^ .punctuation.definition.function.parameters.js
//                      ^^^ .keyword.operator.rest.js
//                         ^^^^^ .variable.parameter.function.js
//                              ^ .punctuation.section.group.end.js
//                                ^ .punctuation.section.block.begin.js
//                                 ^ .punctuation.section.block.end.js
   function foo(param:number, ...param:string):boolean {}
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^^^ .entity.name.function.js
//             ^ .punctuation.section.group.begin.js
//              ^^^^^ .variable.parameter.function.js
//                   ^ .punctuation.binding.flow
//                    ^^^^^^ .support.type.primitive.flow
//                    ^^^^^^ .entity.name.type.flow
//                          ^ .punctuation.definition.function.parameters.js
//                            ^^^ .keyword.operator.rest.js
//                               ^^^^^ .variable.parameter.function.js
//                                    ^ .punctuation.binding.flow
//                                     ^^^^^^ .support.type.primitive.flow
//                                     ^^^^^^ .entity.name.type.flow
//                                           ^ .punctuation.section.group.end.js
//                                            ^ .punctuation.binding.flow
//                                             ^^^^^^^ .support.type.primitive.flow
//                                             ^^^^^^^ .entity.name.type.flow
//                                                     ^ .punctuation.section.block.begin.js
//                                                      ^ .punctuation.section.block.end.js
   function foo(param:?number, ...param:?(string|number)):?boolean {}
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^^^ .entity.name.function.js
//             ^ .punctuation.section.group.begin.js
//              ^^^^^ .variable.parameter.function.js
//                   ^ .punctuation.binding.flow
//                    ^ .keyword.operator.other.nullable.flow
//                     ^^^^^^ .support.type.primitive.flow
//                     ^^^^^^ .entity.name.type.flow
//                           ^ .punctuation.definition.function.parameters.js
//                             ^^^ .keyword.operator.rest.js
//                                ^^^^^ .variable.parameter.function.js
//                                     ^ .punctuation.binding.flow
//                                      ^ .keyword.operator.other.nullable.flow
//                                       ^ .punctuation.definition.expression.group.begin.flow
//                                        ^^^^^^ .support.type.primitive.flow
//                                        ^^^^^^ .entity.name.type.flow
//                                              ^ .keyword.operator.other.union.flow
//                                               ^^^^^^ .support.type.primitive.flow
//                                               ^^^^^^ .entity.name.type.flow
//                                                     ^ .punctuation.definition.expression.group.end.flow
//                                                      ^ .punctuation.section.group.end.js
//                                                       ^ .punctuation.binding.flow
//                                                        ^ .keyword.operator.other.nullable.flow
//                                                         ^^^^^^^ .support.type.primitive.flow
//                                                         ^^^^^^^ .entity.name.type.flow
//                                                                 ^ .punctuation.section.block.begin.js
//                                                                  ^ .punctuation.section.block.end.js
   function foo<A,B>(param:A, ...param:B):B {}
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^^^ .entity.name.function.js
//             ^ .punctuation.definition.template.parameters.begin.flow
//              ^ .entity.name.type.flow
//               ^ .punctuation.definition.template.parameters.flow
//                ^ .entity.name.type.flow
//                 ^ .punctuation.definition.template.parameters.end.flow
//                  ^ .punctuation.section.group.begin.js
//                   ^^^^^ .variable.parameter.function.js
//                        ^ .punctuation.binding.flow
//                         ^ .entity.name.type.flow
//                          ^ .punctuation.definition.function.parameters.js
//                            ^^^ .keyword.operator.rest.js
//                               ^^^^^ .variable.parameter.function.js
//                                    ^ .punctuation.binding.flow
//                                     ^ .entity.name.type.flow
//                                      ^ .punctuation.section.group.end.js
//                                       ^ .punctuation.binding.flow
//                                        ^ .entity.name.type.flow
//                                          ^ .punctuation.section.block.begin.js
//                                           ^ .punctuation.section.block.end.js
   function *foo<A,B>(param:A, ...param:B):B {}
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^ .storage.modifier.js
//           ^^^ .entity.name.function.js
//              ^ .punctuation.definition.template.parameters.begin.flow
//               ^ .entity.name.type.flow
//                ^ .punctuation.definition.template.parameters.flow
//                 ^ .entity.name.type.flow
//                  ^ .punctuation.definition.template.parameters.end.flow
//                   ^ .punctuation.section.group.begin.js
//                    ^^^^^ .variable.parameter.function.js
//                         ^ .punctuation.binding.flow
//                          ^ .entity.name.type.flow
//                           ^ .punctuation.definition.function.parameters.js
//                             ^^^ .keyword.operator.rest.js
//                                ^^^^^ .variable.parameter.function.js
//                                     ^ .punctuation.binding.flow
//                                      ^ .entity.name.type.flow
//                                       ^ .punctuation.section.group.end.js
//                                        ^ .punctuation.binding.flow
//                                         ^ .entity.name.type.flow
//                                           ^ .punctuation.section.block.begin.js
//                                            ^ .punctuation.section.block.end.js
   function () {}
// ^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^ .punctuation.section.group.begin.js
//           ^ .punctuation.section.group.end.js
//             ^ .punctuation.section.block.begin.js
//              ^ .punctuation.section.block.end.js
   function *() {}
// ^^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^ .storage.modifier.js
//           ^ .punctuation.section.group.begin.js
//            ^ .punctuation.section.group.end.js
//              ^ .punctuation.section.block.begin.js
//               ^ .punctuation.section.block.end.js
   function *<A,B>(param:A, ...param:B):B {}
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .meta.function.declaration.js
// ^^^^^^^^ .storage.type.function.js
//          ^ .storage.modifier.js
//           ^ .punctuation.definition.template.parameters.begin.flow
//            ^ .entity.name.type.flow
//             ^ .punctuation.definition.template.parameters.flow
//              ^ .entity.name.type.flow
//               ^ .punctuation.definition.template.parameters.end.flow
//                ^ .punctuation.section.group.begin.js
//                 ^^^^^ .variable.parameter.function.js
//                      ^ .punctuation.binding.flow
//                       ^ .entity.name.type.flow
//                        ^ .punctuation.definition.function.parameters.js
//                          ^^^ .keyword.operator.rest.js
//                             ^^^^^ .variable.parameter.function.js
//                                  ^ .punctuation.binding.flow
//                                   ^ .entity.name.type.flow
//                                    ^ .punctuation.section.group.end.js
//                                     ^ .punctuation.binding.flow
//                                      ^ .entity.name.type.flow
//                                        ^ .punctuation.section.block.begin.js
//                                         ^ .punctuation.section.block.end.js
