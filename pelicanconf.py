#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Prasanna Venkadesh'
SITENAME = u'Towards Freedom'
SITEURL = 'https://prasannavenkadesh.github.io/blog'
TAGLINE = 'Free Software + Free Culture = Free Society'
USER_LOGO_URL = SITEURL + '/images/pic.jpg'

THEME = os.getenv("PELICAN_THEME")

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Diaspora', 'https://joindiaspora.com/u/impras'),
         ('Github', 'https://github.com/prasannavenkadesh')
        )

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
