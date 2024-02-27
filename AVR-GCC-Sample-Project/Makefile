AVR_GCC_PATH = ..\avr8-gnu\bin

CC = $(AVR_GCC_PATH)\avr-gcc.exe
OBJCOPY = $(AVR_GCC_PATH)\avr-objcopy.exe
SIZE = $(AVR_GCC_PATH)\avr-size.exe
REMOVE = del

MCU = atmega16
F_CPU = 

FORMAT = ihex

INCLUDE = .
OPTLEVEL = 
STD = 


CFLAGS = -mmcu=$(MCU)
ifneq ($(F_CPU), )
	CFLAGS += -DF_CPU=$(F_CPU)UL
endif
CFLAGS += -O$(OPTLEVEL)
CFLAGS += -Wall
CFLAGS += -I$(INCLUDE)
ifneq ($(STD), )
	CFLAGS += -std=$(STD)
endif

all: $(CC) $(SRC).c
	@$(CC) $(CFLAGS) $(SRC).c -o .$(SRC).elf
	@$(OBJCOPY) -O $(FORMAT) -j .text -j .data .\.$(SRC).elf $(SRC).hex
	@$(REMOVE) .\.$(SRC).elf

size: $(SIZE) $(CC) $(SRC).c
	@$(CC) $(CFLAGS) $(SRC).c -o .$(SRC).elf
	@$(SIZE) -C --mcu=$(MCU) .$(SRC).elf
	@$(REMOVE) .$(SRC).elf

clean:
	@$(REMOVE) .\$(SRC).hex
