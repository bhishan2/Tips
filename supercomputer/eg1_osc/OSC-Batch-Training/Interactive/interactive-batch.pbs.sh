#PBS -l nodes=1:ppn=12:gpus=2:vis
#PBS -l walltime=00:45:00
#PBS -m bae
#PBS -N VNCjob
#PBS -j oe
#PBS -S /bin/bash

module load virtualgl
module load turbovnc

qstat -rn $PBS_JOBID
vncserver

sleep 100

vncpid=`pgrep -s 0 Xvnc`

while [ -e /proc/$vncpid ]; do sleep 0.1; done
