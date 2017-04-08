from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
#
#import dj_database_url
#DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOST = ['*']


import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
