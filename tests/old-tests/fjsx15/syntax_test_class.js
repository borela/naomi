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
// ^^^^^ .storage.type.class.js
//       ^^^ .entity.name.class.js
//           ^ .punctuation.definition.class.body.begin.js
//            ^ .punctuation.definition.class.body.end.js
   class Foo<A,B> {}
// ^^^^^ .storage.type.class.js
//       ^^^ .entity.name.class.js
//          ^ .punctuation.definition.template.parameters.begin.flow
//           ^ .entity.name.type.flow
//            ^ .punctuation.definition.template.parameters.flow
//             ^ .entity.name.type.flow
//              ^ .punctuation.definition.template.parameters.end.flow
//                ^ .punctuation.definition.class.body.begin.js
//                 ^ .punctuation.definition.class.body.end.js
   class Foo extends A.B.C {}
// ^^^^^ .storage.type.class.js
//       ^^^ .entity.name.class.js
//           ^^^^^^^ .storage.modifier.extends.js
//                   ^ .entity.name.namespace.a.flow
//                    ^ .punctuation.definition.namespace.a.flow
//                     ^ .entity.name.namespace.b.flow
//                      ^ .punctuation.definition.namespace.b.flow
//                       ^ .parent.js
//                       ^ .entity.name.class.js
//                         ^ .punctuation.definition.class.body.begin.js
//                          ^ .punctuation.definition.class.body.end.js
   class Foo<A,B> extends A.B.C {}
