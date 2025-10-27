CC = gcc
CFLAGS = -Wall -Iinclude -fPIC

LIBNAME = print
SRC = src/print.c
OBJ = $(patsubst src/%.c,%.o,$(SRC))

all: lib$(LIBNAME).a lib$(LIBNAME).so main_static main_dynamic

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -c $< -o $@

lib$(LIBNAME).a: $(OBJ)
	ar rcs lib$(LIBNAME).a $(OBJ)

lib$(LIBNAME).so: $(OBJ)
	$(CC) -shared -o lib$(LIBNAME).so $(OBJ)

main_static: main.c lib$(LIBNAME).a
	$(CC) -Iinclude main.c lib$(LIBNAME).a -o main_static

main_dynamic: main.c lib$(LIBNAME).so
	$(CC) -Iinclude main.c -L. -l$(LIBNAME) -Wl,--enable-new-dtags -Wl,-rpath=. -o main_dynamic

clean:
	rm -f *.o *.a *.so main_static main_dynamic
