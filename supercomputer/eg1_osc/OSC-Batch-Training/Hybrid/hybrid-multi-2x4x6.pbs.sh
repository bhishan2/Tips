#PBS -N hybrid-mpi-omp-2x4d2
#PBS -l walltime=00:01:00
#PBS -l nodes=2:ppn=12
#PBS -j oe
#PBS -m bae
#PBS -S /bin/bash

module swap intel gnu

set -x

export OMP_NUM_THREADS=6
export MV2_ENABLE_AFFINITY=0
cd $PBS_O_WORKDIR
pwd

# Compile in $PBS_O_WORKDIR, printed above.
mpicc -O2 -fopenmp hello-hybrid.c -o hello-hybrid

# Copy executable to all nodes
pbsdcp $PBS_O_WORKDIR/hello-hybrid $TMPDIR
mpiexec -npernode 2 $TMPDIR/hello-hybrid

qstat $PBS_JOBID -ln
ja

