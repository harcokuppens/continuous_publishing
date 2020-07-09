# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html



# -- General configuration ---------------------------------------------------

project = 'Continuous Publishing'
copyright = '2020, Harco Kuppens'
author = 'Harco Kuppens'


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx.ext.extlinks','sphinx.ext.todo',
        'sphinx.ext.mathjax','sphinx.ext.graphviz'
]


graphviz_output_format='svg'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# using :ref: we can use sphinx cross referencing in a sphinx document (between possible different rst files in sphinx project)
# however :ref: is only used for internal linking, for external linking you must use the standard restructured text
# syntax using a role with an ending _ character. You can even separate the link and the target definition.
# However the  target definition from standard restructured text only holds for the current rst file.
# The trick to have target definitions hold for all rst files in the sphinx project is to include to each
# rst file the target definitions. We do this by adding an include directive for including hyperlinks.rst
# to the rst_epilog, so that hyperlinks.rst is then automatically include to rst file.
rst_epilog="""
.. include:: hyperlinks.rst
"""


# -- configuration for restructured text appendix  -----------------------

extlinks = {'duref': ('http://docutils.sourceforge.net/docs/ref/rst/'
                      'restructuredtext.html#%s', ''),
            'durole': ('http://docutils.sourceforge.net/docs/ref/rst/'
                       'roles.html#%s', ''),
            'dudir': ('http://docutils.sourceforge.net/docs/ref/rst/'
                      'directives.html#%s', '')}


# -- Load Continuous publishing configuration ---------------------------------------------------

includefile='continuous_publishing.py'
exec(compile(source=open(includefile).read(), filename=includefile, mode='exec'))
