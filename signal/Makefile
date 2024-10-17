appname=signal-handler

CXX=gcc
RM=rm -rf
CXXFLAGS=-O2 -Wall -Wextra -pedantic
LDLIBS=

SRCS=*.c

all:
	mkdir -p build/
	$(CXX) $(CXXFLAGS) $(SRCS) -o build/$(appname) $(LDLIBS)

clean:
	$(RM) build/
