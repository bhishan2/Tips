#!/bin/bash
#PBS -l walltime=10:00
#PBS -l nodes=1:ppn=16
# Append stderr to stdout
#PBS -j oe

# TEMP Workaround to fix problem on Ruby
if [[ $PBS_O_SERVER == *"ruby"* ]] ; then
    SAVE_PBS_JOBID=$PBS_JOBID
    export PBS_JOBID=${PBS_JOBID}.ruby-batch.ten.osc.edu

    module load python/2.7.latest

    # RESET variable to fix problem on Ruby
    export PBS_JOBID=$SAVE_PBS_JOBID
else
    module load python/2.7.latest
fi

cd $PBS_O_WORKDIR
#array=(1 3 4 50000)
array=($(seq 1000 1000 10000))

if [ -z ${PBS_ARRAYID+x} ] ; then # read http://stackoverflow.com/a/13864829/992834
    echo PBS_ARRAYID is not set
    echo submit this script using "qsub -t 1-10 $0"
else
    echo PBS_JOBID: $PBS_JOBID
    echo python example_lapack.py ${array[$PBS_ARRAYID]}
    python example_lapack.py ${array[$PBS_ARRAYID]}
fi
