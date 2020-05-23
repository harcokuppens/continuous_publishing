# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Example sphinx'
copyright = '2020, Harco Kuppens'
author = 'Harco Kuppens'

github_user_or_organisation='harcokuppens'
github_repo_name=="example_sphinx_doc_repo"

# ----------------------------------------------------------------------------



def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    import unicodedata
    import re
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower()).strip()
    return re.sub(r'[\s]+', '', value)


output_pdf="build/latex/" + slugify(project) + ".pdf"
print("::set-env name=SPHINX_BUILD_PDF::" + output_pdf)

# -- Automatically add toolversion,docversion and pdfdocumenturl  -----------------------


# This adds 'toolversion' as variable to sphinx documentation.
# Use in .rst file as |toolversion|
# eg. Documentation for TorXakis version: |toolversion|
with open('TOOLVERSION.txt') as f:
    toolversion = f.readline()
toolversion=toolversion.strip()    



import subprocess
tag=subprocess.check_output(["git","tag", "--points-at","HEAD"])
if tag:
   display_edit_on_github=False
   docversion=str(tag)
   html_docversion="Stable docs (tag " + docversion+")"
   pdf_docversion="Document version " + docversion   
else:   
   display_edit_on_github=True
   docversion=subprocess.check_output(["git","rev-parse","--short","HEAD"])
   docversion="git-sha1-" + str(docversion,'utf-8').strip()
   
   ret=subprocess.call(["git","diff","--quiet"])
   if ret == 1:
       docversion=docversion+"+"

   html_docversion="Latest docs (" + docversion +")"
   pdf_docversion="Document version " + docversion   

# show in left top corner in html build
version="version: " + toolversion + "<br/>" + html_docversion
# show on first page in pdf build
release= toolversion + ", " + pdf_docversion

import os
# DOCUMENT_URL_PDF is set by previous github workflow which build and uploaded the pdf
# for local builds this variable won't be set and no pdf link is added
pdfdocumenturl=os.environ.get('DOCUMENT_URL_PDF')
if pdfdocumenturl:
   # add link to pdf in html theme below version
   version = version + r'<br/><a style="color:white" href="' + pdfdocumenturl + '">pdf</a>'
else:
    pdfdocumenturl="https://for.local.build.no.pdf.is.uploaded"

document_overview_url="https://{0}.github.io/{1}/".format(github_user_or_organisation,github_repo_name)

print("docversion: " +docversion)        
print("toolversion: " +toolversion)        
print("pdfdocumenturl: " +pdfdocumenturl)        
print("document_overview_url: " +document_overview_url)        

#rst_code = '''
rst_epilog = '''
.. |TOOLVERSION| replace:: {toolversion}
.. |DOCVERSION| replace:: {docversion}
.. _PDFDOCUMENTURL: {pdfdocumenturl}
.. _DOCUMENT_OVERVIEW_URL: {document_overview_url}
'''.format(toolversion=toolversion,pdfdocumenturl=pdfdocumenturl,docversion=docversion,document_overview_url=document_overview_url)
# see for the hyperref syntax: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#embedded-uris-and-aliases


extlinks = {'duref': ('http://docutils.sourceforge.net/docs/ref/rst/'
                      'restructuredtext.html#%s', ''),
            'durole': ('http://docutils.sourceforge.net/docs/ref/rst/'
                       'roles.html#%s', ''),
            'dudir': ('http://docutils.sourceforge.net/docs/ref/rst/'
                      'directives.html#%s', '')}



# -- General configuration ---------------------------------------------------
import sphinx_rtd_theme

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        "sphinx_rtd_theme",  'sphinx.ext.extlinks',
        'sphinx.ext.mathjax','sphinx.ext.graphviz'
]

graphviz_output_format='svg'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

html_theme = "sphinx_rtd_theme"

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

html_theme_options = {
#    'canonical_url': '',
#    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
#    'prev_next_buttons_location': 'bottom',
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    #'vcs_pageview_mode': 'blob',  => notexisting option
#    'style_nav_header_background': 'blue',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}


# edit on github
#---------------

#https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=html_context#confval-html_context
# html_context: A dictionary of values to pass into the template engine’s context for all pages.

github_user_or_organisation='harcokuppens'
github_repo_name=="example_sphinx_doc_repo"
# works
## https://github.com/readthedocs/sphinx_rtd_theme/issues/314#issuecomment-244646642-permalink
html_context = {
    # which fields there are see /usr/local/lib/python3.7/site-packages/sphinx_rtd_theme/breadcrumbs.html
    "show_source": False,
    "display_github": display_edit_on_github,
    "github_host": "github.com",
    "github_user": github_user_or_organisation,
    "github_repo": github_repo_name,
    "github_version": "master",
    "conf_py_path": "/source/",
    "source_suffix": '.rst',
}

# higher toc depth in latex bookmarks
#--------------------------------------
# https://www.sphinx-doc.org/en/master/latex.html#latex-elements-confval
#  use tocdepth to increase depth of bookmarks in pdf, see: https://github.com/sphinx-doc/sphinx/issues/2547
latex_elements = {
 'papersize': 'a4paper',
 'preamble': r'''
\setcounter{tocdepth}{9}
'''
}

#html_show_sourcelink = True
