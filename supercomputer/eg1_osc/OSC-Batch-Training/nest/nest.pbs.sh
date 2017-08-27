#PBS -N nest
#PBS -l walltime=00:05:00
#PBS -l nodes=1:ppn=1
#PBS -j oe
#PBS -S /bin/bash
#PBS -m bae

set -x

cd $PBS_O_WORKDIR

gcc nest.c -lm 
./a.out 459 121

rm -f a.out
