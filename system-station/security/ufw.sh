#!/bin/sh

# UFW

# Uncomplicated Firewall (UFW) is a program for managing a netfilter firewall
# designed to be easy to use. It uses a command-line interface consisting
# of a small number of simple commands, and uses iptables for configuration.

set -e

ufw_rules() {
    sudo ufw status verbose
}

ufw_apps() {
    sudo ufw app list
}

ufw_deleterule() {
    sudo ufw status numbered
    echo "Enter rule number to delete:"
    read num
    sudo ufw delete "$num" # or use sudo ufw delete <allow app>
}

ufw_installapps() {
    sudo cp -r ./ufw /etc/ufw
}

case "$1" in
    rules)
        ufw_rules
        ;;
    apps)
        ufw_apps
        ;;
    delete)
        ufw_deleterule
        ;;
    installapps)
        ufw_installapps
        ;;
    *)
        echo "Invalid command"
        exit 1
        ;;
esac
