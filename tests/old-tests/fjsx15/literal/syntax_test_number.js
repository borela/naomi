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

   0;
// ^ .constant.numeric.decimal.js
   123;
// ^^^ .constant.numeric.decimal.js
   1_2_3;
// ^^^^^ .constant.numeric.decimal.js
   123_456_789;
// ^^^^^^^^^^^ .constant.numeric.decimal.js
   123.;
// ^^^^ .constant.numeric.float.js
   1_2_3.;
// ^^^^^^ .constant.numeric.float.js
   123_456_789.;
// ^^^^^^^^^^^^ .constant.numeric.float.js
   123.0;
// ^^^^^ .constant.numeric.float.js
   .123;
// ^^^^ .constant.numeric.float.js
   0.123;
// ^^^^^ .constant.numeric.float.js
   123e10;
// ^^^^^^ .constant.numeric.float.scientific.js
   123e+10;
// ^^^^^^^ .constant.numeric.float.scientific.js
   123e-10;
// ^^^^^^^ .constant.numeric.float.scientific.js
   0x123;
// ^^^^^ .constant.numeric.hex.js
   0x1_2_3;
// ^^^^^^^ .constant.numeric.hex.js
   0x123_456_789;
// ^^^^^^^^^^^^^ .constant.numeric.hex.js
