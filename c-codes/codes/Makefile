CC := gcc
CXX := g++
CFLAGS := -Wall -Wextra -pedantic -O2
CXXFLAGS := -Wall -Wextra -pedantic -O2 -std=c++20

TARGETS := crypt mariadb server sqlite teylor threadc threadcpp weather weathercpp

crypt: crypt.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ -lcrypto

mariadb: mariadb.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ -lmariadb

server: server.c
ifeq ($(OS), Windows_NT)
	$(CXX) $(CXXFLAGS) $< -o $@ -lws2_32
else
	$(CXX) $(CXXFLAGS) $< -o $@
endif

sqlite: sqlite.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ -lsqlite3

teylor: teylor.c
	$(CC) $(CFLAGS) $< -o $@ -lm

threadc: threadc.c
	$(CC) $(CFLAGS) $< -o $@ -lpthread

threadcpp: threadcpp.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ -lpthread

weather: weather.c
	$(CC) $(CFLAGS) $< -o $@ -lcurl

weathercpp: weathercpp.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ -lcurl
