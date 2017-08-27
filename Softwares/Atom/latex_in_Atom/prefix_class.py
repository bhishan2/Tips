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
ofile = 'prefix_class.cson'
grk=['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa',
'lambda','mu','nu','xi','omicron','pi','rho','sigma','tau','upsilon','phi',
'chi','psi','omega','Gamma','Delta','Theta','Lambda','Xi','Pi','Sigma','Phi','Psi']
alph=list('abgdezhqiklmnxoprstufcywGDQLXPSFY')
comment=r"  #-----------------------------------------------------------------------------"

class Prefix:
    def empty(self):
        with open(ofile,'w') as fo:
            pass

    def get_format(self, x, a, y):
        return x + str(a) +  y

    def update_comment(self, prf):
        """
        prf = 'Angle'
        """
        print(comment.strip('\n'),file=open(ofile,'a'))
        print("  # {} Alpha".format(prf).strip('\n'),file=open(ofile,'a'))

    def body(self,prop,x,y):
        for i,a in enumerate(grk):
            hdr = "  '{} {}':\n".format(prop, a)
            pre = "    'prefix': '{}{}y'\n".format(prop[0].lower(), alph[i])
            fmt = self.get_format(x,a,y)
            bdy = "    'body': '{}'\n".format(fmt)
            snip = hdr + pre + bdy
            print(snip,file=open(ofile,'a'))

def main():
    # List of property, first, middle, last
    # fmt = r'\\\\partial\\\\{}\ $0'.format( a)
    # 'Partial', r'\\\\partial\\\\', 'alpha'  , r'\ $0'
    lst_pxay = [['Angle', r'\\\\langle \\\\', 'alpha', r'\\\\rangle\ $0'],
                ['Bold', r'\\\\boldsymbol{\\\\', 'alpha', r'}\ $0'],
                ['Script', r'\\\\mathscr{\\\\', 'alpha',  r'\ $0'],
                ['Partial', r'\\\\partial\\\\', 'alpha'  , r'\ $0']
               ]
    Prefix().empty()
    for pxay in lst_pxay:
        p,x,a,y = pxay
        Prefix().update_comment(p)
        Prefix().body(p,x,y)

if __name__ == "__main__":
    main()
