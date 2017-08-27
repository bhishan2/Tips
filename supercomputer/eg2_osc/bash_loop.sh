#!/bin/bash
#PBS -l walltime=10:00
#PBS -l nodes=1:ppn=16
# Append stderr to stdout
#PBS -j oe
#PBS -q debug

cd $PBS_O_WORKDIR
module load python/2.7.latest

array=$(seq 1000 1000 10000)
for case in $array; do
    echo
    echo python example1.py $case
    python example1.py $case
done
