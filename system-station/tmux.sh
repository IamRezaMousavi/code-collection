#!/bin/sh

### Terminal Multiplexer

# - [tmux](https://github.com/tmux/tmux/wiki):
#   tmux is a terminal multiplexer.
#   It lets you switch easily between several programs in one terminal,
#   detach them (they keep running in the background) and reattach them to a different terminal.
#   [github](https://github.com/tmux/tmux) `ISC` `C`
#   - arch: `tmux`

set -e

# List sessions
tmux_list() {
    tmux ls
}

# New session
tmux_new() {
    tmux new -s $1
}

# Attach session
tmux_attach() {
    tmux a -t $1
}

# Rename session
tmux_rename() {
    tmux rename-session -t $1 $2
}

# Kill session
tmux_kill() {
    tmux kill-session $1
}

case "$1" in
    list)
        tmux_list
        ;;
    new)
        tmux_new $2
        ;;
    attach)
        tmux_attach $2
        ;;
    rename)
        tmux_rename $2 $3
        ;;
    kill)
        tmux_kill $2
        ;;
    *)
        echo "Invalid command"
        exit 1
        ;;
esac
