#!/Users/poudel/anaconda/bin/python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 22, 2017 Tue
# Last update :
# Est time    :

# Imports
import string

# Global Variables
f_greek = 'greek.cson'
f_greek_astr = 'asterisk.cson'
f_greek_tilde = 'tilde.cson'
f_greek_bar = 'bar.cson'
f_greek_ang = 'ang.cson'
f_greek_astr_bold = 'asterisk_bold.cson'
f_greek_tilde_bold = 'tilde_bold.cson'
f_greek_bar_bold = 'bar_bold.cson'
f_greek_ang_bold = 'ang_bold.cson'

grk=['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa',
'lambda','mu','nu','xi','omicron','pi','rho','sigma','tau','upsilon','phi',
'chi','psi','omega','Gamma','Delta','Theta','Lambda','Xi','Pi','Sigma','Phi','Psi']

alph=list('abgdezhqiklmnxoprstufcywGDQLXPSFY')

comment=r"""
#-----------------------------------------------------------------------------
#
"""


def greek():
    print(comment.strip('\n'),file=open(f_greek,'w'))
    for i,a in enumerate(grk):
        hdr = "  '{}':\n".format(a)
        pre = "    'prefix': '{}'\n".format(alph[i])
        fmt = r'\\\\{}\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(f_greek,'a'))

def asterisk():
    print(comment.strip('\n'),file=open(f_greek_astr,'w'))
    for i,a in enumerate(grk):
        # print(i,alph[i],a)
        hdr = "  '{} asterisk':\n".format(a)
        pre = "    'prefix': '{}s'\n".format(alph[i])
        fmt = r'\\\\{}^*\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(f_greek_astr,'a'))

def tilde():
    print(comment.strip('\n'),file=open(f_greek_tilde,'w'))
    for i,a in enumerate(grk):
        # print(i,alph[i],a)
        hdr = "  '{} tilde':\n".format(a)
        pre = "    'prefix': '{}t'\n".format(alph[i])
        fmt = r'\\\\tilde{}\\\\{}{}\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(f_greek_tilde,'a'))

def bar():
    """Note: bb = mathbb{}   so bbar = beta bar."""
    print(comment.strip('\n'),file=open(f_greek_bar,'w'))
    for i,a in enumerate(grk):
        # print(i,alph[i],a)
        hdr = "  '{} bar':\n".format(a)
        pre = "    'prefix': '{}b'\n".format(alph[i])
        fmt = r'\\\\bar{}\\\\{}{}\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(f_greek_bar,'a'))

def ang():
    print(comment.strip('\n'),file=open(f_greek_ang,'w'))
    for i,a in enumerate(grk):
        # print(i,alph[i],a)
        hdr = "  'angle {}':\n".format(a)
        pre = "    'prefix': 'a{}'\n".format(alph[i])
        fmt = r'\\\\langle \\\\{} \\\\rangle\ $0'.format( a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(f_greek_ang,'a'))
# **************************** Bold ****************************************
def astrisk_bold():
    r"""
    Bold Alpha Star
    bas = \boldsymbol{\alpha}^*
    """
    print(comment.strip('\n'),file=open(f_greek_astr_bold,'w'))
    for i,a in enumerate(grk):
        # print(i,alph[i],a)
        hdr = "  'bold {} asterisk':\n".format(a)
        pre = "    'prefix': 'b{}s'\n".format(alph[i])
        # \boldsymbol{\alpha}^*
        fmt = r'\\\\boldsymbol{}\\\\{}{}^*\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(f_greek_astr_bold,'a'))

def tilde_bold():
    """
    Bold Alpha Tilde
    bas = \tilde{\boldsymbol{\alpha}}
    """
    print(comment.strip('\n'),file=open(f_greek_tilde_bold,'w'))
    for i,a in enumerate(grk):
        # print(i,alph[i],a)
        hdr = "  'bold {} tilde':\n".format(a)
        pre = "    'prefix': 'b{}t'\n".format(alph[i])
        fmt = r'\\\\tilde{}\\\\boldsymbol{}\\\\{}{}{}\ $0'.format("{","{", a,"}",'}')
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(f_greek_tilde_bold,'a'))

def bar_bold():
    """
    Bold Alpha Bar
    bab = \bar{\boldsymbol{\alpha}}

    """
    print(comment.strip('\n'),file=open(f_greek_bar_bold,'w'))
    for i,a in enumerate(grk):
        # print(i,alph[i],a)
        hdr = "  'bold {} bar':\n".format(a)
        pre = "    'prefix': 'b{}b'\n".format(alph[i])
        #         \bar{\boldsymbol{\alpha}}
        fmt = r'\\\\bar{}\\\\boldsymbol{}\\\\{}{}{}\ $0'.format("{","{", a,"}",'}')
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(f_greek_bar_bold,'a'))

def ang_bold():
    """
    Angle Bold Alpha
    aba = \langle\boldsymbol{\alpha}\rangle
    """
    print(comment.strip('\n'),file=open(f_greek_ang_bold,'w'))
    for i,a in enumerate(grk):
        # print(i,alph[i],a)
        hdr = "  'angle bold {}':\n".format(a)
        pre = "    'prefix': 'ab{}'\n".format(alph[i])
        fmt = r'\\\\langle\\\\boldsymbol{}\\\\{}{}\\\\rangle\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(f_greek_ang_bold,'a'))

def main():
    """Run main function."""
    astrisk_bold()
    tilde_bold()
    bar_bold()


if __name__ == "__main__":
    main()
