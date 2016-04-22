# Contributing

Thank you for considering contributing to this project! Some tips that make it
easy to create the syntax files:

## 1: Read the docs

There's a basic tutorial on how to write the syntax files and tests in sublime's
[offical documentation](https://www.sublimetext.com/docs/3/syntax.html).

## 2: Install Scope Hunter

This [tool](https://github.com/facelessuser/ScopeHunter) is essential when you
are debugging the highlighting, it has an option "Toggle Instant Scoper" which
shows the scopes in real time as you move the cursor.

## 3: Create the tests

This is an obvious one, it's a lot easier to write the syntax when you know what
the end result must be.

## 4: Don't forget about the variables

In syntax files you can declare variables at the top of the file, use them to
prevent repetion.

## 5: Break the regex into multiple lines

Breaking the regular expressions into multiple lines will make it a lot easier
to understand, just prepend it with `(?x)` and all whitespaces are going to be
ignored.

## 6: Be awared of ignored spaces

When you add the `(?x)` option to your regex, any whitespace is ignored, so, in
those cases, if you need to represent a pattern that includes it, you have to
use the `\s` pattern.

## 7: Atomic groups

Often times you need to check against a list of keywords, symbols, etc... use
atomic groups as it will stop after the first match is found, making the regex
a lot faster.

Bad example:

    (?:Foo
      |Bar
    )

Good example:

    (?>Foo
      |Bar
    )

## 8: Design for sequence

Most languages are designed in a way that you can expect tokens to have some
sort of sequence.

For example, in PHP 7 you can declare the type hint before a function parameter,
it is optional and after it, only a variable is expected and this is key to a
good syntax highlighting.

When you highlight like this, you don't need to mark regions as invalid, the
programmer will know something is wrong if the color isn't right, so it'll make
the syntax file a lot simpler.

To simplify how it would work, imagine a php function:

    function foo($paramter1, string $parameter2)

And the following syntax:

    main:
      - include: parameters-begin

    parameters-begin:
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
      - match: (?=\$)
        pop: true

    variable:
      - match: \$[a-z]*
        scope: variable.php
        pop: true

Basicly, the `main` context will try to match the beginning of the parameters
list and if found, push the `parameters` context.

The `parameters` context is a loop that will first check for the end of the list
and then try to match the type followed by the variable.
