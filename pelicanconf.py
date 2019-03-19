#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Prasanna Venkadesh'
SITENAME = u'Towards Freedom'
SITEURL = 'http://blog.purambokku.me'
TAGLINE = '<a href="https://www.gnu.org/philosophy/free-sw.en.html" target="_blank">Free Software</a> + Free Culture = Free Society'
USER_LOGO_URL = SITEURL + '/images/pic.png'

THEME = os.getenv("PELICAN_THEME")
print (THEME)

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About', 'https://prasannavenkadesh.github.io'),
        ('Social', 'https://mastodon.social/users/prashere'),
         ('Code', 'https://gitlab.com/prashere'),
         ('மாற்று', 'http://maattru.com/author/prashere/')
        )

# Social widget
# SOCIAL = ()

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
