#!/bin/sh

# Editor

# A text editor is a type of computer program that edits plain text.
# [wikipedia](https://en.wikipedia.org/wiki/Text_editor)

# A source-code editor is a text editor program designed specifically
# for editing source code of computer programs.
# [wikipedia](https://en.wikipedia.org/wiki/Source-code_editor)

set -e

# - [Vim](https://www.vim.org/):
#   Vim is a highly configurable text editor built to
#   make creating and changing any kind of text very efficient.
#   [github](https://github.com/vim/vim) `Vim` `C`
#       - arch: `vim`

# - [Neovim](https://neovim.io/):
#   Vim-fork focused on extensibility and usability.
#   [github](https://github.com/neovim/neovim) `Apache 2.0` `C`
#       - arch: `neovim`
nvim_setup() {
    cp -r ./nvim ~/.config/
}

case "$1" in
    nvimsetup)
        nvim_setup
        ;;
    *)
        echo "Invalid command"
        exit 1
        ;;
esac
