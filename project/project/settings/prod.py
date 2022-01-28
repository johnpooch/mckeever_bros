from .base import *
import dj_database_url
import django_heroku
import os

DATABASES = {'default': dj_database_url.parse(os.environ['DATABASE_URL'])}

ALLOWED_HOSTS = ['johnpooch-mckeever-bros.herokuapp.com']

SECRET_KEY = os.environ['SECRET_KEY']

django_heroku.settings(locals())

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[contactor] %(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

# Offline compression for django-compressor
COMPRESS_ENABLED = True