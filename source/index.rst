.. Example sphinx doc repo documentation master file, created by
   sphinx-quickstart on Wed Apr 22 16:00:35 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==========================================================================
Continuous Publishing (CP) with Sphinx, GitHub Actions and GitHub Pages
==========================================================================

.. BUG: above heading MUST be included otherwise the first section will be ommited from the PDF.
        For html output everything works as normal, and above header is made and below content is shown in order as in source,
        however for pdf output above header is discarded, and below output is put in the page after the table of contents. 
        See: https://stackoverflow.com/questions/27965192/python-sphinx-skips-first-section-when-generating-pdf


Documentation version '|DOCVERSION|' for TorXakis version '|TOOLVERSION|'. 

This documentation is also available as printable format as `PDF document <PDFDOCUMENTURL_>`_ .  
For other versions see the `documentation overview webpage <DOCUMENT_OVERVIEW_URL_>`_. 

test4

.. toctree::
   :caption: Contents

   intro
   xtest 

.. toctree::
   :caption: Appendices
   :hidden:

   rst
   glossary
   bibliography
   genindex 

