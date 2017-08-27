#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-14-2016 Fri
# Last update :
#
#
# Imports
from mpi4py import MPI
import random,os

outdir = 'outputs'
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if not os.path.exists(outdir):
    os.makedirs(outdir)

with open (outdir+'/temp%s.txt' % rank,'w') as f :
    a = random.randint(0,9)
    f.write(str(a))
