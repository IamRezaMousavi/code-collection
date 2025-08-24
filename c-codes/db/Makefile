appname=db

CXX=g++
RM=rm -rf
CXXFLAGS=-Wall -O3
LDLIBS=-lsqlite3

SRCS=*.cpp

all:
	mkdir -p build/
	$(CXX) $(CXXFLAGS) $(SRCS) -o build/$(appname) $(LDLIBS)

clean:
	$(RM) build/
