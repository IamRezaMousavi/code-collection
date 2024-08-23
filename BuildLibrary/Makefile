# Variables
CC = gcc
CFLAGS = -Wall -Iinclude -fPIC
SRC_DIR = src
LIB_DIR = lib
LIB_NAME = print

STATIC_LIB = $(LIB_DIR)/lib$(LIB_NAME).a
SHARED_LIB = $(LIB_DIR)/lib$(LIB_NAME).so

# Default Target
all: build_static build_dynamic

$(LIB_DIR):
	mkdir -p $(LIB_DIR)

$(LIB_DIR)/$(LIB_NAME).o: $(SRC_DIR)/$(LIB_NAME).c | $(LIB_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

static: $(STATIC_LIB)

$(STATIC_LIB): $(LIB_DIR)/$(LIB_NAME).o
	ar rcs $@ $^

dynamic: $(SHARED_LIB)

$(SHARED_LIB): $(LIB_DIR)/$(LIB_NAME).o
	$(CC) -shared -o $@ $^

build_static: main.c static
	$(CC) $(CFLAGS) -o main_static main.c $(STATIC_LIB) --static

build_dynamic: main.c dynamic
	$(CC) $(CFLAGS) -o main_dynamic main.c -L$(LIB_DIR) -l$(LIB_NAME)

clean:
	rm -f $(LIB_DIR)/* main_static main_dynamic

.PHONY: all static dynamic build_static build_dynamic clean
