#!/bin/bash
################################################################################
#PBS -N myfile.py
#PBS -l nodes=7:ppn=4
#PBS -l walltime=00:00:00:50
#PBS -m bea
##PBS -M mail@mail.mail
###############################################################################

cores=$(awk 'END {print NR}' $PBS_NODEFILE)
mpirun -np $cores python myfile.py