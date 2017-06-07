#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Benjamin Hillmann'
SITENAME = "Ben of 1"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['plugins', os.path.join('plugins', 'pelican-plugins')]
PLUGINS = ['pelican-ipynb.markup', 'i18n_subsites']


#banner
BANNER='images/mountain_night.jpg'

#path config
STATIC_PATHS=['images', 'extra/favicon.ico', 'extra/robots.txt']

THEME = os.path.join('themes', 'pelican-themes', 'pelican-bootstrap3')
BOOTSTRAP_THEME = 'simplex'
PYGMENTS_STYLE = 'xcode'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
