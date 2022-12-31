# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.10.1e-ph3sx]

### Added

+ Added syntax highlighting for anything written as `ObjXX_XX`

### Fixed

+ Corrected `ObjParticleList_SetAngleXYZ` to `ObjParticleList_SetAngle` in the language server
+ Added syntax highlighting to the `=` symbol (how did I miss this?)

## [1.10.1d-ph3sx]

### Fixed

+ Corrected a typo in `Float_CopySign` (thanks again Mugenri)

## [1.10.1c-ph3sx]

### Fixed

+ Fixed an issue where variable declarators would still highlight even if they were a substring of another word (thanks again Mugenri)

## [1.10.1b-ph3sx]

### Added

+ Added a function reference for `ObjMove_SetAngularAcceleration` (thank you Mugenri!)
+ Added syntax highlighting for the `func` function declaration

### Changed

+ Made `local` highlight in the same style and scope as `function`, `task`, etc. since it's a block declarator

### Fixed

+ Fixed a typo on the notes for `ObjSound_SetRestartEnable` (thanks again Mugenri)

## [1.10.1-ph3sx]

### Added

+ Added syntax for <kbd>VK</kbd> and <kbd>KEY</kbd> enums
+ Added syntax for <kbd>ALIGNMENT</kbd> enums
+ Added syntax for <kbd>FILTER</kbd> enums
+ Added syntax for <kbd>OBJ</kbd> enums
+ Added syntax for <kbd>LERP</kbd> enums
+ Added syntax for <kbd>TYPE</kbd> enums ("scripttype" and "shottype" scopes)
+ Added syntax for <kbd>BLEND_ALPHA_INV</kbd> in the "blendtype" enum scope
+ Added syntax for <kbd>NO_CHANGE</kbd> in the "other" enum scope

### Fixed

+ Fixed a typo in <kbd>ObjCrLaser_GetNodePosition</kbd>
+ Fixed an issue where variable declarations in for, for-each, ascent, and descent loops wouldn't highlight

## [1.10.0i-ph3sx]

### Added

+ Added the function <kbd>ObjParticleList_SetExtraData</kbd> into the language server (because I forgot lol)
+ Added the Japanese header (<kbd>東方弾幕風</kbd>) into the syntax

### Changed

+ Smoothed out some redundancy for the previous update's <kbd>const</kbd> fix.

## [1.10.0h-ph3sx]

### Fixed

+ Fixed an issue where variable types declared as constants wouldn't have their respective type highlighted (e.g. the "int" in const int, etc.)
+ Fixed the notes for <kbd>typeof</kbd> and <kbd>ftypeof</kbd> not appearing in a list format

## [1.10.0g-ph3sx]

### Added

