Installation
============

This part of the documentation covers the installation of Sphinx Readability Theme.

Distribute & Pip
----------------

To use this style in your Sphinx documentation, follow this guide.

Installing this theme is simple with pip::

    $ pip install sphinxtheme.readability

Or, with easy_install::

    $ sudo easy_install sphinxtheme.readability

A few seconds later and you are good to go.

Setup
-----

Add this to your ``conf.py``::

    import sphinxtheme

    readability_path = os.path.dirname(os.path.abspath(sphinxtheme.__file__))
    relative_path = os.path.relpath(readability_path, os.path.abspath('.'))

    html_theme = 'readability'
    html_theme_path = [relative_path]

Themes
------

The following themes exist:

- newspaper (default)
- novel
- ebook
- inverse
- athelas

If you change theme for your document, you can change ``html_theme_options`` like this::

    html_theme_options = {
        'readabilitystyle': 'novel'
    }

Options
-------

The following options exist:

- readabilitystyle
- index_logo_name
- index_logo_alt
- nosidebar
- sidebarwidth

Pygments Style
--------------

If you want to use readability highlighted code, set below::

    pygments_style = 'readability_theme_support.ReadabilityStyle'
