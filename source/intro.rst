
=============================================
Introduction of Continuous Documentation (CD)
=============================================

Welcome to this example project showing how to use sphinx documentation.


The idea is 'continuous documentation'  so that on :

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

So you only have to write documentation and push to github. The
documentation will automatically build by a github actions workflow
script.

If you want to make an official release you create a tag and push that
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
    
     # a tag version: when building a tagged commit in git the
       documentation version is the tag label.
     # a commit version: when building a none tagged commit in git the
        documentation version is the short SHA-1 version of the commit. 
        When building locally and you have none-commited changes in your
        working folder then also a '+', called a dirty flag, is appended to the version. 

The usage off sphinx has the following advantages:

-  it uses latexpdf to build  pdf, so you get nice
-  it support mathjax so you can use latex formula in your source
-  sphinx is easy extensible with python extensions, so almost anything
   is possible.
   eg. graphviz dot source code supported in a block(directive) which
   allows you to make visually attractive graphs in your documentation

