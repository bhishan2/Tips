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
# astrisk bar prime hat tilde
ofile = 'suffix_abdphtm0123.cson'

grk=['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa',
'lambda','mu','nu','xi','omicron','pi','rho','sigma','tau','upsilon','phi',
'chi','psi','omega','Gamma','Delta','Theta','Lambda','Xi','Pi','Sigma','Phi','Psi']

alph=list('abgdezhqiklmnxoprstufcywGDQLXPSFY')

comment=r"""
  #-----------------------------------------------------------------------------
"""
def asterisk():
    """
    Alpha Astrisk
    aa = \alpha^*
    """
    print(comment.strip('\n'),file=open(ofile,'w'))
    print("  # Alpha Astrisk".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} asterisk':\n".format(a)
        pre = "    'prefix': '{}a'\n".format(alph[i])
        fmt = r'\\\\{}^*\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def bar():
    """
    Alpha Bar
    ab = \bar\alpha
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Bar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} bar':\n".format(a)
        pre = "    'prefix': '{}b'\n".format(alph[i])
        fmt = r'\\\\bar{}\\\\{}{}\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def dot():
    """
    Alpha Dot
    ad = \dot{\alpha}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Dot".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} dot':\n".format(a)
        pre = "    'prefix': '{}d'\n".format(alph[i])
        fmt = r'\\\\dot{}\\\\{}{}\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def prime():
    """
    Alpha Prime
    ap = \alpha\prime
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Prime".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} prime':\n".format(a)
        pre = "    'prefix': '{}p'\n".format(alph[i])
        fmt = r'\\\\{}\\\\prime\ $0'.format( a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def hat():
    """
    Alpha Hat
    ah = \hat{\alpha}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Hat".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} hat':\n".format(a)
        pre = "    'prefix': '{}h'\n".format(alph[i])
        fmt = r'\\\\hat{}\\\\{}{}\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def tilde():
    """
    Alpha Tilde
    at = \tilde{\alpha}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Tilde".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} tilde':\n".format(a)
        pre = "    'prefix': '{}t'\n".format(alph[i])
        fmt = r'\\\\tilde{}\\\\{}{}\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def modulus():
    """
    Alpha Modulus
    am = \lvert\alpha\rvert
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Modulus".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} modulus':\n".format(a)
        pre = "    'prefix': '{}m'\n".format(alph[i])
        fmt = r'\\\\lvert\\\\{}\\\\rvert\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def zero():
    """
    Alpha Zero
    a0 = \alpha_0
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Zero".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} zero':\n".format(a)
        pre = "    'prefix': '{}0'\n".format(alph[i])
        fmt = r'\\\\{}_0\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def one():
    """
    Alpha One
    a1 = \alpha_1
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha One".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} one':\n".format(a)
        pre = "    'prefix': '{}1'\n".format(alph[i])
        fmt = r'\\\\{}_1\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def two():
    """
    Alpha Two
    a2 = \alpha_2
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Two".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} two':\n".format(a)
        pre = "    'prefix': '{}2'\n".format(alph[i])
        fmt = r'\\\\{}_2\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def three():
    """
    Alpha Three
    a3 = \alpha_3
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Three".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} three':\n".format(a)
        pre = "    'prefix': '{}3'\n".format(alph[i])
        fmt = r'\\\\{}_3\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

