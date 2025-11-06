#!/bin/sh

### Cryptography

# Encryption software is software that uses cryptography
# to prevent unauthorized access to digital information.
# Cryptography is used to protect digital information
# on computers as well as the digital information
# that is sent to other computers over the Internet.
# [wikipedia](https://en.wikipedia.org/wiki/Encryption_software)

#   - [GnuPG](https://gnupg.org/):
#       GnuPG is a complete and free implementation of the OpenPGP standard
#       as defined by RFC4880 (also known as PGP). GnuPG allows you to encrypt
#       and sign your data and communications; it features a versatile key management system,
#       along with access modules for all kinds of public key directories.
#       [source-code](https://git.gnupg.org/) `GPL-3.0-or-later` `C`
#       - arch: `gnupg`

set -e

gpg_genkey() {
    gpg --gen-key # or --full-generate-key
}

# output file has .gpg extension
gpg_encrypt() {
    local recipient="$1"
    local file="$2"

    if [[ -z "$recipient" || -z "$file" ]]; then
        echo "usage: encrypt <recipient_email> <file>"
        return 1
    fi

    gpg --encrypt --recipient "$recipient" "$file"
}

gpg_decrypt() {
    local file="$1"
    local output="$2"

    if [[ -z "$file" ]]; then
        echo "usage: decrypt <file> [output]"
        return 1
    fi

    if [[ -z "$output" ]]; then
        gpg --decrypt "$file"
    else
        gpg  --output "$output" --decrypt "$file"
    fi
    echo "Done"
}

# output file has .sig extension
gpg_sign() {
    local file="$1"

    if [[ -z "$file" ]]; then
        echo "usage: sign <file>"
        return 1
    fi

    gpg --sign "$file"
}

# input file has .gpg extension
gpg_verify() {
    local file="$1"

    if [[ -z "$file" ]]; then
        echo "usage: verify <file>"
        return 1
    fi

    gpg --verify "$file"
}

gpg_exportkey() {
    local recipient="$1"

    if [[ -z "$recipient" ]]; then
        echo "usage: export <recipient_email>"
        return 1
    fi

    gpg --export --armor "$recipient" --output public_key.asc
    gpg --export-secret-keys --armor --output private_key.asc
}

gpg_importkey() {
    local keyfile="$1"

    if [[ -z "$keyfile" ]]; then
        echo "usage: import <key_file>"
        return 1
    fi

    gpg --import "$keyfile"
}

gpg_listkeys() {
    gpg --list-keys
}

gpg_editkey() {
    local keyid="$1"

    if [[ -z "$keyid" ]]; then
        echo "usage: editkey <key_id>"
        return 1
    fi

    gpg --edit-key "$keyid"
}

# Git GPG signing allows you to sign your commits
# and tags to ensure their authenticity.
# By signing your commits with GPG, others can verify
# that the commits were made by you and haven't been tampered with.
# On github.com, you need to use your verified email address associated with your account.
gpg_gitconfig() {
    local keyid="${1:-}"
    if [[ -z "$keyid" ]]; then
        echo "usage: gitconfig <key_id>"
        return 1
    fi

    # If you have previously configured Git to use
    # a different key format when signing with --gpg-sign,
    # unset this configuration so the default format of openpgp will be used.
    git config --global --unset gpg.format
    git config --global user.signingkey "$keyid"

    # Enable signing your commit automaticly
    # or manually use git commit -S -m "Your commit message"
    git config --global commit.gpgsign true
    echo "Git is now sign your commits with $keyid"
}

case "$1" in
    genkey)
        gpg_genkey
        ;;
    encrypt)
        gpg_encrypt "$2" "$3"
        ;;
    decrypt)
        gpg_decrypt "$2" "$3"
        ;;
    sign)
        gpg_sign "$2"
        ;;
    verify)
        gpg_verify "$2"
        ;;
    export)
        gpg_exportkey "$2"
        ;;
    import)
        gpg_importkey "$2"
        ;;
    list)
        gpg_listkeys
        ;;
    editkey)
        gpg_editkey "$2"
        ;;
    gitconfig)
        gpg_gitconfig "$2"
        ;;
    *)
        echo "Invalid command"
        exit 1
        ;;
esac