// ^^^^^ .storage.type.class.js
//       ^^^ .entity.name.class.js
//          ^ .punctuation.definition.template.parameters.begin.flow
//           ^ .entity.name.type.flow
//            ^ .punctuation.definition.template.parameters.flow
//             ^ .entity.name.type.flow
//              ^ .punctuation.definition.template.parameters.end.flow
//                ^^^^^^^ .storage.modifier.extends.js
//                        ^ .entity.name.namespace.a.flow
//                         ^ .punctuation.definition.namespace.a.flow
//                          ^ .entity.name.namespace.b.flow
//                           ^ .punctuation.definition.namespace.b.flow
//                            ^ .parent.js
//                            ^ .entity.name.class.js
//                              ^ .punctuation.definition.class.body.begin.js
//                               ^ .punctuation.definition.class.body.end.js
   class Foo {
// ^^^^^ .storage.type.class.js
//       ^^^ .entity.name.class.js
//           ^ .punctuation.definition.class.body.begin.js
   @decorator
// ^ .punctuation.definition.decorator.js
//  ^^^^^^^^^ .entity.name.decorator.js
   @decorator.decorator
// ^ .punctuation.definition.decorator.js
//  ^^^^^^^^^ .entity.name.decorator.js
//           ^ .punctuation.definition.decorator.chain.js
//            ^^^^^^^^ .entity.name.decorator.js
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
   @decorator(1,'2').decorator(1,'2')
// ^ .punctuation.definition.decorator.js
//  ^^^^^^^^^ .entity.name.decorator.js
//           ^ .punctuation.definition.decorator.arguments.begin.js
//            ^ .constant.numeric.decimal.js
//             ^ .punctuation.definition.decorator.arguments.js
//              ^^^ .string.quoted.single.js
//              ^ .punctuation.definition.string.begin.js
//                ^ .punctuation.definition.string.end.js
//                 ^ .punctuation.definition.decorator.arguments.end.js
//                  ^ .punctuation.definition.decorator.chain.js
//                   ^^^^^^^^^ .entity.name.decorator.js
//                            ^ .punctuation.definition.decorator.arguments.begin.js
//                             ^ .constant.numeric.decimal.js
//                              ^ .punctuation.definition.decorator.arguments.js
//                               ^^^ .string.quoted.single.js
//                               ^ .punctuation.definition.string.begin.js
//                                 ^ .punctuation.definition.string.end.js
//                                  ^ .punctuation.definition.decorator.arguments.end.js
   static propTypes:number = {initialCount:React.PropTypes.number};
// ^^^^^^ .storage.modifier.js
// ^^^^^^ .keyword.other.access.js
//        ^^^^^^^^^ .variable.other.readwrite.js
//                         ^ .keyword.operator.other.assignment.js
//                           ^ .punctuation.section.block.begin.js
//                            ^^^^^^^^^^^^ .variable.other.readwrite.js
//                                        ^ .punctuation.binding.js
//                                         ^^^^^ .variable.other.readwrite.js
//                                              ^ .keyword.operator.other.member-access.js
//                                               ^^^^^^^^^ .variable.other.readwrite.js
//                                                        ^ .keyword.operator.other.member-access.js
//                                                         ^^^^^^ .variable.other.readwrite.js
//                                                               ^ .punctuation.section.block.end.js
//                                                                ^ .punctuation.terminator.js
   static defaultProps = {initialCount:0};
// ^^^^^^ .storage.modifier.js
// ^^^^^^ .keyword.other.access.js
//        ^^^^^^^^^^^^ .variable.other.readwrite.js
//                     ^ .keyword.operator.other.assignment.js
//                       ^ .punctuation.section.block.begin.js
//                        ^^^^^^^^^^^^ .variable.other.readwrite.js
//                                    ^ .punctuation.binding.js
//                                     ^ .constant.numeric.decimal.js
//                                      ^ .punctuation.section.block.end.js
//                                       ^ .punctuation.terminator.js
   state = {count:this.props.initialCount};
// ^^^^^ .variable.other.readwrite.js
//       ^ .keyword.operator.other.assignment.js
//         ^ .punctuation.section.block.begin.js
//          ^^^^^ .variable.other.readwrite.js
//               ^ .punctuation.binding.js
//                ^^^^ .support.core.js
//                ^^^^ .variable.other.readwrite.js
//                    ^ .keyword.operator.other.member-access.js
//                     ^^^^^ .support.lib.react-js
//                     ^^^^^ .variable.other.readwrite.js
//                          ^ .keyword.operator.other.member-access.js
//                           ^^^^^^^^^^^^ .variable.other.readwrite.js
//                                       ^ .punctuation.section.block.end.js
//                                        ^ .punctuation.terminator.js
    constructor(){}
//  ^^^^^^^^^^^ .support.js
//  ^^^^^^^^^^^ .entity.name.function.js
//             ^ .punctuation.section.group.begin.js
//              ^ .punctuation.section.group.end.js
//               ^ .punctuation.section.block.begin.js
//                ^ .punctuation.section.block.end.js
    method(){}
//  ^^^^^^ .entity.name.function.js
//        ^ .punctuation.section.group.begin.js
//         ^ .punctuation.section.group.end.js
//          ^ .punctuation.section.block.begin.js
//           ^ .punctuation.section.block.end.js
    *method(){}
//  ^ .storage.modifier.js
//   ^^^^^^ .entity.name.function.js
//         ^ .punctuation.section.group.begin.js
//          ^ .punctuation.section.group.end.js
//           ^ .punctuation.section.block.begin.js
//            ^ .punctuation.section.block.end.js
    get property(){}
//  ^^^ .storage.modifier.js
//  ^^^ .keyword.other.proxy.js
//      ^^^^^^^^ .entity.name.function.js
//              ^ .punctuation.section.group.begin.js
//               ^ .punctuation.section.group.end.js
//                ^ .punctuation.section.block.begin.js
//                 ^ .punctuation.section.block.end.js
    set property(){}
//  ^^^ .storage.modifier.js
//  ^^^ .keyword.other.proxy.js
//      ^^^^^^^^ .entity.name.function.js
//              ^ .punctuation.section.group.begin.js
//               ^ .punctuation.section.group.end.js
//                ^ .punctuation.section.block.begin.js
//                 ^ .punctuation.section.block.end.js
    async method(){}
//  ^^^^^ .storage.modifier.js
//  ^^^^^ .keyword.other.async.js
//        ^^^^^^ .entity.name.function.js
//              ^ .punctuation.section.group.begin.js
//               ^ .punctuation.section.group.end.js
//                ^ .punctuation.section.block.begin.js
//                 ^ .punctuation.section.block.end.js
    static method(){}
//  ^^^^^^ .storage.modifier.js
//  ^^^^^^ .keyword.other.access.js
//         ^^^^^^ .entity.name.function.js
//               ^ .punctuation.section.group.begin.js
//                ^ .punctuation.section.group.end.js
//                 ^ .punctuation.section.block.begin.js
//                  ^ .punctuation.section.block.end.js
    static get property(){}
//  ^^^^^^ .storage.modifier.js
//  ^^^^^^ .keyword.other.access.js
//         ^^^ .storage.modifier.js
//         ^^^ .keyword.other.proxy.js
//             ^^^^^^^^ .entity.name.function.js
//                     ^ .punctuation.section.group.begin.js
//                      ^ .punctuation.section.group.end.js
//                       ^ .punctuation.section.block.begin.js
//                        ^ .punctuation.section.block.end.js
    static set property(){}
//  ^^^^^^ .storage.modifier.js
//  ^^^^^^ .keyword.other.access.js
//         ^^^ .storage.modifier.js
//         ^^^ .keyword.other.proxy.js
//             ^^^^^^^^ .entity.name.function.js
//                     ^ .punctuation.section.group.begin.js
//                      ^ .punctuation.section.group.end.js
//                       ^ .punctuation.section.block.begin.js
//                        ^ .punctuation.section.block.end.js
    static async method(){}
//  ^^^^^^ .storage.modifier.js
//  ^^^^^^ .keyword.other.access.js
//         ^^^^^ .storage.modifier.js
//         ^^^^^ .keyword.other.async.js
//               ^^^^^^ .entity.name.function.js
//                     ^ .punctuation.section.group.begin.js
//                      ^ .punctuation.section.group.end.js
//                       ^ .punctuation.section.block.begin.js
//                        ^ .punctuation.section.block.end.js
   }
// ^ .punctuation.definition.class.body.end.js
   class Foo {
// ^^^^^ .storage.type.class.js
//       ^^^ .entity.name.class.js
//           ^ .punctuation.definition.class.body.begin.js
   property:type
// ^^^^^^^^ .variable.other.readwrite.js
//         ^ .punctuation.binding.flow
//          ^^^^ .flow
//          ^^^^ .entity.name.type.flow
    constructor(){}
//  ^^^^^^^^^^^ .support.js
//  ^^^^^^^^^^^ .entity.name.function.js
//             ^ .punctuation.section.group.begin.js
//              ^ .punctuation.section.group.end.js
//               ^ .punctuation.section.block.begin.js
//                ^ .punctuation.section.block.end.js
   }
// ^ .punctuation.definition.class.body.end.js
