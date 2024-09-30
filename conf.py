# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# pylint: skip-file

# project information

project = 'PhasorPy'
copyright = '2022-2024 PhasorPy Contributors'
author = 'PhasorPy Contributors'

# general configuration

extensions = [
    'sphinx.ext.todo',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# options for HTML output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_js_files = ['custom-icons.js']
html_show_sourcelink = False

html_title = 'PhasorPy homepage'

html_logo = '_static/logo.png'
# html_favicon = ''

pygments_style = 'sphinx'

# extension configurations

html_sidebars = {'**': []}

html_theme_options = {
    'logo': {
        'text': 'PhasorPy',
        'alt_text': 'PhasorPy',
        # 'image_dark': '_static/logo-dark.svg',
    },
    'header_links_before_dropdown': 3,
    'navigation_with_keys': False,
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/phasorpy/phasorpy',
            'icon': 'fa-brands fa-github',
        },
        {
            'name': 'PyPI',
            'url': 'https://pypi.org/project/phasorpy/',
            'icon': 'fa-custom fa-pypi',
            'type': 'fontawesome',
        },
    ],
    'secondary_sidebar_items': [],
    'navbar_persistent': [],
    'show_prev_next': False,
}
