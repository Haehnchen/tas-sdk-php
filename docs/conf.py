import sys
import os

from sphinx.highlighting import lexers
from pygments.lexers.compiled import CLexer
from pygments.lexers.special import TextLexer
from pygments.lexers.text import RstLexer
from pygments.lexers.web import PhpLexer

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'tas-sdk-php'
copyright = u'2016, trivago GmbH'
author = u'trivago GmbH'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'tas-sdk-php-doc'

html_sidebars = {
   '**': ['globaltoc.html']
}

html_show_sphinx = False
html_show_copyright = False
html_show_sourcelink = False

lexers['markdown'] = TextLexer()
lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
lexers['php-standalone'] = PhpLexer(startinline=True)
lexers['rst'] = RstLexer()
lexers['varnish3'] = CLexer()
lexers['varnish4'] = CLexer()

config_block = {
    'markdown': 'Markdown',
    'rst': 'reStructuredText',
    'varnish3': 'Varnish 3',
    'varnish4': 'Varnish 4'
}
