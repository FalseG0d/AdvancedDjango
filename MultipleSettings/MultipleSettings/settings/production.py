from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', ]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Apoorv'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True