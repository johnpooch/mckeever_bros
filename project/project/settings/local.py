from .base import *

SECRET_KEY = 'ifoehwfgqingqojg5348423589hfbjnsd'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}