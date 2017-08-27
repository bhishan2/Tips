#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 19, 2017 Wed
# Last update :
#
# Imports
from __future__ import print_function

template=r"""
    'MacOS Desktop Nofitication':
        'prefix': 'xnotify'
        'body': '''
"""

def convert_txt_to_atom_snippet(infile='original.txt'):
    """Convert snippets formats from txt to atom snippets."""
    fo = open('output.txt','w')
    lines = open(infile,'r').readlines()

    # First line framework.
    print(template.strip(), file=fo)
    for i, l in enumerate(lines):
        print(l.strip('\n'))

        # First  line of function def
        if i < 1:
            l = '        ' + l.strip('\n')
            print(l,file=fo)

        # Body of function
        else:
            # Keep empty lines empty.
            if l.isspace():
                print(l.strip('\n'),file=fo)

            else:
                l = l.replace("\\","\\\\\\\\")
                l = r'        \ \ \ \ ' + l.lstrip().strip('\n')
                l = l.replace(r"'",r"\'")
                print(l,file=fo)

    # end part
    print(r"        $0",file=fo)
    print(r"        '''",file=fo)
    print("\npaste select all and indent twice",file=fo)
    fo.close()

if __name__ == '__main__':
    infile = 'original.txt'
    convert_txt_to_atom_snippet()
