// SYNTAX TEST "Packages/Naomi/syntaxes/naomi.mql4.sublime-syntax"

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

    virtual void Myfunction(   ) = 0;
//  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ statement.function.mql.4
//  ^^^^^^^ keyword.modifier.mql.4
//          ^^^^ support.type.mql.4
//          ^^^^ entity.name.type.mql.4
//               ^^^^^^^^^^ entity.name.function.mql.4
//                         ^^^^^ statement.function.parameters.mql.4
//                          ^^^ statement.function.parameters.content.mql.4

    virtual void Myfunction(   ) = NULL;
//  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ statement.function.mql.4
//  ^^^^^^^ keyword.modifier.mql.4
//          ^^^^ support.type.mql.4
//          ^^^^ entity.name.type.mql.4
//               ^^^^^^^^^^ entity.name.function.mql.4
//                         ^^^^^ statement.function.parameters.mql.4
//                          ^^^ statement.function.parameters.content.mql.4


    static void Myfunction(   ){   }
//  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ statement.function.mql.4
//  ^^^^^^ keyword.modifier.mql.4
//         ^^^^ support.type.mql.4
//         ^^^^ entity.name.type.mql.4
//              ^^^^^^^^^^ entity.name.function.mql.4
//                        ^^^^^ statement.function.parameters.mql.4
//                         ^^^ statement.function.parameters.content.mql.4


    void Myfunction(   ){   }
//  ^^^^^^^^^^^^^^^^^^^^^^ statement.function.mql.4
//  ^^^^ support.type.mql.4
//  ^^^^ entity.name.type.mql.4
//       ^^^^^^^^^^ entity.name.function.mql.4
//                 ^^^^^ statement.function.parameters.mql.4
//                  ^^^ statement.function.parameters.content.mql.4


    void Myfunction(void){   }
//  ^^^^^^^^^^^^^^^^^^^^^^^^^^ statement.function.mql.4
//  ^^^^ support.type.mql.4
//  ^^^^ entity.name.type.mql.4
//       ^^^^^^^^^^ entity.name.function.mql.4
//                 ^^^^^ statement.function.parameters.mql.4
//                  ^^^ statement.function.parameters.content.mql.4
