# BuildLibrary

How to Build Library in C?

---

## Build

Build Options:

1. Static Lib Build

```sh
make static
```

2. Dynamic Lib Build

```sh
make dynamic
```

3. Static main.c Build

```sh
make build_static
./main_static
```

4. Dynamic main.c Build

```sh
make dynamic_static
LD_LIBRARY_PATH=./lib:$LD_LIBRARY_PATH ./main_dynamic
```

---
