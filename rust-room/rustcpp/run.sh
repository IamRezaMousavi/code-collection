#!/bin/bash
set -e

build() {
    echo "=== Building Rust library ==="
    cd geometry
    cargo build --release
    cd ..

    echo "=== Building C++ library ==="
    cd point
    g++ -c -O2 -fPIC *.cpp -I../app
    ar rcs libpoint.a *.o
    cd ..

    echo "=== Linking executables ==="
    g++ -o app/main.out app/main.cpp \
        -Lgeometry/target/release \
        -lgeometry \
        -lpthread -ldl -lm

    g++ -o app/main1.out app/main.cpp \
        -Lpoint/ \
        -lpoint \
        -lm

    echo "Build completed successfully."
}

clean() {
    echo "=== Cleaning generated files ==="

    # Rust
    cd geometry
    cargo clean
    cd ..
    echo "Cleaned geometry dir"

    # C++ object files and static lib
    rm -f point/*.o point/libpoint.a
    echo "Cleaned point dir"

    # Executables
    rm -f app/main.out app/main1.out
    echo "Cleaned app dir"

    echo "Clean completed."
}

run() {
    build
    echo ""
    echo "=== Running programs ==="
    echo "--- main.out (Rust) ---"
    ./app/main.out
    echo ""
    echo "--- main1.out (C++) ---"
    ./app/main1.out
}

# ---------- Main ----------

case "${1:-}" in
    build)
        build
        ;;
    clean)
        clean
        ;;
    "")
        run
        ;;
    *)
        echo "Usage: $0 [build|clean]"
        echo "  $0 build   - only compile"
        echo "  $0 clean   - remove generated files"
        echo "  $0         - build and run"
        exit 1
        ;;
esac
