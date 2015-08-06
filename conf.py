# import sys, os
# sys.path.append(os.path.abspath('_ext'))

extensions = [ 
    # 'matplotlib.sphinxext.mathmpl',
    # 'matplotlib.sphinxext.only_directives',
    # 'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage', 
    'sphinx.ext.doctest', 
    'sphinx.ext.ifconfig', 
    'sphinx.ext.intersphinx',
    'sphinx.ext.pngmath',
    'sphinx.ext.todo', 
    'sphinx.ext.viewcode',
    # "sphinxcontrib.blockdiag", 
    # "sphinxcontrib.seqdiag",
] 

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Grundwissen Elektronik'
copyright = u'2011-2015, Bernhard Grotz'
version = '0.1.3'
release = '0.1.3'
language = 'de'
spelling_lang = 'de_DE'
html_show_copyright = False
html_show_sphinx = False
exclude_patterns = ["notes.rst", "*/notes.rst", "**/notes.rst"]
pygments_style = 'sphinx'
html_theme = 'sphinxdoc'
html_static_path = ['_static']
html_additional_pages = {'home': 'home.html'}
htmlhelp_basename = 'Grundwissen Elektronik'
html_title = "Grundwissen Elektronik"
html_short_title = "Grundwissen Elektronik"
html_logo = "logo.png"
html_favicon = "favicon.ico"
todo_include_todos = False
number_figures=False
figure_caption_prefix="Abbildung"
html_last_updated_fmt = '%d. %b %Y'
html_search_language = 'en'
html_search_options = {'type': 'default'}

trim_footnote_reference_space = True

latex_preamble = r'''
\usepackage[version=3]{mhchem}
\usepackage{amsmath, units}
\usepackage{amsfonts, amssymb}
\usepackage{nicefrac} 
\setlength{\headheight}{15pt}
\setcounter{secnumdepth}{-1}
\setcounter{tocdepth}{2}
\clubpenalty  = 10000 % Disable single lines at the start of a page (Schusterjungen)
\widowpenalty = 10000 % Disable single lines at the end   of a page (Hurenkinder)
\displaywidowpenalty = 10000
'''

pngmath_latex_preamble = latex_preamble
latex_elements = {
    "preamble": latex_preamble,
    "papersize": 'a4paper',
    "pointsize": '12pt',
    "fontpkg": '',
    "babel":    "\\usepackage[ngerman]{babel}",
    "fncychap": '\\usepackage[Conny]{fncychap}',
}

texinfo_documents = [
  ('index', 'Grundwissen Elektronik', u'Grundwissen Elektronik',
   u'Bernhard Grotz', 'Grundwissen Elektronik', 'Grundwissen Elektronik',
   'Miscellaneous'),
]

latex_documents = [
  ('index', 'grundwissen-elektronik.tex', u'Grundwissen Elektronik',
   u'Bernhard Grotz', 'manual'),
]

intersphinx_mapping = {
    'gw': ('http://grund-wissen.de/', None),
    'gwm': ('http://grund-wissen.de/mathematik', None),
    'gwp': ('http://grund-wissen.de/physik', None),
    'gwl': ('http://grund-wissen.de/linux', None),
    'gwic': ('http://grund-wissen.de/informatik/c', None),
    'gwil': ('http://grund-wissen.de/informatik/latex', None),
    'gwip': ('http://grund-wissen.de/informatik/python', None),
}


