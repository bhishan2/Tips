#!bash
# Author: Bhishan Poudel
# Date: Aug 16, 2017
#
# Usage: bash run_latex main.tex
# file=$1
file=hello.tex
base=${file%%.*}
ext=${file#*.}

# First clean
# Now delete build files
echo $base.aux
rm -f $base.aux $base.bbl,$base.blg,$base.dvi $base.fls $base.lof $base.log $base.lot $base.out $base.toc $base.fdb_latexmk

rm -f sections/*.aux

# Run latex commands
pdflatex $base
bibtex $base
pdflatex $base
pdflatex $base



# Delete build files
rm -f $base.aux $base.bbl $base.blg $base.dvi $base.fls $base.lof $base.log $base.lot $base.out $base.toc $base.fdb_latexmk

rm -f sections/*.aux

# Open pdf
open $base.pdf
