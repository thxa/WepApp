""" Production Settings """

import os
import dj_database_url
from .dev import *

#DATABASES = {
#    'default': dj_database_url.config(
#        default=os.getenv('DATABASE_URL')
#    )
#}


############
# SECURITY #
############

DEBUG = bool(os.getenv('DJANGO_DEBUG', ''))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')