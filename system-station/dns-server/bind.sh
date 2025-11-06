#!/bin/sh

set -e

bind_install() {
    cp -r ./bind /etc/bind
    sudo named-checkconf
    sudo named-checkzone cloud99p.org /etc/bind/zones/db.cloud99p.org

    sudo systemctl restart bind9
    sudo ufw allow Bind9
}

case "$1" in
    install)
        bind_install
        ;;
    
    *)
        echo "Invalid command"
        exit 1
        ;;
esac
