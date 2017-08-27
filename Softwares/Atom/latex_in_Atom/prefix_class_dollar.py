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
ofile = 'prefix_class_dollar.cson'
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

    def update_comment(self, prf,mod):
        print(comment.strip('\n'),file=open(ofile,'a'))
        print("  # {} Alpha {}".format(prf,mod).strip('\n'),file=open(ofile,'a'))

    def body(self,prop,x,y,mod):
        for i,a in enumerate(grk):
            hdr = "  '{} {} {}':\n".format(prop, a,mod)
            md, mdd = '', ''

            if not mod == '':
                md = mod[0].lower()
            else:
                md = ''
                
            if mod == 'Dollar':
                md, mdd = '', 'x'
            pre = "    'prefix': '{}{}{}y{}'\n".format(prop[0].lower(), alph[i],md,mdd)
            fmt = self.get_format(x,a,y)
            bdy = "    'body': '{}'\n".format(fmt)
            snip = hdr + pre + bdy
            print(snip,file=open(ofile,'a'))

def main():
    lst_pxaym = [['Angle', r'\\\\langle \\\\', 'alpha', r'\\\\rangle\ $0',''],
                ['Bold', r'\\\\boldsymbol{\\\\', 'alpha', r'}\ $0',''],
                ['Script', r'\\\\mathscr{\\\\', 'alpha',  r'\ $0',''],
                ['Partial', r'\\\\partial\\\\', 'alpha'  , r'\ $0',''],
                ['Angle', r'\\\\langle \\\\', 'alpha', r'\\\\rangle\ $0','Bold'],
                ['Partial', r'\\\\partial\\\\', 'alpha'  , r'\ $0','Bold'],
                ['Bold', r'\\\\partial\\\\', 'alpha'  , r'\ $0','Dollar']
               ]
    Prefix().empty()
    for pxaym in lst_pxaym:
        p,x,a,y,m = pxaym
        Prefix().update_comment(p,m)
        Prefix().body(p,x,y,m)

if __name__ == "__main__":
    main()
