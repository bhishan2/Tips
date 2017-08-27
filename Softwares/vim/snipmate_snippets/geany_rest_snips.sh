# https://www.youtube.com/watch?v=L-fXOoxrt0M
hdr=.. contents:: Table of Contents\n   :depth: 3\n\n
contents=.. contents:: Table of Contents\n   :depth: 3\n\n
toc=.. toctree::\n   :maxdepth: 4\n\n   %cursor%
h=%cursor%\n################################################################################\n\n
h2=%cursor%\n********************************************************************************\n\n
h3=%cursor%\n================================================================================\n\n
h4=%cursor%\n--------------------------------------------------------------------------------\n\n
h5=%cursor%\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n
h6=%cursor%\n""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""\n\n
img=.. image:: ../images/%cursor%.png\n   :height: 100px\n   :width: 400 px\n   :align: center\n
fig=\n.. figure:: ../images/a.png\n    :width: 200px\n    :align: center\n    :height: 100px\n    :alt: alternate text\n    :figclass: align-center\n\n    This is caption.\n
footnote=[#f1]_  \n\n.. rubric:: Footnotes\n\n.. [#f1] Text of the first footnote.\n\n
cite=[book]_ \n\n.. [book] Name of book
link=`Link text <%cursor%>`_
link2=`a link`_.\n\n.. _a link: %cursor%\n\n
table=\n\n=====  =====  =======\nA      B      A and B\n=====  =====  =======\nF      F      F\nT      F      F\nF      T      F\nT      T      T\n=====  =====  =======\n\n
table2=\n\n+------------------------+------------+----------+----------+\n| Header1                | Header 2   | Header 3 | Header 4 |\n+========================+============+==========+==========+\n| ..                     | 12         |   13     | 14       |\n+------------------------+------------+----------+----------+\n| 21                     | 22         | 23       |       24 |\n+------------------------+------------+----------+----------+\n\n
ss=|H2O|\n\n.. |H2O| replace:: H\ :sub:`2`\ O\n
superscript=|H2O|\n\n.. |H2O| replace:: H\ :sub:`2`\ O\n
code=::\n\n    This is code.
i=\n    %cursor%
# new line
nl=\n| %cursor%\n| %cursor%
doctest=>>> print 'this is a Doctest block'\nthis is a Doctest block
hlist=.. hlist::\n   :columns: 3\n\n   * A list of\n   * short items\n   * that should be\n   * displayed\n   * horizontally\n\n

############# For Python and Rest both
note=.. note::\n\n   %cursor%.
seealso=.. seealso::\n\n   %cursor%.
seealso2=.. seealso::\n   Module :py:mod:`zipfile`\n      Documentation of the :py:mod:`zipfile` standard module.\n\n   `GNU tar manual, Basic Tar Format <http://link>`_\n      Documentation for tar archive files, including GNU tar extensions.\n
warning=.. warning::\n\n   Write complete sentence.
todo=.. admonition:: todo\n\n   %cursor%
info=.. admonition:: Info\n\n   %cursor%
info=.. admonition:: Readme\n\n   %cursor%
code=.. code-block:: c\n\n    printf("hi there");\n
math=.. :math:: %cursor%
mth=\n:math:`\alpha`
math2=.. math::\n\n    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k\n
topic=.. topic:: Topic\n\n    Indented text is the body.
sidebar=.. sidebar:: Sidebar\n\n   Body.
i=\n\n    %cursor%
test=.. testcode::\n\n    print("hi")\n\n.. testoutput::\n\n    hi\n
class=:class:`~fibonacci_doctest` 
meth=:meth:`~fibonacci_doctest.fib`
paired_index=..  index::\npair: poetry; bad # gives bad>poetry and poetry>bad.
single_index=..  index::\nsingle: Pythagoras # gives bad>poetry and poetry>bad.
frac=\frac{%cursor%}{%cursor%}
