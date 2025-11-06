#!/bin/sh

### XMPP

# Extensible Messaging and Presence Protocol
# (abbreviation XMPP, originally named Jabber)
# is an open communication protocol designed for
# instant messaging (IM), presence information,
# and contact list maintenance.
# [wikipedia](https://en.wikipedia.org/wiki/XMPP)

#   - [Prosody](https://prosody.im/):
#       Prosody is a modern XMPP communication server.
#       [github](https://github.com/bjc/prosody) `MIT` `Lua`
#       - arch: `prosody`

set -e

prosody_install() {
    sudo apt install prosody lua-dbi-sqlite3 lua-unbound
    sudo cp /etc/prosody/prosody.cfg.lua /etc/prosody/prosody.cfg.lua.origin
    suso cp ./prosody/prosody.cfg.lua /etc/prosody/prosody.cfg.lua

    sudo certbot -d cloud99p.org --nginx
    sudo certbot -d xmpp.cloud99p.org --nginx
    sudo certbot -d share.cloud99p.org --nginx

    sudo prosodyctl --root cert import /etc/letsencrypt/live
    sudo prosodyctl adduser reza@cloud99p.org

    sudo systemctl restart prosody
}

case "$1" in
    install)
        prosody_install
        ;;

    *)
        echo "Invalid command"
        exit 1
        ;;
esac
