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

   class Foo {}
// ^^^^^ .keyword.declaration.class.js.fjsx15
//       ^^^ .entity.name.class.js.fjsx15
//           ^ .punctuation.definition.class.body.begin.js.fjsx15
//            ^ .punctuation.definition.class.body.end.js.fjsx15
   class Foo<A,B> {}
// ^^^^^ .keyword.declaration.class.js.fjsx15
//       ^^^ .entity.name.class.js.fjsx15
//          ^ .punctuation.definition.template.parameters.begin.flowtype
//           ^ .entity.name.type.flowtype
//            ^ .punctuation.definition.template.parameters.flowtype
//             ^ .entity.name.type.flowtype
//              ^ .punctuation.definition.template.parameters.end.flowtype
//                ^ .punctuation.definition.class.body.begin.js.fjsx15
//                 ^ .punctuation.definition.class.body.end.js.fjsx15
   class Foo extends A.B.C {}
// ^^^^^ .keyword.declaration.class.js.fjsx15
//       ^^^ .entity.name.class.js.fjsx15
//           ^^^^^^^ .keyword.other.inherit.js.fjsx15
//                   ^ .entity.name.namespace.a.flowtype
//                    ^ .punctuation.definition.namespace.a.flowtype
//                     ^ .entity.name.namespace.b.flowtype
//                      ^ .punctuation.definition.namespace.b.flowtype
//                       ^ .parent.js.fjsx15
//                       ^ .entity.name.class.js.fjsx15
//                         ^ .punctuation.definition.class.body.begin.js.fjsx15
//                          ^ .punctuation.definition.class.body.end.js.fjsx15
   class Foo<A,B> extends A.B.C {}
