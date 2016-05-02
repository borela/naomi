# Contributing

Thank you for considering contributing to this project!

1. Fork the repository.
2. Do your changes on a separate branch.
3. Send the pull request.

## Code style

* Indent syntax files with 2 spaces.
* Indent other files with 4 spaces.
* Try to limit the line length to 80 characters, it's easier to scroll vertically
than horizontally.
* Avoid abbreviations and be descriptive as possible.

## Color scheme tips

Look at the color schemes provided to have an idea of how to create your own and
use [ScopeHunter][1] to understand how
the code is being highlighted.

## Syntax tips

#### 1: Read the [docs][0]

There's a basic tutorial on how to write the syntax files and tests on sublime's
[official documentation][0].

#### 2: Install [ScopeHunter][1]

This [tool][1] is essential when you
are debugging the highlighting, it has an option `Toggle Instant Scoper` which
shows the scopes in real time as you move the cursor.

#### 3: Create the tests

Try to create tests for all cases and check if your changes broke any of the
previous ones.

#### 4: Variables

In syntax files you can declare variables at the top of the file, use them to
prevent repetion.

#### 5: Break the regex into multiple lines

Break your regexes into multiple lines if it would make it clearer, just
remeber to use the option `(?x)` to ignore the white spaces.

#### 6: Be awared of ignored spaces

When you add the `(?x)` option to your regex, any whitespace is ignored, so, in
those cases, if you need to represent a pattern that includes it, you have to
use the `\s` pattern.

#### 7: Atomic groups

Often times you need to check against a list of keywords, symbols, etc... use
atomic groups as it will stop after the first match is found, making the regex
a lot faster.

#### 8: Design for sequence

Most languages are designed in a way that you can expect tokens to have some
sort of sequence.

For example, in PHP 7 you can declare the type hint before a function parameter,
it is optional and after it only a variable is expected.

When you highlight like this, you don't need to mark regions as invalid, the
programmer will know something is wrong if the color isn't right, so it'll make
the syntax file simpler.

Here's how it would work, consider this function:

    function foo($paramter1, string $parameter2)

And the following syntax:

    main:
      - match: \(
        scope: punctuation.structure.parameters.begin.php
        push: parameters

    parameters:
      - match: \)
        pop: true
      - match: ""
        push: [
          variable,
          type
        ]

    type:
      - match: [a-z]*
        scope: type.php
        pop: true
      # The type is optional, check it is a variable.
      - match: (?=\$)
        pop: true

    variable:
      - match: \$[a-z]*
        scope: variable.php
        pop: true

The `main` context will try to match the beginning of the parameters list and if
found, push the `parameters` context. The `parameters` context is a loop that
will first check for the end of the list and then try to match the type followed
by the variable.

[0]: https://www.sublimetext.com/docs/3/syntax.html
[1]: https://github.com/facelessuser/ScopeHunter