# **************************** Bold ***************************
def asterisk_bold():
    """
    Alpha Asterisk Bold
    aab = \boldsymbol{\alpha}^*
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Astrisk Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} asterisk bold':\n".format(a)
        pre = "    'prefix': '{}ab'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\{}{}^*\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def bar_bold():
    """
    Alpha Bar Bold
    abb = \boldsymbol{\bar{\alpha}}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("# Alpha Bar Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} bar bold':\n".format(a)
        pre = "    'prefix': '{}bb'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\bar{}\\\\{}{}{}\ $0'.format("{", "{", a,"}","}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def dot_bold():
    """
    Alpha Dot Bold
    adb = \boldsymbol{\dot{\alpha}}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("# Alpha Dot Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} dot bold':\n".format(a)
        pre = "    'prefix': '{}db'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\dot{}\\\\{}{}{}\ $0'.format("{", "{", a,"}","}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def prime_bold():
    """
    Alpha Prime Bold
    apb = \boldsymbol{\alpha}\prime
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("# Alpha Prime Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} prime bold':\n".format(a)
        pre = "    'prefix': '{}pb'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\{}{}\\\\prime\ $0'.format("{", a, "}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def hat_bold():
    """
    Alpha Hat Bold
    ahb = \boldsymbol{\hat{\alpha}}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("# Alpha Hat Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} hat bold':\n".format(a)
        pre = "    'prefix': '{}hb'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\hat{}\\\\{}{}{}\ $0'.format("{", "{", a,"}","}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def tilde_bold():
    """
    Alpha Tilde Bold
    atb = \boldsymbol{\tilde{\alpha}}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Tilde Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} tilde bold':\n".format(a)
        pre = "    'prefix': '{}tb'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\tilde{}\\\\{}{}{}\ $0'.format("{", "{", a,"}","}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def modulus_bold():
    """
    Alpha Modulus Bold
    amb = \lvert\boldsymbol{\alpha}\rvert
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Modulus Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} modulus bold':\n".format(a)
        pre = "    'prefix': '{}mb'\n".format(alph[i])
        fmt = r'\\\\lvert\\\\boldsymbol{}\\\\{}{}\\\\rvert\ $0'.format("{", a, '}')
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def zero_bold():
    """
    Alpha Zero Bold
    a0b = \boldsymbol{\alpha_0}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Zero Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} zero bold':\n".format(a)
        pre = "    'prefix': '{}0b'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\{}_0{}\ $0'.format("{", a, "}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def one_bold():
    """
    Alpha One Bold
    a1b = \boldsymbol{\alpha_1}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha One Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} one bold':\n".format(a)
        pre = "    'prefix': '{}1b'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\{}_1{}\ $0'.format("{", a, "}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def two_bold():
    """
    Alpha Two Bold
    a2b = \boldsymbol{\alpha_2}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Two Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} two bold':\n".format(a)
        pre = "    'prefix': '{}2b'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\{}_2{}\ $0'.format("{", a, "}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def three_bold():
    """
    Alpha Three Bold
    a3b = \boldsymbol{\alpha_3}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Three Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} three bold':\n".format(a)
        pre = "    'prefix': '{}3b'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\{}_3{}\ $0'.format("{", a, "}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

# **************************** Suffix Dollar ***************************
def asterisk_dollar():
    """
    Alpha Astrisk Dollar
    aax = $\alpha^*$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Astrisk Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} asterisk dollar':\n".format(a)
        pre = "    'prefix': '{}ax'\n".format(alph[i])
        fmt = r'\$\\\\{}^*\$\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def bar_dollar():
    """
    Alpha Bar Dollar
    abx = $\bar\alpha$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Bar Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} bar dollar':\n".format(a)
        pre = "    'prefix': '{}bx'\n".format(alph[i])
        fmt = r'\$\\\\bar{}\\\\{}{}\$\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def dot_dollar():
    """
    Alpha Dot Dollar
    adx = $\dot{\alpha}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Dot Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} dot dollar':\n".format(a)
        pre = "    'prefix': '{}dx'\n".format(alph[i])
        fmt = r'\$\\\\dot{}\\\\{}{}\$\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def prime_dollar():
    """
    Alpha Prime Dollar
    apx = $\alpha\prime$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Prime Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} prime dollar':\n".format(a)
        pre = "    'prefix': '{}px'\n".format(alph[i])
        fmt = r'\$\\\\{}\\\\prime\$\ $0'.format( a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def hat_dollar():
    """
    Alpha Hat Dollar
    ahx = $\hat{\alpha}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Hat Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} hat dollar':\n".format(a)
        pre = "    'prefix': '{}hx'\n".format(alph[i])
        fmt = r'\$\\\\hat{}\\\\{}{}\$\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def tilde_dollar():
    """
    Alpha Tilde Dollar
    atx = $\tilde{\alpha}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Tilde Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} tilde dollar':\n".format(a)
        pre = "    'prefix': '{}tx'\n".format(alph[i])
        fmt = r'\$\\\\tilde{}\\\\{}{}\$\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def modulus_dollar():
    """
    Alpha Modulus Dollar
    amx = $\lvert\alpha\rvert$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Modulus Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} modulus dollar':\n".format(a)
        pre = "    'prefix': '{}mx'\n".format(alph[i])
        fmt = r'\$\\\\lvert\\\\{}\\\\rvert\$\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def zero_dollar():
    """
    Alpha Zero Dollar
    a0 = $\alpha_0$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Zero Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} zero dollar':\n".format(a)
        pre = "    'prefix': '{}0x'\n".format(alph[i])
        fmt = r'\$\\\\{}_0\$\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def one_dollar():
    """
    Alpha One Dollar
    a1 = $\alpha_1$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha One Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} one dollar':\n".format(a)
        pre = "    'prefix': '{}1x'\n".format(alph[i])
        fmt = r'\$\\\\{}_1\$\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def two_dollar():
    """
    Alpha Two Dollar
    a2x = $\alpha_2$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Two Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} two dollar':\n".format(a)
        pre = "    'prefix': '{}2x'\n".format(alph[i])
        fmt = r'\$\\\\{}_2\$\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def three_dollar():
    """
    Alpha Three Dollar
    a3x = $\alpha_3$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Three Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} three dollar':\n".format(a)
        pre = "    'prefix': '{}3x'\n".format(alph[i])
        fmt = r'\$\\\\{}_3\$\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


