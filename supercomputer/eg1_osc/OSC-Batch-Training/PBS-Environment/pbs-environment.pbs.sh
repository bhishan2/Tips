#PBS -l walltime=1:00
#PBS -N print-env-var
#PBS -j oe
#PBS -m bae
#PBS -S /bin/bash


set -x
cd $PBS_O_WORKDIR
qstat -u $USER -rn
echo $PBS_O_HOST
echo $PBS_O_QUEUE
echo $PBS_QUEUE
echo $PBS_JOBID
echo $PBS_JOBNAME
cat $PBS_NODEFILE

