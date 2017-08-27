#PBS -N mpi-hello-tmpdir
#PBS -l walltime=0:02:00
#PBS -l nodes=2:ppn=8
#PBS -j oe
#PBS -m bae
#PBS -S /bin/bash

set -x

cd $PBS_O_WORKDIR
pbsdcp mpi-hello.c $TMPDIR
mpicc -O2 mpi-hello.c -o mpi-hello
ls -l mpi-hello
mpiexec ./mpi-hello


