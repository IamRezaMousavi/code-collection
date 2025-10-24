#!/bin/sh

windres icon.rc icon.o
gcc main.c icon.o

