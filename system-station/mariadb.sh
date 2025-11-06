#!/bin/sh

set -e

mariadb_install() {
    sudo apt install mariadb-server
    sudo mysql_secure_installation
}

mariadb_createuser() {
    mariadb -u root -p < db-user.sql
}

case "$1" in
    install)
        mariadb_install
        ;;
    
    createuser)
        mariadb_createuser
        ;;
    
    *)
        echo "Invalid command"
        exit 1
        ;;
esac
