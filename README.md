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
[![All Contributors](https://img.shields.io/badge/all_contributors-25-orange.svg?style=flat-square)](#contributors)
[![Downloads](https://img.shields.io/packagecontrol/dt/Naomi.svg?style=flat-square)][package-control]

Enhanced syntax definitions for Sublime Text 3.

[![preview](art/main-preview.png)][naomi]

## What’s included

### Color Schemes

* Candyman;

### Syntaxes

* CSS 3+;
* JavaScript;
  * [Stage 0-3 proposals](//github.com/tc39/proposals);
  * [Node globals](//nodejs.org/api/globals.html);
  * [Jest globals](//facebook.github.io/jest/docs/en/api.html);
  * [Flow](//flow.org);
  * [JSX](//reactjs.org/docs/introducing-jsx.html) with complete support for
    [Emmet](//github.com/sergeche/emmet-sublime);
* HTML 5+;
* MQL4 (Updating);
* Jest Snapshot;
* PHP 7+ (Updating);
* SCSS (Updating);

### Enhanced Go To Symbol

* **Windows or Linux**: `Ctrl+R`;
* **OSX**: `⌘ + R`;

[![go-to-symbol](art/go-to-symbol.png)][naomi]

### OSX’s curly quotes for Windows and Linux

* `Alt+[` produces “.
* `Alt+Shift+[` produces ”.
* `Alt+]` produces ‘.
* `Alt+Shift+]` produces ’.

### Other enhancements

* JS/JSX comment toggle;
* Pressing enter between `()`, `[]`, `""`, `''` and ``` `` ```  will have the same
  behavior as `{}`;

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

After installing the plugin and restarting Sublime, it will automatically use
the syntaxes contained in this package.

You can also set them manually through:

  1. Go to the “View” menu;
  2. Then “Syntax”;
  3. Finally “Naomi”;

Or:

  1. Click at the bottom right corner where it shows the current syntax;
  2. Then “Naomi”.

## Contributors

Thanks goes to these wonderful people ([emoji legend][emoji-legend]):

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/borela"><img src="https://avatars3.githubusercontent.com/u/11317458?v=4" width="100px;" alt="Alexandre Borela"/><br /><sub><b>Alexandre Borela</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Aborela" title="Bug reports">🐛</a> <a href="https://github.com/borela/naomi/commits?author=borela" title="Code">💻</a> <a href="#design-borela" title="Design">🎨</a> <a href="https://github.com/borela/naomi/commits?author=borela" title="Documentation">📖</a></td>
    <td align="center"><a href="http://cjwinslow.com"><img src="https://avatars0.githubusercontent.com/u/1581943?v=4" width="100px;" alt="C.J. Winslow"/><br /><sub><b>C.J. Winslow</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3AWhoaa512" title="Bug reports">🐛</a> <a href="https://github.com/borela/naomi/commits?author=Whoaa512" title="Code">💻</a> <a href="#ideas-Whoaa512" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://faiwer.ru"><img src="https://avatars1.githubusercontent.com/u/744114?v=4" width="100px;" alt="faiwer"/><br /><sub><b>faiwer</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Afaiwer" title="Bug reports">🐛</a> <a href="#ideas-faiwer" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://www.betafabric.com/francisco/"><img src="https://avatars0.githubusercontent.com/u/208149?v=4" width="100px;" alt="Francisco Lourenço"/><br /><sub><b>Francisco Lourenço</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Afranciscolourenco" title="Bug reports">🐛</a> <a href="https://github.com/borela/naomi/commits?author=franciscolourenco" title="Code">💻</a></td>
    <td align="center"><a href="https://butternutbox.com/"><img src="https://avatars0.githubusercontent.com/u/9534622?v=4" width="100px;" alt="Tomas Barry"/><br /><sub><b>Tomas Barry</b></sub></a><br /><a href="https://github.com/borela/naomi/commits?author=TomasBarry" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/crapthings"><img src="https://avatars2.githubusercontent.com/u/1147704?v=4" width="100px;" alt="crapthings"/><br /><sub><b>crapthings</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Acrapthings" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://memcrab.com"><img src="https://avatars3.githubusercontent.com/u/1213198?v=4" width="100px;" alt="Max Mykhailenko"/><br /><sub><b>Max Mykhailenko</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Amax-mykhailenko" title="Bug reports">🐛</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/2Pacalypse-"><img src="https://avatars3.githubusercontent.com/u/4757944?v=4" width="100px;" alt="Marko Žarković"/><br /><sub><b>Marko Žarković</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3A2Pacalypse-" title="Bug reports">🐛</a> <a href="#ideas-2Pacalypse-" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="http://neaumusic.github.io"><img src="https://avatars0.githubusercontent.com/u/3423750?v=4" width="100px;" alt="James Wilson"/><br /><sub><b>James Wilson</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Aneaumusic" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/ericbiewener"><img src="https://avatars2.githubusercontent.com/u/253298?v=4" width="100px;" alt="ericbiewener"/><br /><sub><b>ericbiewener</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Aericbiewener" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://lematt1991.github.io/"><img src="https://avatars1.githubusercontent.com/u/13142923?v=4" width="100px;" alt="Matt Le"/><br /><sub><b>Matt Le</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Alematt1991" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/clark-pan"><img src="https://avatars0.githubusercontent.com/u/1161431?v=4" width="100px;" alt="Clark Pan"/><br /><sub><b>Clark Pan</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Aclark-pan" title="Bug reports">🐛</a> <a href="#ideas-clark-pan" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://octetstream.me"><img src="https://avatars3.githubusercontent.com/u/7884558?v=4" width="100px;" alt="Nick K."/><br /><sub><b>Nick K.</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Aoctet-stream" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://eventa.mx"><img src="https://avatars3.githubusercontent.com/u/4448627?v=4" width="100px;" alt="Alex Cavazos"/><br /><sub><b>Alex Cavazos</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3AAlexKvazos" title="Bug reports">🐛</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://divisionof.com"><img src="https://avatars3.githubusercontent.com/u/6924108?v=4" width="100px;" alt="Enrique Ballesté"/><br /><sub><b>Enrique Ballesté</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Aeballeste" title="Bug reports">🐛</a> <a href="#ideas-eballeste" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="http://themaingate.net"><img src="https://avatars0.githubusercontent.com/u/120596?v=4" width="100px;" alt="David Calhoun"/><br /><sub><b>David Calhoun</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Adavidcalhoun" title="Bug reports">🐛</a> <a href="#ideas-davidcalhoun" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/StreetStrider"><img src="https://avatars3.githubusercontent.com/u/2124761?v=4" width="100px;" alt="Strider"/><br /><sub><b>Strider</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3AStreetStrider" title="Bug reports">🐛</a> <a href="#ideas-StreetStrider" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/borela/naomi/commits?author=StreetStrider" title="Code">💻</a></td>
    <td align="center"><a href="http://mauricioandrades.com/"><img src="https://avatars0.githubusercontent.com/u/4704508?v=4" width="100px;" alt="Mauricio Andrades"/><br /><sub><b>Mauricio Andrades</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3AMauricioAndrades" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://blog.gerardroche.com"><img src="https://avatars3.githubusercontent.com/u/44148?v=4" width="100px;" alt="Gerard Roche"/><br /><sub><b>Gerard Roche</b></sub></a><br /><a href="https://github.com/borela/naomi/commits?author=gerardroche" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ihodev"><img src="https://avatars1.githubusercontent.com/u/9801624?v=4" width="100px;" alt="Ihor Oleksandrov"/><br /><sub><b>Ihor Oleksandrov</b></sub></a><br /><a href="https://github.com/borela/naomi/commits?author=ihodev" title="Code">💻</a> <a href="#design-ihodev" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/seanders"><img src="https://avatars0.githubusercontent.com/u/2849183?v=4" width="100px;" alt="Sean Miller"/><br /><sub><b>Sean Miller</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3Aseanders" title="Bug reports">🐛</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://yurigor.com/"><img src="https://avatars0.githubusercontent.com/u/6861317?v=4" width="100px;" alt="YuriGor"/><br /><sub><b>YuriGor</b></sub></a><br /><a href="https://github.com/borela/naomi/issues?q=author%3AYuriGor" title="Bug reports">🐛</a> <a href="#ideas-YuriGor" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="http://mellow.sh"><img src="https://avatars2.githubusercontent.com/u/1474821?v=4" width="100px;" alt="not"/><br /><sub><b>not</b></sub></a><br /><a href="https://github.com/borela/naomi/commits?author=mvllow" title="Code">💻</a></td>
    <td align="center"><a href="http://kevinghadyani.info"><img src="https://avatars1.githubusercontent.com/u/3948069?v=4" width="100px;" alt="Kevin Ghadyani"/><br /><sub><b>Kevin Ghadyani</b></sub></a><br /><a href="https://github.com/borela/naomi/commits?author=Sawtaytoes" title="Code">💻</a></td>
    <td align="center"><a href="https://ryankoval.com"><img src="https://avatars2.githubusercontent.com/u/1282943?v=4" width="100px;" alt="Ryan Koval"/><br /><sub><b>Ryan Koval</b></sub></a><br /><a href="https://github.com/borela/naomi/commits?author=rkoval" title="Code">💻</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors][all-contributors] specification.
Contributions of any kind are welcome!

If you are not included but created bug reports, sent ideas or patches please
send a pull request to the `.all-contributorsrc` file.

[all-contributors]: //github.com/kentcdodds/all-contributors
[candyman]: schemes/candyman
[emoji-legend]: //github.com/kentcdodds/all-contributors#emoji-key
[forks]: //github.com/borela/naomi/network/members
[issues]: //github.com/borela/naomi/issues
[naomi]: //github.com/borela/naomi
[package-control]: //packagecontrol.io/packages/Naomi
[pulls]: //github.com/borela/naomi/pulls
[stars]: //github.com/borela/naomi/stargazers
[sublime]: //www.sublimetext.com
[sublimeLinter]: //github.com/SublimeLinter/SublimeLinter3
[watchers]: //github.com/borela/naomi/watchers
