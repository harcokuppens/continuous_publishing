Why combination sphinx, github actions and github pages
-------------------------------------------------------

Sphinx
^^^^^^

The usage of `Sphinx`_ as documentation build system has the following advantages:

- `Sphinx`_ uses RestructuredText as source which is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax.

  The primary goal of reStructuredText is to define a markup
  syntax that is readable and simple, yet powerful enough for non-trivial use. The intended purpose of the reStructuredText markup is twofold:

  - the establishment of a set of standard conventions allowing the expression of structure within plaintext, and
  - the conversion of such documents into useful structured data formats.

- `Sphinx`_ enhances RestructuredText to allow you to write documentation  in a more structured  way in many source files with cross referencing between these source files. It extends RestructuredText with many convenient roles and directives to make documentation writing easier and better.


-  `Sphinx`_ is easy extensible with python extensions, so almost anything
   is possible:

     eg. graphviz dot source code supported in a block(directive) which
     allows you to make visually attractive graphs in your documentation

-  `Sphinx`_ has fancy html themes for nice web documentation
-  `Sphinx`_ uses pdflatex to build  PDF, so you also get a nice PDF document
-  `Sphinx`_ supports mathjax so you can use latex formula in your source
-  `Sphinx`_ uses `Pygments <https://pygments.org/>`_ as a generic syntax highlighter with which you can `Sphinx`_ any source code. It is also easy to extend.

- Thus with sphinx we get a simple and readable documentation source with the expression strenght to build powerfull documentation.
  Powerfull in the meaning that it supports document structuring with parts/chapter/sections/sub..sections,  table of contents, index, glossary, figure environment, advanced cross referencing, math, etc...

GitHub Actions
^^^^^^^^^^^^^^

The combination of `Sphinx`_ documentation builder and `GitHub Actions`_ allows us to automatically build the documentation on pushing to github. On problems with the restructuredText source the Sphinx build action within github actions shows in the online github editor annotations where the problems with the source are. This makes fixing problems with the source code easy. It also allows you to edit the source files online on the github website, where on every save in the online editor a new commit is pushed to the repository.

GitHub Pages
^^^^^^^^^^^^^^

Using `GitHub Pages`_ we can publish the web documentation online. Using the project's `GitHub Releases`_ page we can publish the PDF documents and zip archives of the web documentation for all 'stable' releases online. The 'latest' build is also published on the website under latest/ subdirectory, and the latest PDF document is uploaded to bashupload_ where it stays available for a week. You have a week the time to evaluate the PDF build for the latest commit.

.. _Sphinx: https://www.sphinx-doc.org/
.. _GitHub: https://github.com/
.. _GitHub Actions: https://github.com/features/actions
.. _GitHub Pages: https://pages.github.com/
.. _bashupload:  https://bashupload.com/
.. _GitHub Releases: https://help.github.com/en/github/administering-a-repository/releasing-projects-on-github


