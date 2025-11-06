#!/bin/sh

# Terminal Emulator

# - [Alacritty](https://alacritty.org/):
#   Alacritty is a modern terminal emulator that comes with sensible defaults,
#   but allows for extensive configuration.
#   [github](https://github.com/alacritty/alacritty) `MIT-or-Apache-2.0` `Rust`
#     - arch: `alacritty`

# - [Windows Terminal](https://aka.ms/terminal):
#   The new Windows Terminal and the original Windows console host, all in the same place!
#   [github](https://github.com/microsoft/terminal) `MIT` `C++`
#     - winget: `--id Microsoft.WindowsTerminal -e`

set -e

alacritty_setup() {
  mkdir -p ~/.config/alacritty
  cp ./alacritty.toml ~/.config/alacritty
}

case "$1" in
  alacritty_setup)
    alacritty_setup
    ;;
  *)
    echo "Invalid command"
    exit 1
    ;;
esac
