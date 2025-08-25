##### Toolchain #####
CC 		=	cc
CFLAGS := -Wall -fPIC
LDFLAGS := -shared

ifeq ($(OS),Windows_NT)
	LIB = mylib.dll
else
	LIB = libmylib.so
endif

all:  $(LIB)

$(LIB): mylib.c
	$(CC) $(CFLAGS) mylib.c -o $@ $(LDFLAGS)

clean:
	rm -f *.so *.dll
