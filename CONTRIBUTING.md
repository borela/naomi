# Contributing

Thank you for considering contributing to this project! The following is a set
of guidelines not rules, use your best judgment and feel free to propose changes
to this document in a pull request.

## Table of contents

1. [Pull requests](#pull-requests)
2. [Style guides](#style-guides)
  1. [Commit messages](#commit-messages)
    1. [Example of a commit message](#example-of-a-commit-message)
  2. [Color schemes](#color-schemes-style-guide)
  3. [Syntaxes](#syntaxes-style-guide)
  4. [Tests](#tests-style-guide)
3. [License headers](#license-headers)
4. [Useful links](#useful-links)

## Pull requests

1. Fork.
2. Follow the style guides.
3. Do your changes on a separate branch.
4. Use your real name and email in the commits.
5. Include screenshots and animated GIFs in your pull request whenever possible.

## Style guides

### Commit messages

In the beginning of the project, there were no guides on commit messages and
[now][badCommit1] [some][badCommit2] [messages][badCommit3] cannot be visualized
perfectly on some tools and github, to prevent further mistakes, use the
following style:

* Use the present tense: “*Add feature.*” instead of “*Added feature.*”.
* Use the imperative mood: “*Move file to...*” instead of “*Moves file to...*”.
* Lines must not exceed 72 characters.
* Use asterisks for bullet points.
* Use a hanging indent for bullet points that goes through multiple lines.
* Reference issues and pull requests liberally.

#### Example of a commit message:

    Summary (72 chars or less)

    More detailed explanatory text, if necessary.  Wrap it to about 72
    characters. In some contexts, the first line is treated as the
    subject of an email and the rest of the text as the body. The blank
    line separating the summary from the body is critical unless you omit
    the body entirely.

    Further paragraphs come after blank lines.

    * An asterisk followed by a single space is used for bullet points
      with blank lines in between them.

    * Use a hanging indent for bullet points that goes through multiple
      lines.

### Color schemes style guide

Color schemes are coded with scss, you will have one main file at the root of
the project and as many partials as you need under `scheme/[name]`. To compile
those files you will need [CSScheme][CSScheme].

* Use SCSS.
* Indent with 2 spaces.
* Use blank lines to group related sections of code.
* Add the appropriate [license header](#license-headers).

### Syntaxes style guide

* Name the main syntax file using the following format
  `naomi.[syntax].sublime-syntax`.
* Additional files must not have the `name` or `file_extension` keys in the
  header. Also, they must have the key `scope` set to `...` and the key `hidden`
  set to `true`.
* Break the syntax into multiple files to make it easier to maintain and extend.
* Break the regexes into multiple lines. This rule can be broken if the having
  the patterns on the same line will make it clearer.
* Design for sequence. It means that you should avoid look behind pattern at all
  costs and matches pop the current context from the stack.
* Execute the command `Naomi: Run syntax tests` to check if your changes broke
  anything.
* Add the appropriate [license header](#license-headers).

### Tests style guide

* Feel free to use the `code-generator.xlsm` to generate tests for lists of
  constants, it’s just a spreedsheet with macros where can click a button to
  send the tests to the clipboard.
* Create multiple files to group related tests.
* Test as much as possible.
* Add the appropriate [license header](#license-headers).

### License headers

This project uses the [Apache 2.0 license][license] and one of its requirements
is a header which makes it easier for other people to know which license was
used without having to look into the root of the project.

The original header has the author and an email, but in this case it won’t be
necessary as one of the project’s requirements is that you use your real name
and email in the commits so that we can track the author easily.

Not all files need a license header, configuration files are a  good example of
that, so, if a file required careful design on your part, use one of these:

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

    # Licensed under the Apache License, Version 2.0 (the “License”); you may not
    # use this file except in compliance with the License. You may obtain a copy of
    # the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an “AS IS” BASIS, WITHOUT
    # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    # License for the specific language governing permissions and limitations under
    # the License.

    <!--
     | Licensed under the Apache License, Version 2.0 (the “License”); you may not
     | use this file except in compliance with the License. You may obtain a copy of
     | the License at
     |
     |     http://www.apache.org/licenses/LICENSE-2.0
     |
     | Unless required by applicable law or agreed to in writing, software
     | distributed under the License is distributed on an “AS IS” BASIS, WITHOUT
     | WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
     | License for the specific language governing permissions and limitations under
     | the License.
    -->

## Useful links

* [Sublime text API][sublimeApiDocs]
* [Sublime text syntax][sublimeSynDocs]
* [CSScheme][CSScheme]
* [Scope hunter][scopeHunter]

[CSScheme]: https://github.com/FichteFoll/CSScheme
[sublimeApiDocs]: https://www.sublimetext.com/docs/3/api_reference.html
[sublimeSynDocs]: https://www.sublimetext.com/docs/3/syntax.html
[scopeHunter]: https://github.com/facelessuser/ScopeHunter

[badCommit1]: https://github.com/borela/naomi/commit/91cc07753bff53c7f003d674a6e607b0979f3eae
[badCommit2]: https://github.com/borela/naomi/commit/e1e95cc0279614e92938d1181391217cbcaf2b07
[badCommit3]: https://github.com/borela/naomi/commit/84af9160bc57dd607ed9afda58338e50c09fc080

[license]: http://www.apache.org/licenses/LICENSE-2.0
[issues]: https://guides.github.com/features/issues/
[releases]: https://github.com/borela/naomi/releases
