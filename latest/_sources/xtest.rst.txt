
======
Xtest 
======


If [#note]_ is the first footnote reference, it will show up as
"[1]".  


We can refer to it again as [#note]_ and again see
"[1]". 


We can also refer to it as note_ (an ordinary internal
hyperlink reference).

.. include:: inclusion.txt


| Line blocks are useful for addresses,
|     verse, and adornment-free lists.
|    
|     Each new line begins with a
|     vertical bar ("|").
|         Line breaks and initial indents
|         are preserved.
|     Continuation lines are wrapped
      portions of long lines; they begin
      with spaces in place of vertical bars.
|     New 
|     agian new

.. graphviz::

   digraph foo {
      "bar" -> "baz";
   }


.. role:: latex(code)
   :language: latex

This is some latex code :latex:`\TeX{} users`.

H\ :sub:`2`\ O
E = mc\ :sup:`2`

Math using latex style math using mathjax: :math:`x = {-b \pm \sqrt{b^2-4ac} \over 2a}`.


Lorem ipsum [Xef]_ dolor sit amet.


.. [#note] This is the footnote labeled "note".


