TARGET := sha3-512
CXX := g++
CXXFLAGS := -Wall -O2 -std=c++17
LIBS := -lcrypto

SRC := main.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET) $(LIBS)

clean:
	rm -rf $(TARGET)

.PHONY: all clean
