#!/bin/bash
#PBS -l walltime=10:00
#PBS -l nodes=2:ppn=16
#PBS -q debug
# Append stderr to stdout
#PBS -j oe

cd $PBS_O_WORKDIR
source /usr/local/lmod/lmod/init/sh
module load python/2.7.latest

procs=32
ppn=16
max_nodes=$((procs/ppn))
count=0
base=0
array=($(seq 1000 1000 10000))
while [ $base -lt ${#array[@]} ]; do
    for task in $(seq 1 $procs); do
        case=${array[$((task / ppn + base))]}
        command="python example_lapack.py $case"
        echo "if [ $((task%$ppn)) -eq 1 ] ; then $command; fi"
    done | mpiexec parallel-command-processor
    base=$((base+max_nodes))
done
