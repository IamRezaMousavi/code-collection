#!/bin/sh

set -e

nginx_setup() {
    cp -r ./nginx /etc/nginx
}

case "$1" in
    setup)
        nginx_setup
        ;;
    *)
        echo "Invalid command"
        exit 1
        ;;
esac
