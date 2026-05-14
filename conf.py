"""Configuration file for the Sphinx documentation builder.

https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

# project information

project = 'PhasorPy'
copyright = '2022-2026 PhasorPy Contributors'
author = 'PhasorPy Contributors'

# general configuration

extensions = [
    'sphinx.ext.todo',
    'sphinx_design',
    'gallery_tile',
    'notfound.extension',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# options for HTML output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_js_files = [('custom-icons.js', {'defer': 'defer'})]
html_css_files = ['sg_gallery.css', 'custom.css']
html_show_sourcelink = False

html_title = 'PhasorPy homepage'

html_logo = '_static/phasorpy_logo.svg'
html_favicon = '_static/favicon.ico'

gallery_docs_root = 'https://www.phasorpy.org/docs/stable/'

html_title = ''
html_short_title = ''

pygments_style = 'sphinx'

# extension configurations

notfound_urls_prefix = None

html_sidebars: dict[str, list[str]] = {'**': []}

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
        'navbar-icon-links',
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


def _copy_404_for_dirhtml(app: Any, exception: Any) -> None:
    """Copy 404/index.html to 404.html for dirhtml builds."""
    if exception is not None or app.builder.name != 'dirhtml':
        return
    src = Path(app.outdir) / '404' / 'index.html'
    dst = Path(app.outdir) / '404.html'
    if src.exists():
        content = src.read_text(encoding='utf-8')
        content = content.replace(
            'data-content_root="../"', 'data-content_root="./"'
        )
        dst.write_text(content, encoding='utf-8')


def setup(app: Any) -> None:
    """Connect build-finished event to copy 404 page for dirhtml builds."""
    app.connect('build-finished', _copy_404_for_dirhtml)
