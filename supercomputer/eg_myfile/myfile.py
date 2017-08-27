#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-15-2016 Sat
# Last update :
#
#
# Imports
from mpi4py import MPI
import random,os

outdir = 'outputs'
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

with open (outdir+'/temp%s.txt' % rank,'w') as f :
    a = random.randint(0,9)
    f.write(str(a))
