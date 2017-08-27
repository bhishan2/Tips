#!bash
# Author: Bhishan Poudel
# Date: Aug 16, 2017
#
# Usage: bash run_latex main.tex
# file=$1
file=glossaries_eg2.tex
base=${file%%.*}
ext=${file#*.}

# First clean
# Now delete build files
echo $base.aux
rm -f $base.aux $base.bbl $base.blg $base.dvi $base.fls $base.lof $base.log $base.lot $base.out $base.toc $base.fdb_latexmk *.alg *.glg *.glo *.gls *.ist *.acr *.acn *.glsdef

# If we have subsections in folder sections
rm -f sections/*.aux

# If we have additional style files,tex files etc on the folder pkg
cp pkg/*.sty .

# Run latex commands
pdflatex $base
bibtex $base
makeglossaries $base
pdflatex $base
pdflatex $base



# Delete build files
rm -f $base.aux $base.bbl $base.blg $base.dvi $base.fls $base.lof $base.log $base.lot $base.out $base.toc $base.fdb_latexmk *.alg *.glg *.glo *.gls *.ist *.acr *.acn *.glsdef

rm -f sections/*.aux

rm -f *.sty

# Open pdf
open $base.pdf
