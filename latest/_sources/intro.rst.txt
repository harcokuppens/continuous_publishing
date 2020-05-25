

Introduction of Continuous Publishing (CP) documentation
========================================================


Continuous Publishing (CP) is in analogy to Continouos Integration(CI) and
Continouos Deployment(CD) a method to 

- to write documentation source  
- with supporting easy cooperation of documentation writers 
- using a version control system 
- where on pushing the documentation gets automatically build and published 

In this project we implemented this idea of Continuous Publishing using the
sphinx documentation generator tool in a github repository where we use a github action which on a git push automatically builds the documentation and publishes it online.


The documentation writer only needs to write the documentation source, and depending on the type of push an official 'stable' release or a temporary  'latest' version of the documentation is build and publish. In more detail: 

-  push of commits

   #. documentation gets automatically build
   #. build website uploaded to  latest/ subdir of  gh-pages branch
      which is automatically shown as website by github
   #. build pdf uploaded to a some temporary internet storage ( 1 week
      )  which gets linked from the website

-  push of tag   or  creation of github release online(for which
   automatically a tag gets pushed)

   #.  stable documentation gets automaticaly build
   #. build website uploaded to  stable/ subdir of  gh-pages branch
      which is automatically shown as website by github
   #. the build pdf is upload as release asset for that github release,
      this pdf url is linked from the website
   #. the build website is zipped and also archived as release asset for
      that github release

So the documentation write only needs to write documentation and push it to github. The documentation will automatically be build and published by a github actions workflow script.

For an official release you create a tag and push that
to github. You get automatically build documentation which is archived
in the repositories releases page. So you can always look back at older
documentation.

In this setup there is also added support of separate

-  tool version:  the version of the tool what the documentation
   describes. Because this changes from time to time we let you configure
   this in a separate TOOLVERSION.txt source file.
-  documentation version:  because the documentation is a repository it
   has its own version now. So for a specific tool version we 'can' have
   multiple documentation versions. The version can be:
    
   a tag version: 
     when building a tagged commit in git the
     documentation version is the tag label.
   a commit version: 
     when building a none tagged commit in git the
     documentation version is the short SHA-1 version of the commit. 
     When building locally and you have none-commited changes in your
     working folder then also a '+', called a dirty flag, is appended to the version. 


Why combination sphinx, github actions and github pages
-------------------------------------------------------

The usage of sphinx as documentation build system has the following advantages:

- it uses RestructuredText as source. The primary goal of reStructuredText is to define a markup 
  syntax that is readable and simple, yet powerful enough for non-trivial use. The intended purpose of the reStructuredText markup is twofold:

  - the establishment of a set of standard conventions allowing the expression of structure within plaintext, and
  - the conversion of such documents into useful structured data formats.

  Thus, a simple and readable documentation source with the expression strenght to build powerfull documentation.
  Powerfull in the meaning that it supports document structuring with parts/chapter/sections/sub..sections,  table of contents, index, glossary, figure environment, advanced cross referencing, math, etc...
  
  
-  sphinx is easy extensible with python extensions, so almost anything
   is possible:
     
     eg. graphviz dot source code supported in a block(directive) which
     allows you to make visually attractive graphs in your documentation

-  it has fancy html themes for nice web documentation 
-  it uses pdflatex to build  pdf, so you also get a nice pdf document 
-  it supports mathjax so you can use latex formula in your source

The combination of sphinx documentation builder and github actions allows us to automatically build the documentation on pushing to github. On problems with the restructuredText source the Sphinx build action within github actions shows in the online github editor annotations where the problems with the source are. This makes fixing problems with the source code easy. It also allows you to edit the source files online on the github website. After editing the online github editor lets you do a commit and push online. 

Using github pages we can publish the web documentation. Using the project's releases page we can publish stable pdf documents and a zip archives of the web documentation. The 'latest' build is also published on the website under latest/ subdirectory, and the latest pdf document is uploaded to bashupload.com where it stays available for a week. You have a week the time to evaluate the pdf build for you can decide is good enough to make it possible the stable release.