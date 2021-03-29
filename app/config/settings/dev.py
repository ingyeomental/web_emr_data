from ._base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
WSGI_APPLICATION = 'config.wsgi.dev.application'
INSTALLED_APPS += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DEV_DB_NAME'),
        'USER': config('DEV_DB_USER'),
        'PASSWORD': config('DEV_DB_PASSWORD'),
        'HOST': config('DEV_DB_HOST'),
        'PORT': 5432,
    }
}