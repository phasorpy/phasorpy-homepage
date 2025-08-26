# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# pylint: skip-file

# project information

project = 'PhasorPy'
copyright = '2022-2025 PhasorPy Contributors'
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

html_logo = '_static/phasorpy_logo.svg'
html_favicon = '_static/favicon.ico'

html_title = ''
html_short_title = ''

pygments_style = 'sphinx'

# extension configurations

html_sidebars = {'**': []}

html_theme_options = {
    'logo': {
        'text': 'PhasorPy',
        'alt_text': 'PhasorPy',
    },
    'header_links_before_dropdown': 4,
    'navigation_with_keys': False,
    # 'collapse_navigation': True,
    'navbar_align': 'content',  # [left, content, right]
    'navbar_persistent': [],
    # 'navbar_center': [],  # , 'version-switcher', 'navbar-nav'
    'navbar_end': [
        # 'search-button',
        # 'version-switcher',
        'theme-switcher',
        'navbar-icon-links'
    ],
    'icon_links': [
        {
            'name': 'PyPI',
            'url': 'https://pypi.org/project/phasorpy/',
            'icon': 'fa-custom fa-pypi',
            'type': 'fontawesome',
        },
        {
            'name': 'GitHub',
            'url': 'https://github.com/phasorpy/phasorpy',
            'icon': 'fa-brands fa-github',
        },
        # {
        #     'name': 'Home',
        #     'url': 'https://www.phasorpy.org',
        #     'icon': 'fa fa-home',
        # },
    ],
    # 'secondary_sidebar_items': [],
    'show_prev_next': False,
}
