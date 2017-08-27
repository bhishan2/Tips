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
ofile = 'prefix_absp.cson'

grk=['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa',
'lambda','mu','nu','xi','omicron','pi','rho','sigma','tau','upsilon','phi',
'chi','psi','omega','Gamma','Delta','Theta','Lambda','Xi','Pi','Sigma','Phi','Psi']

alph=list('abgdezhqiklmnxoprstufcywGDQLXPSFY')

comment=r"""
  #-----------------------------------------------------------------------------
"""
def greek():
    """
    Greek
    a = \alpha
    """
    print(comment.strip('\n'),file=open(ofile,'w'))
    print("  # Greek".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{}':\n".format(a)
        pre = "    'prefix': '{}'\n".format(alph[i])
        fmt = r'\\\\{}'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def angle():
    """
    Angle Alpha
    yaa = \langle\alpha\rangle
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Angle Alpha".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Angle {}':\n".format(a)
        pre = "    'prefix': 'a{}y'\n".format(alph[i])
        fmt = r'\\\\langle \\\\{} \\\\rangle\ $0'.format( a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def bold():
    """
    Bold Alpha
    yba = \boldsymbol{\alpha}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Bold Alpha".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Bold {}':\n".format(a)
        pre = "    'prefix': 'b{}y'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\{}{}\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def script():
    r"""
    Script Alpha
    ysa = \mathscr{\alpha}

    Note: \mathscr needs   \usepackage{mathrsfs}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Script Alpha".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Script {}':\n".format(a)
        pre = "    'prefix': 's{}y'\n".format(alph[i])
        fmt = r'\\\\mathscr{}\\\\{}{}\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def partial():
    r"""
    Partial Alpha
    ysa = \partial{\alpha}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Partial Alpha".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Partial {}':\n".format(a)
        pre = "    'prefix': 'p{}y'\n".format(alph[i])
        fmt = r'\\\\partial\\\\{}\ $0'.format( a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))



# **************************** Bold ****************************
def angle_bold():
    r"""
    Angle Alpha Bold
    yaab = \langle\boldsymbol{\alpha}\rangle
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Angle Alpha Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Angle {} Bold':\n".format(a)
        pre = "    'prefix': 'a{}by'\n".format(alph[i])
        fmt = r'\\\\langle\\\\boldsymbol{}\\\\{}{}\\\\rangle\ $0'.format( "{", a, "}" )
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def partial_bold():
    r"""
    Partial Alpha Bold
    ypab = \partial\boldsymbol{\alpha}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Partial Alpha Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Partial {} Bold':\n".format(a)
        pre = "    'prefix': 'p{}by'\n".format(alph[i])
        fmt = r'\\\\partial\\\\boldsymbol{}\\\\{}{}\ $0'.format( "{", a, "}" )
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

# **************************** Dollar ****************************
def dollar_greek():
    """
    Alpha Dollar
    xa = $\alpha$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} Dollar':\n".format(a)
        pre = "    'prefix': '{}x'\n".format(alph[i])
        fmt = r'\$\\\\{}\$\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def dollar_bold():
    """
    Bold Alpha Dollar
    xyba = $\boldsymbol{\alpha}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Bold Alpha Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Bold {} Dollar':\n".format(a)
        pre = "    'prefix': 'b{}yx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\{}{}\$\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def dollar_script():
    r"""
    Script Alpha Dollar
    ysa = $\mathscr{\alpha}$

    Note: \mathscr needs   \usepackage{mathrsfs}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Script Alpha Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Script {} Dollar':\n".format(a)
        pre = "    'prefix': 's{}yx'\n".format(alph[i])
        fmt = r'\$\\\\mathscr{}\\\\{}{}\$\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def main():
    """Run main function."""
    greek()
    angle()
    script()
    partial()

    # bold
    angle_bold()
    partial_bold()

    # Dollar
    dollar_greek()
    dollar_bold()
    dollar_script()


if __name__ == "__main__":
    main()