// ^^^^^ .keyword.declaration.class.js.fjsx15
//       ^^^ .entity.name.class.js.fjsx15
//          ^ .punctuation.definition.template.parameters.begin.flowtype
//           ^ .entity.name.type.flowtype
//            ^ .punctuation.definition.template.parameters.flowtype
//             ^ .entity.name.type.flowtype
//              ^ .punctuation.definition.template.parameters.end.flowtype
//                ^^^^^^^ .keyword.other.inherit.js.fjsx15
//                        ^ .entity.name.namespace.a.flowtype
//                         ^ .punctuation.definition.namespace.a.flowtype
//                          ^ .entity.name.namespace.b.flowtype
//                           ^ .punctuation.definition.namespace.b.flowtype
//                            ^ .parent.js.fjsx15
//                            ^ .entity.name.class.js.fjsx15
//                              ^ .punctuation.definition.class.body.begin.js.fjsx15
//                               ^ .punctuation.definition.class.body.end.js.fjsx15
   class Foo {
// ^^^^^ .keyword.declaration.class.js.fjsx15
//       ^^^ .entity.name.class.js.fjsx15
//           ^ .punctuation.definition.class.body.begin.js.fjsx15
   @decorator
// ^ .punctuation.definition.decorator.js.fjsx15
//  ^^^^^^^^^ .entity.name.decorator.js.fjsx15
   @decorator.decorator
// ^ .punctuation.definition.decorator.js.fjsx15
//  ^^^^^^^^^ .entity.name.decorator.js.fjsx15
//           ^ .punctuation.definition.decorator.chain.js.fjsx15
//            ^^^^^^^^ .entity.name.decorator.js.fjsx15
   @decorator(1,'2')
// ^ .punctuation.definition.decorator.js.fjsx15
//  ^^^^^^^^^ .entity.name.decorator.js.fjsx15
//           ^ .punctuation.definition.decorator.arguments.begin.js.fjsx15
//            ^ .constant.numeric.decimal.js.fjsx15
//             ^ .punctuation.definition.decorator.arguments.js.fjsx15
//              ^^^ .string.quoted.single.js.fjsx15
//              ^ .punctuation.definition.string.begin.js.fjsx15
//                ^ .punctuation.definition.string.end.js.fjsx15
//                 ^ .punctuation.definition.decorator.arguments.end.js.fjsx15
   @decorator(1,'2').decorator(1,'2')
// ^ .punctuation.definition.decorator.js.fjsx15
//  ^^^^^^^^^ .entity.name.decorator.js.fjsx15
//           ^ .punctuation.definition.decorator.arguments.begin.js.fjsx15
//            ^ .constant.numeric.decimal.js.fjsx15
//             ^ .punctuation.definition.decorator.arguments.js.fjsx15
//              ^^^ .string.quoted.single.js.fjsx15
//              ^ .punctuation.definition.string.begin.js.fjsx15
//                ^ .punctuation.definition.string.end.js.fjsx15
//                 ^ .punctuation.definition.decorator.arguments.end.js.fjsx15
//                  ^ .punctuation.definition.decorator.chain.js.fjsx15
//                   ^^^^^^^^^ .entity.name.decorator.js.fjsx15
//                            ^ .punctuation.definition.decorator.arguments.begin.js.fjsx15
//                             ^ .constant.numeric.decimal.js.fjsx15
//                              ^ .punctuation.definition.decorator.arguments.js.fjsx15
//                               ^^^ .string.quoted.single.js.fjsx15
//                               ^ .punctuation.definition.string.begin.js.fjsx15
//                                 ^ .punctuation.definition.string.end.js.fjsx15
//                                  ^ .punctuation.definition.decorator.arguments.end.js.fjsx15
   static propTypes:number = {initialCount:React.PropTypes.number};
// ^^^^^^ .storage.modifier.js.fjsx15
// ^^^^^^ .keyword.other.access.js.fjsx15
//        ^^^^^^^^^ .entity.name.variable.js.fjsx15
//                         ^ .keyword.operator.other.assignment.js.fjsx15
//                           ^ .punctuation.definition.object.begin.js.fjsx15
//                            ^^^^^^^^^^^^ .entity.name.variable.js.fjsx15
//                                        ^ .keyword.operator.other.association.js.fjsx15
//                                         ^^^^^ .entity.name.variable.js.fjsx15
//                                              ^ .keyword.operator.other.member-access.js.fjsx15
//                                               ^^^^^^^^^ .entity.name.variable.js.fjsx15
//                                                        ^ .keyword.operator.other.member-access.js.fjsx15
//                                                         ^^^^^^ .entity.name.variable.js.fjsx15
//                                                               ^ .punctuation.definition.object.end.js.fjsx15
//                                                                ^ .keyword.operator.other.terminator.js.fjsx15
   static defaultProps = {initialCount:0};
// ^^^^^^ .storage.modifier.js.fjsx15
// ^^^^^^ .keyword.other.access.js.fjsx15
//        ^^^^^^^^^^^^ .entity.name.variable.js.fjsx15
//                     ^ .keyword.operator.other.assignment.js.fjsx15
//                       ^ .punctuation.definition.object.begin.js.fjsx15
//                        ^^^^^^^^^^^^ .entity.name.variable.js.fjsx15
//                                    ^ .keyword.operator.other.association.js.fjsx15
//                                     ^ .constant.numeric.decimal.js.fjsx15
//                                      ^ .punctuation.definition.object.end.js.fjsx15
//                                       ^ .keyword.operator.other.terminator.js.fjsx15
   state = {count:this.props.initialCount};
// ^^^^^ .entity.name.variable.js.fjsx15
//       ^ .keyword.operator.other.assignment.js.fjsx15
//         ^ .punctuation.definition.object.begin.js.fjsx15
//          ^^^^^ .entity.name.variable.js.fjsx15
//               ^ .keyword.operator.other.association.js.fjsx15
//                ^^^^ .support.core.js.fjsx15
//                ^^^^ .entity.name.variable.js.fjsx15
//                    ^ .keyword.operator.other.member-access.js.fjsx15
//                     ^^^^^ .support.lib.react-js.fjsx15
//                     ^^^^^ .entity.name.variable.js.fjsx15
//                          ^ .keyword.operator.other.member-access.js.fjsx15
//                           ^^^^^^^^^^^^ .entity.name.variable.js.fjsx15
//                                       ^ .punctuation.definition.object.end.js.fjsx15
//                                        ^ .keyword.operator.other.terminator.js.fjsx15
    constructor(){}
//  ^^^^^^^^^^^ .support.js.fjsx15
//  ^^^^^^^^^^^ .entity.name.function.js.fjsx15
//             ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//              ^ .punctuation.definition.function.parameters.end.js.fjsx15
//               ^ .punctuation.definition.function.body.begin.js.fjsx15
//                ^ .punctuation.definition.function.body.end.js.fjsx15
    method(){}
//  ^^^^^^ .entity.name.function.js.fjsx15
//        ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//         ^ .punctuation.definition.function.parameters.end.js.fjsx15
//          ^ .punctuation.definition.function.body.begin.js.fjsx15
//           ^ .punctuation.definition.function.body.end.js.fjsx15
    *method(){}
//  ^ .storage.modifier.js.fjsx15
//  ^ .keyword.operator.other.generator.js.fjsx15
//   ^^^^^^ .entity.name.function.js.fjsx15
//         ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//          ^ .punctuation.definition.function.parameters.end.js.fjsx15
//           ^ .punctuation.definition.function.body.begin.js.fjsx15
//            ^ .punctuation.definition.function.body.end.js.fjsx15
    get property(){}
//  ^^^ .storage.modifier.js.fjsx15
//  ^^^ .keyword.other.proxy.js.fjsx15
//      ^^^^^^^^ .entity.name.function.js.fjsx15
//              ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//               ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                ^ .punctuation.definition.function.body.begin.js.fjsx15
//                 ^ .punctuation.definition.function.body.end.js.fjsx15
    set property(){}
//  ^^^ .storage.modifier.js.fjsx15
//  ^^^ .keyword.other.proxy.js.fjsx15
//      ^^^^^^^^ .entity.name.function.js.fjsx15
//              ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//               ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                ^ .punctuation.definition.function.body.begin.js.fjsx15
//                 ^ .punctuation.definition.function.body.end.js.fjsx15
    async method(){}
//  ^^^^^ .storage.modifier.js.fjsx15
//  ^^^^^ .keyword.other.async.js.fjsx15
//        ^^^^^^ .entity.name.function.js.fjsx15
//              ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//               ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                ^ .punctuation.definition.function.body.begin.js.fjsx15
//                 ^ .punctuation.definition.function.body.end.js.fjsx15
    static method(){}
//  ^^^^^^ .storage.modifier.js.fjsx15
//  ^^^^^^ .keyword.other.access.js.fjsx15
//         ^^^^^^ .entity.name.function.js.fjsx15
//               ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//                ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                 ^ .punctuation.definition.function.body.begin.js.fjsx15
//                  ^ .punctuation.definition.function.body.end.js.fjsx15
    static get property(){}
//  ^^^^^^ .storage.modifier.js.fjsx15
//  ^^^^^^ .keyword.other.access.js.fjsx15
//         ^^^ .storage.modifier.js.fjsx15
//         ^^^ .keyword.other.proxy.js.fjsx15
//             ^^^^^^^^ .entity.name.function.js.fjsx15
//                     ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//                      ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                       ^ .punctuation.definition.function.body.begin.js.fjsx15
//                        ^ .punctuation.definition.function.body.end.js.fjsx15
    static set property(){}
//  ^^^^^^ .storage.modifier.js.fjsx15
//  ^^^^^^ .keyword.other.access.js.fjsx15
//         ^^^ .storage.modifier.js.fjsx15
//         ^^^ .keyword.other.proxy.js.fjsx15
//             ^^^^^^^^ .entity.name.function.js.fjsx15
//                     ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//                      ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                       ^ .punctuation.definition.function.body.begin.js.fjsx15
//                        ^ .punctuation.definition.function.body.end.js.fjsx15
    static async method(){}
//  ^^^^^^ .storage.modifier.js.fjsx15
//  ^^^^^^ .keyword.other.access.js.fjsx15
//         ^^^^^ .storage.modifier.js.fjsx15
//         ^^^^^ .keyword.other.async.js.fjsx15
//               ^^^^^^ .entity.name.function.js.fjsx15
//                     ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//                      ^ .punctuation.definition.function.parameters.end.js.fjsx15
//                       ^ .punctuation.definition.function.body.begin.js.fjsx15
//                        ^ .punctuation.definition.function.body.end.js.fjsx15
   }
// ^ .punctuation.definition.class.body.end.js.fjsx15
   class Foo {
// ^^^^^ .keyword.declaration.class.js.fjsx15
//       ^^^ .entity.name.class.js.fjsx15
//           ^ .punctuation.definition.class.body.begin.js.fjsx15
   property:type
// ^^^^^^^^ .entity.name.variable.js.fjsx15
//         ^ .keyword.operator.other.association.flowtype
//          ^^^^ .flowtype
//          ^^^^ .entity.name.type.flowtype
    constructor(){}
//  ^^^^^^^^^^^ .support.js.fjsx15
//  ^^^^^^^^^^^ .entity.name.function.js.fjsx15
//             ^ .punctuation.definition.function.parameters.begin.js.fjsx15
//              ^ .punctuation.definition.function.parameters.end.js.fjsx15
//               ^ .punctuation.definition.function.body.begin.js.fjsx15
//                ^ .punctuation.definition.function.body.end.js.fjsx15
   }
// ^ .punctuation.definition.class.body.end.js.fjsx15