# **************************** Bold Dollar ***************************
def asterisk_bold_dollar():
    """
    Alpha Asterisk Bold Dollar
    aabx = $\boldsymbol{\alpha}^*$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Astrisk Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} asterisk bold dollar':\n".format(a)
        pre = "    'prefix': '{}abx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\{}{}^*\$\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def bar_bold_dollar():
    """
    Alpha Bar Bold Dollar
    abbx = $\boldsymbol{\bar{\alpha}}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Bar Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} bar bold dollar':\n".format(a)
        pre = "    'prefix': '{}bbx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\bar{}\\\\{}{}{}\$\ $0'.format("{", "{", a,"}","}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def dot_bold_dollar():
    """
    Alpha Dot Bold Dollar
    adbx = $\boldsymbol{\dot{\alpha}}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Dot Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} dot bold dollar':\n".format(a)
        pre = "    'prefix': '{}dbx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\dot{}\\\\{}{}{}\$\ $0'.format("{", "{", a,"}","}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def prime_bold_dollar():
    """
    Alpha Prime Bold Dollar
    apbx = $\boldsymbol{\alpha}\prime$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Prime Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} prime bold dollar':\n".format(a)
        pre = "    'prefix': '{}pbx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\{}{}\\\\prime\$\ $0'.format("{", a, "}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def hat_bold_dollar():
    """
    Alpha Hat Bold Dollar
    ahbx = $\boldsymbol{\hat{\alpha}}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Hat Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} hat bold dollar':\n".format(a)
        pre = "    'prefix': '{}hbx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\hat{}\\\\{}{}{}\$\ $0'.format("{", "{", a,"}","}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def tilde_bold_dollar():
    """
    Alpha Tilde Bold Dollar
    atbx = \boldsymbol{\tilde{\alpha}}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Tilde Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} tilde bold dollar':\n".format(a)
        pre = "    'prefix': '{}tbx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\tilde{}\\\\{}{}{}\$\ $0'.format("{", "{", a,"}","}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def modulus_bold_dollar():
    """
    Alpha Modulus Bold Dollar
    amb = $\lvert\boldsymbol{\alpha}\rvert$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Modulus Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} modulus bold dollar':\n".format(a)
        pre = "    'prefix': '{}mbx'\n".format(alph[i])
        fmt = r'\$\\\\lvert\\\\boldsymbol{}\\\\{}{}\\\\rvert\$\ $0'.format("{", a, '}')
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def zero_bold_dollar():
    """
    Alpha Zero Bold Dollar
    a0bx = $\boldsymbol{\alpha_0}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Zero Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} zero bold dollar':\n".format(a)
        pre = "    'prefix': '{}0bx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\{}_0{}\$\ $0'.format("{", a, "}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def one_bold_dollar():
    """
    Alpha One Bold Dollar
    a1bx = $\boldsymbol{\alpha_1}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha One Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} one bold dollar':\n".format(a)
        pre = "    'prefix': '{}1bx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\{}_1{}\$\ $0'.format("{", a, "}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def two_bold_dollar():
    """
    Alpha Two Bold Dollar
    a2bx = $\boldsymbol{\alpha_2}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Two Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} two bold dollar':\n".format(a)
        pre = "    'prefix': '{}2bx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\{}_2{}\$\ $0'.format("{", a, "}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def three_bold_dollar():
    """
    Alpha Three Bold Dollar
    a3bx = $\boldsymbol{\alpha_3}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Three Bold Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} three bold dollar':\n".format(a)
        pre = "    'prefix': '{}3bx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\{}_3{}\$\ $0'.format("{", a, "}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def main():
    """Run main function."""
    # Suffix
    asterisk()
    bar()
    dot()
    prime()
    hat()
    tilde()
    modulus()
    zero()
    one()
    two()
    three()

    # Bold
    asterisk_bold()
    bar_bold()
    dot_bold()
    prime_bold()
    hat_bold()
    tilde_bold()
    modulus_bold()
    zero_bold()
    one_bold()
    two_bold()
    three_bold()

    # Suffix Dollar
    asterisk_dollar()
    bar_dollar()
    dot_dollar()
    prime_dollar()
    hat_dollar()
    tilde_dollar()
    modulus_dollar()
    zero_dollar()
    one_dollar()
    two_dollar()
    three_dollar()

    # Bold Dollar
    asterisk_bold_dollar()
    bar_bold_dollar()
    dot_bold_dollar()
    prime_bold_dollar()
    hat_bold_dollar()
    tilde_bold_dollar()
    modulus_bold_dollar()
    zero_bold_dollar()
    one_bold_dollar()
    two_bold_dollar()
    three_bold_dollar()


if __name__ == "__main__":
    main()
