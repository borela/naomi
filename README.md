[![Naomi](art/logo.png)][naomi]

[![GitHub watchers](https://img.shields.io/github/watchers/borela/naomi.svg?style=social)][watchers]
[![GitHub stars](https://img.shields.io/github/stars/borela/naomi.svg?style=social)][stars]
[![GitHub issues](https://img.shields.io/github/issues/borela/naomi.svg?style=social)][issues]
[![GitHub pulls](https://img.shields.io/github/issues-pr/borela/naomi.svg?style=social)][pulls]
[![GitHub forks](https://img.shields.io/github/forks/borela/naomi.svg?style=social)][forks]

[![Package version](https://img.shields.io/github/release/borela/naomi.svg?style=flat-square)][naomi]
[![Sublime version](https://img.shields.io/badge/sublime-%E2%89%A53126-orange.svg?style=flat-square)][sublime]
[![Platforms](https://img.shields.io/badge/platforms-Windows%20%7C%20Linux%20%7C%20OSX-ff4081.svg?style=flat-square)][naomi]
[![License](https://img.shields.io/badge/license-Apache%202.0%20%7C%20BSD%20%7C%20MIT-ba68c8.svg?style=flat-square)][naomi]
[![Downloads](https://img.shields.io/packagecontrol/dt/Naomi.svg?style=flat-square)][package-control]

Enhanced syntax definitions and doc shortcuts for Sublime Text 3.

[![preview](art/main-preview.png)][naomi]

## What’s included

### Color Schemes

* Candyman;

### Syntaxes

* CSS 3+;
* Git config;
* Git ignore;
* JavaScript;
  * [Stage 0-3 proposals](//github.com/tc39/proposals);
  * [Node globals](//nodejs.org/api/globals.html);
  * [Jest globals](//facebook.github.io/jest/docs/en/api.html);
  * [Flow](//flow.org);
  * [JSX](//reactjs.org/docs/introducing-jsx.html);
* Git attributes;
* HTML 5+
* MQL4 (Updating);
* Jest Snapshot;
* PHP 7+ (Updating);
* SCSS (Updating);

### Enhanced Go To Symbol

Go to symbol with emojis:

[![go-to-symbol](art/go-to-symbol.png)][naomi]

### Mac’s curly quotes for Windows and Linux

* `Alt+[` produces “.
* `Alt+Shift+[` produces ”.
* `Alt+]` produces ‘.
* `Alt+Shift+]` produces ’.

### Docblock shortcuts

* `Enter` creates a new comment line.
* `Backspace` deletes the current line and goes to the previous one.
* `Shift+Enter` closes the docblock.
  ![Multline line docblock preview](preview/multiline.gif)

### Single line comment shortcuts

* `Shift+Enter` creates new single line comment.
* `Backspace` deletes the current line and goes to the previous one.
  ![Single line docblock preview](preview/single-line.gif)

## Installation

#### Manual installation

Clone the repository in your Sublime Text “Packages” directory:

    git clone https://github.com/borela/naomi.git Naomi

The “Packages” directory is located at:

* **OS X**: `~/Library/Application Support/Sublime Text 3/Packages`
* **Linux**: `~/.config/sublime-text-3/Packages`
* **Windows**: `%APPDATA%\Sublime Text 3\Packages`

#### Installing using Package Control

1. Install [Package Control](https://packagecontrol.io/installation).
2. Run **Package Control: Install Package** command.
3. Find and install the **Naomi** plugin.
4. Restart Sublime Text.

## Usage

To the use syntaxes available you can:

  1. Go to the “View” menu;
  2. Then “Syntax”;
  3. Finally “Naomi”;

Or:

  1. Click at the bottom right corner where it shows the current syntax;
  2. Then “Naomi”.

[candyman]: schemes/candyman
[package-control]: //packagecontrol.io/packages/Naomi
[sublime]: //www.sublimetext.com
[naomi]: //github.com/borela/naomi
[issues]: //github.com/borela/naomi/issues
[pulls]: //github.com/borela/naomi/pulls
[stars]: //github.com/borela/naomi/stargazers
[watchers]: //github.com/borela/naomi/watchers
[forks]: //github.com/borela/naomi/network/members
[sublimeLinter]: //github.com/SublimeLinter/SublimeLinter3