+ Added variable declaration for "const" (I can't believe I forgot this)

## [1.10.0f-ph3sx]

### Added

+ Included entries for SetUserReplayData and GetUserReplayData (These are currently undocumented, so please let me know if I screwed up any argument types or something)

### Fixed

+ Fixed an issue where > and >= wouldn't highlight
+ Fixed an issue where the for, for-each, ascent, and descent snippets would label the contect argument as argument 3 when it sould be 4, causing the actual 3rd argument to populate in the content as well

## [1.10.0e-ph3sx]

### Fixed

+ Fixed a copy-paste error where the "wait" function's input type was labelled as "number (Object ID)" instead of "number (int)"

## [1.10.0d-ph3sx]

### Added

+ Syntax highlighting for default ph3sx functions
+ A small Python script that takes the source functions file and puts all the function names into a file (not too necessary, but figured I'd include it since I used it)

## [1.10.0c-ph3sx]

### Fixed

+ Fixed a typo in the description of UnloadScriptFromCache

## [1.10.0b-ph3sx]

### Added

+ Snippet for descent

### Changed

+ Snippets for for, for-each, ascent, and descent loops now contain 3 arguments that can be tabbed across **(i** in **0**..**10**)

### Fixed

+ Fixed a grammatical error in the for, for-each, and ascent loops

## [1.10.0-ph3sx] - 2022-08-12

### Added

+ All ph3sx functions as of engine version 1.32b
+ Syntax for all ph3sx loop types, veriable declarations, constants, and more
+ Snippets for for loops, for-each loops, async, and functions with return types

### Changed

+ Updated all original ph3 functions that have been modified in ph3sx
+ Updated dependencies

### Fixed

+ Fixed all function entries that contained outdated or copy-paste errors


## [Unreleased]

## [1.10.0] - 2020-02-06

### Changed

+ Updated the ph3 function reference
+ Updated dependencies

### Fixed

+ Fixed the `alternative` snippet (contribution by user ooa113y)

## [1.9.0] - 2019-10-24

### Changed

+ Updated the ph3 function reference
+ Updated dependencies

## [1.8.0] - 2019-07-18

### Changed

+ Updated dependencies

## [1.7.0] - 2019-07-05

### Changed

+ Updated ph3 function reference
+ Updated dependencies

## [1.6.0] - 2019-05-07

### Changed

+ Updated dependencies

## [1.5.1] - 2019-03-11

### Fixed

+ Fixed language server not working by including `semver` in the extension
  package

## [1.5.0] - 2019-03-06

### Changed

+ Reintroduced support for unsaved files
+ Updated tooling
+ Refactored code

## [1.4.0] - 2019-02-28

### Changed

+ Updated ph3 function reference
+ Updated Travis CI configuration
+ Updated dependencies

## [1.3.0] - 2018-07-15

### Changed

+ Updated ph3 function reference
+ Adjusted copyright notices in license to comply with the standard
+ Updated dependencies

## [1.2.0] - 2018-06-28

### Added

+ Added basic shot and item data support
+ Refactored JSON processing
+ Added VS Code Marketplace link in form of a badge

### Changed

+ Adjusted/expanded readme
+ Updated dependencies

## [1.1.0] - 2018-06-27

### Added

+ Added language server for code completion and on-demand documentation on
  hover
+ Added snippets

## [1.0.3] - 2018-06-23

### Removed

+ Removed unnecessary `fileTypes` section in `syntaxes/dnh.tmLanguage.json`

### Fixed

+ Fixed `TouhouDanmakufu` header not getting highlighted

## [1.0.2] - 2018-06-23

### Fixed

+ Reduced amount of keywords in `package.json`
+ Corrected `galleryBanner.theme` to `dark`

## [1.0.1] - 2018-06-23

### Added

+ Added extension icon to `README.md` for some flair

### Fixed

+ Added the correct keywords in `package.json`

## 1.0.0 - 2018-06-23

### Added

+ Initial release

[Unreleased]: https://github.com/mserajnik/dnh/compare/1.10.0...develop
[1.10.0]: https://github.com/mserajnik/dnh/compare/1.9.0...1.10.0
[1.9.0]: https://github.com/mserajnik/dnh/compare/1.8.0...1.9.0
[1.8.0]: https://github.com/mserajnik/dnh/compare/1.7.0...1.8.0
[1.7.0]: https://github.com/mserajnik/dnh/compare/1.6.0...1.7.0
[1.6.0]: https://github.com/mserajnik/dnh/compare/1.5.1...1.6.0
[1.5.1]: https://github.com/mserajnik/dnh/compare/1.5.0...1.5.1
[1.5.0]: https://github.com/mserajnik/dnh/compare/1.4.0...1.5.0
[1.4.0]: https://github.com/mserajnik/dnh/compare/1.3.0...1.4.0
[1.3.0]: https://github.com/mserajnik/dnh/compare/1.2.0...1.3.0
[1.2.0]: https://github.com/mserajnik/dnh/compare/1.1.0...1.2.0
[1.1.0]: https://github.com/mserajnik/dnh/compare/1.0.3...1.1.0
[1.0.3]: https://github.com/mserajnik/dnh/compare/1.0.2...1.0.3
[1.0.2]: https://github.com/mserajnik/dnh/compare/1.0.1...1.0.2
[1.0.1]: https://github.com/mserajnik/dnh/compare/1.0.0...1.0.1
