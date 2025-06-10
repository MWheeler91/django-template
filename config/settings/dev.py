from .base import *

DEBUG = env.bool('DEBUG_DEV', default=True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV')
CORS_ORIGIN_ALLOW_ALL = True  # Dev-only convenience
CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS_DEV')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME_TEST'),
        'USER': env('DB_USER_TEST'),
        'PASSWORD': env('DB_PASSWORD_TEST'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    },
}
