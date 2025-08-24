##### Toolchain #####
CC 		=	gcc
FILE_NAME = funcs

ifeq ($(OS),Windows_NT)
	RM      =   del /F
else
	RM      =   rm -f
endif

##### Compiler options #####
CFLAGS = -Wall -fPIC -shared


all:  $(FILE_NAME).dll

$(FILE_NAME).dll:
	-$(CC) $(CFLAGS) -o  $(FILE_NAME).dll .\$(FILE_NAME).c

clean:
	@$(RM) $(FILE_NAME).dll
