#PBS -N sleepy 
#PBS -l walltime=00:05:30
#PBS -l nodes=1:ppn=1
#PBS -j oe

set echo on
cd $PBS_O_WORKDIR
date
pwd
hostname
qstat $PBS_JOBID -n
sleep 300 

date




