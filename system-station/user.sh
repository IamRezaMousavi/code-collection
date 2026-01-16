#!/bin/sh

# Users and Groups

set -e

# Create new user
#   -m used to create user home dir.
user_create() {
    useradd -m $1
}

# Delete user
#   -r used to delete user home dir.
user_delete() {
    userdel -r $1
}

# Change user password
user_chpw() {
    passwd $1
}

# Rename user
#   $2 is new username
user_rename() {
    usermod -l $2 $1
}

# Lock user
user_lock() {
    usermod -L $1
}

# Unlock user
user_unlock() {
    usermod -U $1
}

# Change user shell
#   $2 is abs path of shell. (eq: /bin/bash)
user_chsh() {
    usermod -s $2 $1
}

# Show user info
user_info() {
    id $1
}

# List users
user_list() {
    cat /etc/passwd
}

# List user groups
user_listgroups() {
    groups $1
}

# Create new group
group_create() {
    groupadd $1
}

# Delete group
group_delete() {
    groupdel $1
}

# Add user to group
#   $2 is username
group_adduser() {
    usermod -aG $1 $2
}

# Delete user from group
#   $2 is username
group_deluser() {
    gpasswd -d $2 $1
}

# List groups
group_list() {
    cat /etc/group
}

case "$1" in
    create)
        user_create "$2"
        ;;
    delete)
        user_delete "$2"
        ;;
    chpw)
        user_chpw "$2"
        ;;
    rename)
        user_rename "$2" "$3"
        ;;
    lock)
        user_lock "$2"
        ;;
    unlock)
        user_unlock "$2"
        ;;
    chsh)
        user_chsh "$2" "$3"
        ;;
    info)
        user_info "$2"
        ;;
    list)
        user_list
        ;;
    listgroups)
        user_listgroups "$2"
        ;;
    gcreate)
        group_create "$2"
        ;;
    gdelete)
        group_delete "$2"
        ;;
    gadduser)
        group_adduser "$2" "$3"
        ;;
    gdeluser)
        group_deluser "$2" "$3"
        ;;
    glist)
        group_list
        ;;
    *)
        echo "Invalid command"
        exit 1
        ;;
esac
