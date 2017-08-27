#!bash
# Author: Bhishan Poudel
# Date  : Aug 24, 2017 Thu
#
# Program: Makefile for C programs
#
# Compiler, flags and Libraries
# Macport install fitsio.h in /opt/local/include/fitsio.h
# Command: gcc -Wall -o a a.c -I/usr/local/include -I/usr/include -I/opt/local/include -lm -lcfitsio -lfftw3f -lfftw3f
# Run: ./a
CC = gcc
CFLAGS = -O3 -Wall
LIB = -I/usr/local/include -I/usr/include -I/opt/local/include -lm -lcfitsio -lfftw3f -lfftw3f

# Program names separated by space and without extension
PROGRAMS = a jediaverage
ODIR = executables

# Execute run in the end
default: all
	./a
	rm -f *.o *.mod *.MOD
	mv $(PROGRAMS) $(ODIR)/

all: $(PROGRAMS)

# .o are created from .c files.
# Here, first is Target and second is Dependency.
%: %.o
	$(CC) $(CFLAGS) -o $@ $^ $(LIB)

%.o: %.c
	$(CC) $(CFLAGS) -c $<  $(LIB)

# Utility targets
.PHONY: clean

clean:
	rm -f *.o *.mod *.MOD fort.8
	rm -f *~ $(PROGRAMS)
