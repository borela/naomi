# General [Work in progress]

Creating color schemes can be hard because many syntaxes use very generic scopes
and if like me, you tried to create one, you’ll soon find conflicts between
languages because like CSS classes, color schemes follow not only the order rules
appear in the file but the specificity too.

This documents aims to simplify that process by having a set of very specific
scopes that will make writting color schemes easier, you’ll be able to use tools
like [CSScheme][csscheme] and not be worried of the order of the rules, only their
specificity.

Look into the color scheme [Candyman][candyman] to see an example of how to create
your own using these scopes.

## Scope structure

Every token may have the following scopes:

* Origin (Optional)
* Context (Optional)
* Group (Optional)
* Identity (Required)

### Origin

Identifies the token’s origin to know if it's defined by a library or the
language’s core, for example:

```css
.support.core
.entity.name.function

.support.lib
.entity.name.constant
```

### Context

Some tokens may change based on the context, an example would be a function’s
parameter as they usualy just like normal variables and can be matched using
the same pattern.

```css
.function.parameter
.entity.name.variable
```

### Group

Grouping is commonly used to add special meaning to certain tokens. An common
example is that in some languages, class/function/variable declarations requires
a keyword before the actual entity’s name and most color schemes like to give
them a different color so that they are not confused with the other keywords:

#### Examples

```css
.storage.type
.keyword.declaration.function

.storage.type
.keyword.declaration.variable
```

### Identity

An identity is the most specific scope possible that decribes the token.

## Scope catalog

### Origin

```css
.support
  .core
  .lib
    .node-js
    .react-js
```

### Context

```css
.import
  .default

.function
  .parameter

.object
  .property

.destructuring
  .array
  .object
```

### Group

```css
.storage
  .modifier
  .type
.word
```

### Identity

```css
.entity
  .name
    .attribute
    .class
    .constant
    .enum
    .function
    .interface
    .structure
    .tag
    .trait
    .typedef
    .variable

.punctuation
  .delimiter
    .array
      .begin
      .end
      .access
        .begin
        .enda
    .class
      .body
        .begin
        .end
    .function
      .parameters
        .begin
        .end
      .parameters
        .begin
        .end
      .body
        .begin
        .end
    .object
      .computed-property
        .begin
        .end
      .body
        .begin
        .end

.keyword
  .control
    .conditional
    .loop
  .declaration
    .class
    .constant
    .interface
    .function
    .struct
    .trait
    .variable
  .operator
    .arithmetic
    .assignment
    .logical
    .other
      .association
      .comma
      .key-value
      .inherit
      .member-access
      .rest
      .scope-resolution
      .spread
      .terminator
      .void
  .other
    .access
    .async
    .constant-function
    .inherit
    .proxy
    .pure-virtual
    .unit
```

[candyman]: ./schemes/candyman
[csscheme]: https://github.com/FichteFoll/CSScheme
