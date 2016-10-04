# Naomi

[![Sublime version](https://img.shields.io/badge/sublime%203->%3D3084-orange.svg?style=flat-square)][sublime]
[![License](http://img.shields.io/:license-apache-blue.svg?style=flat-square)](LICENSE.md)

Package designed to provide easy to extend syntax highlighting and other stuff
that makes writting more fun.

## Features

#### General

* Auto complete asterisks in documentation blocks.
* Add Mac’s curly quotes shortcuts for Windows and Linux:
    1. Alt+[ produces “.
    2. Alt+Shift+[ produces ”.
    3. Alt+] produces ‘.
    4. Alt+Shift+] produces ’.

#### FJSX15 (ES2015 + FlowType + React’s JSX - Experimental)

* Combines the 3 syntaxes.
* Classes.
* Interfaces.
* Templates.
* Destructure operator.
* Generator functions.
* Arrow functions.
* Get, set and static functions.
* Decimal, floating point and hexadecimal literal.

#### HTML 5 (Experimental)

* Highlight FJSX15 inside `<script type="text/babel">` tags.
* Balanced tags.
* Section root elements.
* Embedded elements.
* Form elements.

#### MQL4

* Decimal, floating point and hexadecimal literal.
* RGB literal.
* Alternating escaped characters.

#### PHP 7

* phpDoc instructions.
* Decimal, floating point, binary, octal and hexadecimal literal.
* Alternating namespace names.
* Alternating escaped characters.
* Alternating embedded variables.
* Alternating parenthesis in expressions.
* Extended class and implemented interfaces.
* Specific scope for private and protected modifiers.

#### XML 1.0 (Experimental)

* Balanced tags.

## Installation

#### Package Control

1. Install [Package Control](https://packagecontrol.io/installation).
2. Run **Package Control: Install Package** command.
3. Find and install the **Naomi** plugin.
4. Restart Sublime Text if there are issues.

#### Manual

Clone the repository in your Sublime Text “Packages” directory:

    git clone https://github.com/borela/naomi.git Naomi

The “Packages” directory is located at:

* **OS X**: `~/Library/Application Support/Sublime Text 3/Packages`
* **Linux**: `~/.config/sublime-text-3/Packages`
* **Windows**: `%APPDATA%\Sublime Text 3\Packages`

## Usage

1. Go to the menu `View / Syntax / Naomi / ...` to select the new syntax.
2. Select a color scheme provided in `Preferences / Color Scheme / Naomi`.

#### Notes

You aren’t required to use the color schemes provided but keep in mind
that not all features listed before are going to work with other color schemes.
Also, be aware of auto completion conflicts provided by other packages, you may
need to disable them.

## Preview

#### FJSX15 (ES2015 + FlowType + React’s JSX)

![Candyman FJSX15 preview 1](./preview/fjsx15/candyman-1.png)

#### HTML 5

![Candyman HTML5 preview 1](./preview/html5/candyman-1.png)

#### PHP 7

![Candyman PHP 7 preview 1](./preview/php7/candyman-3.png)

[sublime]: http://www.sublimetext.com/
