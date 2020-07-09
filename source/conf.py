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
#exclude_patterns = []
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

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
