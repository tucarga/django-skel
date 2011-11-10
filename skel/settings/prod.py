"""Production settings and globals."""


from os import environ
from sys import exc_info
from urlparse import urlparse, uses_netloc

from common import *


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host
EMAIL_HOST = environ['EMAIL_HOST'] or 'smtp.gmail.com'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ['EMAIL_HOST_PASSWORD'] or ''

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host-user
EMAIL_HOST_USER = environ['EMAIL_HOST_USER'] or 'your_email@example.com'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-port
EMAIL_PORT = environ['EMAIL_PORT'] or 587

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-use-tls
EMAIL_USE_TLS = True
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: http://devcenter.heroku.com/articles/django#postgres_database_config
uses_netloc.append('postgres')
uses_netloc.append('mysql')

try:
    if environ.has_key('DATABASE_URL'):
        url = urlparse(environ['DATABASE_URL'])
        DATABASES['default'] = {
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        }
        if url.scheme == 'postgres':
            DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
        if url.scheme == 'mysql':
            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
except:
    print "Unexpected error:", exc_info()
########## DATABASE CONFIGURATION