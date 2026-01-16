CC := gcc
CXX := g++
CFLAGS := -Wall -Wextra -pedantic -O2
CXXFLAGS := -Wall -Wextra -pedantic -O2 -std=c++20

TARGETS := server weather

server: server.c
ifeq ($(OS), Windows_NT)
	$(CXX) $(CXXFLAGS) $< -o $@ -lws2_32
else
	$(CXX) $(CXXFLAGS) $< -o $@
endif

weather: weather.c
	$(CC) $(CFLAGS) $< -o $@ -lcurl
