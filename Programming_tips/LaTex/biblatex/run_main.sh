#!bash
# Commands to compile latex with biblatex
# Needs etools.sty, xtring.sty and xstring.tex files
pdflatex main
bibtex main    # biber main   # if backend is biber
pdflatex main
pdflatex main
