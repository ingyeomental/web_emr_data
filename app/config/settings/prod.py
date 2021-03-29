from ._base import *

DEBUG = False
ALLOWED_HOSTS = ['*']
WSGI_APPLICATION = 'config.wsgi.prod.application'
INSTALLED_APPS += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PROD_DB_NAME'),
        'USER': config('PROD_DB_USER'),
        'PASSWORD': config('PROD_DB_PASSWORD'),
        'HOST': config('PROD_DB_HOST'),
        'PORT': 5432,
    }
}