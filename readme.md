## Overview

Custom themes and color schemes for Sublime Text. Uses the new `.sublime-color-scheme` format and requires **at least version 3149** of Sublime.

## Installation

Clone the repo and symlink it to your Sublime packages directory. Example for MacOS:

    git clone https://github.com/mitranim/sublime-themes.git
    cd sublime-themes
    ln -sf "$(pwd)" "$HOME/Library/Application Support/Sublime Text 3/Packages/"

To find the packages directory on your system, use Sublime Text menu → Preferences → Browse Packages.

Activate:

    Command Palette -> UI: Select Color Scheme -> Cloud
    # or
    Command Palette -> UI: Select Color Scheme -> Nether

Use the built-in Adaptive theme to match the color scheme:

    Command Palette -> UI: Select Theme -> Adaptive

## Modification

`make.py` automatically rebuilds the themes on changes in `src`.

## License

https://en.wikipedia.org/wiki/WTFPL
