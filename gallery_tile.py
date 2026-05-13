"""Custom directive to render Sphinx-Gallery style tutorial tiles."""

from __future__ import annotations

from html import escape
from typing import TYPE_CHECKING
from urllib.parse import urlsplit

from docutils import nodes
from docutils.parsers.rst.directives import unchanged
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx

DEFAULT_DOCS_ROOT = 'https://www.phasorpy.org/docs/stable/'


def resolve_url(value: str, prefix: str) -> str:
    """Return absolute URL for relative values using a default prefix."""
    if value.startswith(('http://', 'https://', '/', '#')):
        return value
    return f'{prefix}{value}'


def ensure_trailing_slash(value: str) -> str:
    """Ensure URL prefix has trailing slash for safe concatenation."""
    return value if value.endswith('/') else f'{value}/'


def normalize_tutorial_value(value: str) -> str:
    """Normalize tutorial path values while preserving absolute URLs."""
    if value.startswith(('http://', 'https://', '/', '#')):
        return value
    return value.strip('/')


def derive_thumb_filename(link_value: str) -> str:
    """Derive Sphinx-Gallery thumbnail filename from tutorial link."""
    path = urlsplit(link_value).path.strip('/')
    slug = path.rsplit('/', 1)[-1]
    if not slug:
        msg = 'cannot derive thumbnail filename from empty link path'
        raise ValueError(msg)
    return f'sphx_glr_{slug}_thumb.png'


def derive_title_from_tutorial(tutorial_value: str) -> str:
    """Create a readable title from the last tutorial path segment."""
    slug = tutorial_value.rsplit('/', 1)[-1]
    return slug.replace('_', ' ').strip().title()


class GalleryTileDirective(SphinxDirective):
    """Render a single tutorial tile matching Sphinx-Gallery classes.

    Usage:

    .. gallery-tile:: api/phasorpy_io
      :title: File input/output
      :description: ...

    """

    required_arguments = 1
    final_argument_whitespace = True
    has_content = False
    option_spec = {
        'title': unchanged,
        'img': unchanged,
        'link-prefix': unchanged,
        'img-prefix': unchanged,
        'tooltip': unchanged,
        'description': unchanged,
    }

    def run(self) -> list[nodes.raw]:
        """Build and return raw HTML for one gallery tile."""
        argument_value = self.arguments[0].strip()
        docs_root = ensure_trailing_slash(self.env.config.gallery_docs_root)
        link_prefix = self.options.get(
            'link-prefix', f'{docs_root}tutorials/'
        ).strip()
        img_prefix = self.options.get(
            'img-prefix', f'{docs_root}_images/'
        ).strip()

        link_value = normalize_tutorial_value(argument_value)
        title = self.options.get(
            'title', derive_title_from_tutorial(link_value)
        ).strip()

        if not link_value:
            msg = 'gallery-tile requires a non-empty tutorial value.'
            raise self.error(msg)

        img_value = self.options.get('img', '').strip()
        if not img_value:
            try:
                img_value = derive_thumb_filename(link_value)
            except ValueError as exc:
                msg = (
                    'gallery-tile requires :img: or a tutorial value with '
                    f'a valid slug to derive thumbnail name ({exc}).'
                )
                raise self.error(msg) from exc

        link = resolve_url(link_value, link_prefix)
        img = resolve_url(img_value, img_prefix)
        tooltip = self.options.get(
            'tooltip', self.options.get('description', title)
        )
        assert tooltip is not None
        tooltip = tooltip.strip()

        html = (
            '<div class="sphx-glr-thumbcontainer" '
            f'tooltip="{escape(tooltip)}">'
            f'<img alt="{escape(title)}" src="{escape(img)}" />'
            '<p>'
            f'<a class="reference internal" href="{escape(link)}">'
            f'<span>{escape(title)}</span>'
            '</a>'
            '</p>'
            f'<div class="sphx-glr-thumbnail-title">{escape(title)}</div>'
            '</div>'
        )
        return [nodes.raw('', html, format='html')]


def setup(app: Sphinx) -> dict[str, bool]:
    """Register the gallery tile directive."""
    app.add_config_value('gallery_docs_root', DEFAULT_DOCS_ROOT, 'env')
    app.add_directive('gallery-tile', GalleryTileDirective)
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
