#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 19, 2017 Wed
# Last update :
#
# Imports
from __future__ import print_function
import numpy as np
import pandas as pd

def convert_geany_snippets_to_vim_snipmate_snippet(infile):
    """Convert snippets formats from geany to vim-snipmate."""
    fo = open(infile.replace('geany','vim_snipmate'),'w')
    data = open(infile,'r').readlines()
    for d in data:
        if not d.startswith('#') and len(d) !=1:
            parts = d.split('=')
            p1 = parts[1]
            p1 = p1.replace('%cursor%', '${1}')
            p1a = p1.split(r'\n')
            print('snippet {}'.format(parts[0]),file=fo)
            for p in p1a:
                print('\t' + p, file=fo)
            print("\n", file=fo)
    fo.close()

if __name__ == '__main__':
    infile = 'geany_rest_snips.sh'
    convert_geany_snippets_to_vim_snipmate_snippet(infile)
