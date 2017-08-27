snippet hdr
	.. contents:: Table of Contents
	   :depth: 3
	
	



snippet contents
	.. contents:: Table of Contents
	   :depth: 3
	
	



snippet toc
	.. toctree::
	   :maxdepth: 4
	
	   ${1}



snippet h
	${1}
	################################################################################
	
	



snippet h2
	${1}
	********************************************************************************
	
	



snippet h3
	${1}
	


snippet h4
	${1}
	--------------------------------------------------------------------------------
	
	



snippet h5
	${1}
	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	
	



snippet h6
	${1}
	""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	
	



snippet img
	.. image:: ../images/${1}.png
	   :height: 100px
	   :width: 400 px
	   :align: center
	



snippet fig
	
	.. figure:: ../images/a.png
	    :width: 200px
	    :align: center
	    :height: 100px
	    :alt: alternate text
	    :figclass: align-center
	
	    This is caption.
	



snippet footnote
	[#f1]_  
	
	.. rubric:: Footnotes
	
	.. [#f1] Text of the first footnote.
	
	



snippet cite
	[book]_ 
	
	.. [book] Name of book



snippet link
	`Link text <${1}>`_



snippet link2
	`a link`_.
	
	.. _a link: ${1}
	
	



snippet table
	
	
	


snippet table2
	
	
	+------------------------+------------+----------+----------+
	| Header1                | Header 2   | Header 3 | Header 4 |
	+


snippet ss
	|H2O|
	
	.. |H2O| replace:: H\ :sub:`2`\ O
	



snippet superscript
	|H2O|
	
	.. |H2O| replace:: H\ :sub:`2`\ O
	



snippet code
	::
	
	    This is code.



snippet i
	
	    ${1}



snippet nl
	
	| ${1}
	| ${1}



snippet doctest
	>>> print 'this is a Doctest block'
	this is a Doctest block



snippet hlist
	.. hlist::
	   :columns: 3
	
	   * A list of
	   * short items
	   * that should be
	   * displayed
	   * horizontally
	
	



snippet note
	.. note::
	
	   ${1}.



snippet seealso
	.. seealso::
	
	   ${1}.



snippet seealso2
	.. seealso::
	   Module :py:mod:`zipfile`
	      Documentation of the :py:mod:`zipfile` standard module.
	
	   `GNU tar manual, Basic Tar Format <http://link>`_
	      Documentation for tar archive files, including GNU tar extensions.
	



snippet warning
	.. warning::
	
	   Write complete sentence.



snippet todo
	.. admonition:: todo
	
	   ${1}



snippet info
	.. admonition:: Info
	
	   ${1}



snippet info
	.. admonition:: Readme
	
	   ${1}



snippet code
	.. code-block:: c
	
	    printf("hi there");
	



snippet math
	.. :math:: ${1}



snippet mth
	
	:math:`\alpha`



snippet math2
	.. math::
	
	    n_{\mathrm{offset}} 


snippet topic
	.. topic:: Topic
	
	    Indented text is the body.



snippet sidebar
	.. sidebar:: Sidebar
	
	   Body.



snippet i
	
	
	    ${1}



snippet test
	.. testcode::
	
	    print("hi")
	
	.. testoutput::
	
	    hi
	



snippet class
	:class:`~fibonacci_doctest` 



snippet meth
	:meth:`~fibonacci_doctest.fib`



snippet paired_index
	..  index::
	pair: poetry; bad # gives bad>poetry and poetry>bad.



snippet single_index
	..  index::
	single: Pythagoras # gives bad>poetry and poetry>bad.



snippet frac
	\frac{${1}}{${1}}



