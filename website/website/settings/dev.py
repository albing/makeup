from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-%*2+u1vo=-fh9(#dh2ab99zi1neupf@$!b%9xufma5=b6rs$7'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = [
        'makeup-artist-gregalbing.c9users.io',
        'localhost',
        '127.0.0.1',
        '[::1]'
    ]

try:
    from .local import *
except ImportError:
    pass
