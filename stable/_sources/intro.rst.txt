

Introduction Continuous Publishing
==================================

Continuous Publishing(CP) is in analogy to Continouos Integration(CI) and
Continouos Deployment(CD) a method

- to write documentation source
- with supporting easy cooperation of documentation writers
- using a version control system
- where on pushing the documentation gets automatically build and published

We can say that Continuous Publishing (CP) makes writing documentation easy.

In this project we implemented this idea of Continuous Publishing using the
`Sphinx documentation generator tool <Sphinx_>`_ in a `GitHub`_ repository where we use  `GitHub Actions`_ which on a git push automatically builds the documentation and publishes it online in a `GitHub Pages`_ website. So documentation gets automatically build for each 'latest' version. However using git tags we can mark a specific version as a 'stable' release, for which automatically a release in the project's `GitHub Releases`_ page is created, and where the build PDF document and the zipped website are archived. Also the online website generated for the 'stable' release is put at a separate location then for the 'latest' documentation build, so that the 'stable' release can be used as official documention which only changes on each new release. The 'latest' release website location is overwritten on each commit.

The documentation writer only needs to write the documentation source, and depending on the type of push an official 'stable' release or a temporary  'latest' version of the documentation is build and published.

The automation is done by a by a `Github Actions`_ workflow script which  builds either the 'latest' or 'stable documentation depending on the type of its trigger event:

-  push of a set of commits

   #. build the documentation on that committed version. It builds documentation both as website and as a PDF document.
   #. upload the build website  to the latest/ subdir of the `gh-pages <https://help.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>`_
      branch which is automatically shown as website by github
   #. upload the build PDF to the temporary internet storage bashupload_, where the specific storage URL gets used to link the PDF document from the website.  The PDF is automatically deleted from the online storage after 1 week. This allows documentation writers to inspect the build PDF for 1 week. Only for stable releases we archive the PDF permanent online.

-  push of a tag


   #. build the documentation on that tagged version. It builds documentation both as website and as a PDF document.
   #. upload the build website  to the stable/ subdir of the gh-pages
      branch which is automatically shown as website by github
   #. the build PDF is upload as release asset for that github release,
      this PDF url is linked from the website
   #. the build website is zipped and also archived as release asset for
      that github release

   note: when creating a github release online then indirectly a tag gets
   created and pushed

The 'stable' documentation gets linked to from your tool's website as the official documentation. The 'stable' documentation gets tagged by official versions which are represented by releases on GitHub_. The build documentation per release gets archived on the github's documention project releases webpage. So you can always look back at older officially released documentation versions.

The 'latest' documentation is seen as the latest documentation under construction. It is the latest version where the documentation writers are working on. Users of the tool should not use this as documentation, but instead read the 'stable' documentation. Only when the 'latest' documentation is found ready, then a new 'stable' release will be made by the documentation writers.  Only documentation writers use this 'latest' build of the documentation to quickly review the documentation without needing to build it themselves locally. They even can write documentation online in the github repository's editor. On every save in the online editor a new commit is pushed to the repository and new 'latest' documentation gets automatically build and published. When looking at a webpage in the 'latest' documentation website there is a 'Edit on Github' button which takes you directly the page's source in the github project to allows you to quickly edit it. So for example if you see small typo you can immediately fix it online. On the 'stable' documentation website this button is not present, because it is a fixed release.

We can conclude that writing documentation has become easy, because the documentation writer only needs to write the documentation source and push it online to github, and then the documentation gets automatically build and he only has to review the build version online. If then finally the new documentation is ready for release he can either just create a new git tag locally and push it to github or just create a new tagged release on the github project's website. Then the documentation will be automatically build and officially released as the new stable version of the documentation which is linked by the tool's website.


Combined version of tool and documentation version
--------------------------------------------------

Often documentation is written for some tool. In that case we will
have two different versions which we combine:

tool version:
   the version of the tool what the documentation
   describes. Because this changes from time to time we let you configure
   this in a separate TOOLVERSION.txt source file.
documentation version:
   because the documentation is a repository it
   has its own version now. For a specific tool version we 'can' have
   multiple documentation versions. The version can be a:

   tag version:
     when building a tagged commit in git the
     documentation version is the tag label.
   commit version:
     when building a none tagged commit in git the
     documentation version is the short SHA-1 version of the commit.
     When building locally and you have none-commited changes in your
     working folder then also a '+', called a dirty flag, is appended to the version.

We then combine these versions in the name of the PDF document. For example::

  TorXakis-v4.3.14_Userguide-0a69d7c.pdf


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


Setup a new documentation repository
====================================

initial setup
-------------

configuration
-------------

TODO:
 * index.html with link to releases website
 * make build faster by upload to bashupload in sphinx's make file!
 * configuration at one place,  DOCUMENT_NAME
 * document as example and as easy reference we added rest doc from sphinx website
 * document: gh-pages url's
 * document: setup doc repo, how to set orphan gh-pages branch
   => make it easy => download start files
 * document: rest docs overview
