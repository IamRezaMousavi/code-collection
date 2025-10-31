#!/bin/sh

if [ -z "$1" ]; then
    echo "Usage: $0 <binary_file>"
    exit 1
fi

BIN="$1"
PKG_DIR="$(basename $BIN).package"

mkdir -p "$PKG_DIR"
cp "$BIN" "$PKG_DIR/"

for dll in $(ldd "$BIN" | grep '/mingw64/bin/' | awk '{print $3}'); do
    cp "$dll" "$PKG_DIR/"
    echo "copy $dll"
done
