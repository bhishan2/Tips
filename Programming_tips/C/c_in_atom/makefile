# Author: Bhishan Poudel
# Date: Aug 24, 2017
CC=gcc -O3 -Wall -I/usr/local/include -I/usr/include -I/opt/local/include -lm -lcfitsio -lfftw3f
EXE_PATH=../executables
SRC_PATH=.

# Notes:
# Using macport to install fitsio gives /opt/local/include/fitsio.h

# Programs names separated by space and without extensions.
PROGRAMS=jedicatalog jeditransform jedidistort jedipaste jediconvolve jedirescale jedinoise jediaverage jedicolor
# execute program and clean it
default: jedi
	echo " compilation finished ... "
	rm -f *.o *.mod *.MOD
	mv $(PROGRAMS) $(EXE_PATH)/




jedi : $(PROGRAMS)

% : %.o
	$(CC) -o $@ $^

%.o : %.c
	$(CC) $(CFLAGS) -c $<
