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
        fmt = r'\\\\{}\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def main():
    """Run main function."""
    greek()

if __name__ == "__main__":
    main()
