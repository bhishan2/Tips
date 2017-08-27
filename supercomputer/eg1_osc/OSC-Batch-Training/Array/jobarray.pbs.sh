#PBS -N test-array
#PBS -l walltime=00:00:30
#PBS -l nodes=1:ppn=1
#PBS -t 1-3,10,20
#PBS -j oe 
#PBS -S /bin/bash

set -x

cd $PBS_O_WORKDIR

echo $PBS_ARRAYID
echo $PBS_JOBID

mkdir dir${PBS_ARRAYID}

qstat $PBS_JOBID -rn

