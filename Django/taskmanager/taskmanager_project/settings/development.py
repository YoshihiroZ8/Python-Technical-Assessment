from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# For development, allow all hosts
ALLOWED_HOSTS = ['*']

# Email settings for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'