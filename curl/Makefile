appname=github-commits

CXX=gcc
RM=rm -rf
CXXFLAGS=-O2 -Wall -Wextra -pedantic
LDLIBS=-lcurl -ljansson

SRCS=*.c

all:
	mkdir -p build/
	$(CXX) $(CXXFLAGS) $(SRCS) -o build/$(appname) $(LDLIBS)

clean:
	$(RM) build/
