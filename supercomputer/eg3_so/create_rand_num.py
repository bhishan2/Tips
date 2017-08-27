#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-14-2016 Fri
# Last update :
#
#
# Imports
import random,os

outdir = 'outputs'
if not os.path.exists(outdir):
    os.makedirs(outdir)

with open (outdir+'/temp.txt','w') as f :
    a = random.randint(0,9)
    f.write(str(a))

