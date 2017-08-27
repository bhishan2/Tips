#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Jul 24, 2017 Mon
# Last update : 
#
# Imports
import cson


def read_cson():
    with open('a.cson', 'rb') as fin:
        obj = cson.load(fin)
        print(obj)

if __name__ == '__main__':
    read_cson()
