#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-14-2016 Fri
# Last update :
#
#
# Imports
import os,shutil,random,time,subprocess


for i in list(range(5)):
    cmd = 'python create_rand_num.py'
    subprocess.call(cmd,shell=1)

    outfolder = 'outputs'
    outfile = outfolder + '/' + \
              str(random.randint(0,10000)) + time.strftime('_%b_%d_%H_%M')


    subprocess.call('cp temp.txt ' + outfile, shell=1)
    os.remove('temp.txt')
