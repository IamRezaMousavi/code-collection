CC := gcc
CXX := g++
CFLAGS := -Wall -Wextra -pedantic -O2
CXXFLAGS := -Wall -Wextra -pedantic -O2 -std=c++20

TARGETS := crypt mariadb sqlite threadc threadcpp weather weathercpp

crypt: crypt.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ -lcrypto

mariadb: mariadb.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ -lmariadb

sqlite: sqlite.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ -lsqlite3

threadc: threadc.c
	$(CC) $(CFLAGS) $< -o $@ -lpthread

threadcpp: threadcpp.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ -lpthread

weather: weather.c
	$(CC) $(CFLAGS) $< -o $@ -lcurl

weathercpp: weathercpp.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ -lcurl
