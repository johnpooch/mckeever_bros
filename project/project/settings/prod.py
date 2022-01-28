from .base import *
import dj_database_url
import django_heroku
import os

DATABASES = {'default': dj_database_url.parse(os.environ['DATABASE_URL'])}

ALLOWED_HOSTS = ['johnpooch-mckeever-bros.herokuapp.com']

SECRET_KEY = os.environ['SECRET_KEY']

django_heroku.settings(locals())