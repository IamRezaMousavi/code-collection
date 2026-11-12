PROJECT := core

SRC_DIR   := src
INC_DIR   := inc
BUILD_DIR := build

CC       := cc
CXX      := c++
CFLAGS   := -O2 -Wall -Wextra
CXXFLAGS := $(CFLAGS) -std=c++20
LDFLAGS  :=
LDLIBS   :=

TARGETS := $(BUILD_DIR)/$(PROJECT)

C_SRCS   := $(wildcard $(SRC_DIR)/*.c)
CPP_SRCS := $(wildcard $(SRC_DIR)/*.cpp)
HDRS     := $(wildcard $(INC_DIR)/*.h $(INC_DIR)/*.hpp)

C_OBJS   := $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.o,$(C_SRCS))
CPP_OBJS := $(patsubst $(SRC_DIR)/%.cpp,$(BUILD_DIR)/%.o,$(CPP_SRCS))
OBJS     := $(C_OBJS) $(CPP_OBJS)

C_DEPS   := $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.d,$(C_SRCS))
CPP_DEPS := $(patsubst $(SRC_DIR)/%.cpp,$(BUILD_DIR)/%.d,$(CPP_SRCS))
DEPS     := $(C_DEPS) $(CPP_DEPS)

Q := @
E := $(Q)echo

all: prepare $(TARGETS)

prepare:
	$(Q) mkdir -p $(BUILD_DIR)

$(TARGETS): $(OBJS)
	$(E) "  LINK     " $@
	$(Q) $(CXX) $(CXXFLAGS) $^ -o $@ $(LDFLAGS) $(LDLIBS)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c
	$(E) "  CC       " $<
	$(Q) $(CC) $(CFLAGS) -I$(INC_DIR) -MMD -MP -MF $(patsubst %.o,%.d,$@) -MT $@ -c $< -o $@

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(E) "  CXX      " $<
	$(Q) $(CXX) $(CXXFLAGS) -I$(INC_DIR) -MMD -MP -MF $(patsubst %.o,%.d,$@) -MT $@ -c $< -o $@

clean:
	$(E) "  CLEAN"
	$(Q) rm -rf $(BUILD_DIR)

-include $(DEPS)

.PHONY: all prepare clean
