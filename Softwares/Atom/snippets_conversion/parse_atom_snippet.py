#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Jul 24, 2017 Mon
# Last update : 
#
# Imports

# Lists
headers, prefixes, bodies = [], [], []

def parse_atom_snippets():
    
    with open('a.cson', 'r') as fin, open('tmp.txt', 'w') as fo:
        for line in fin:
            parts = line.split(':')
            if ':' in line and 'prefix' in line:
                h = parts[1].strip()
                h = h.replace("'", "")
                print(h)
                print('snippet ', h.strip(), file=fo)
            if ':' in line and 'body' in line:
                bodies.append(parts[1])
                body = parts[1]
                body = parts[1].split(r'\n')
                for b in body:
                    b = b.replace(r'$0', r"${0}")
                    b = b.replace(r'$1', r"${1}")
                    b = b.replace(r'$2', r"${2}")
                    b = b.replace(r'$3', r"${3}")
                    b = b.replace(r'\\', r"").strip()
                    print('\t' + b, file=fo)
                print("\n\n", file=fo)
    
if __name__ == '__main__':
    parse_atom_snippets()
