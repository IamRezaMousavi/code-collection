appname=hashtable

CXX=gcc
RM=rm -rf
CXXFLAGS=-O2 -Wall -Wextra -pedantic `pkg-config --cflags glib-2.0`
LDLIBS=`pkg-config --libs glib-2.0`

SRCS=*.c

all:
	mkdir -p build/
	$(CXX) $(CXXFLAGS) $(SRCS) -o build/$(appname) $(LDLIBS)

clean:
	$(RM) build/
