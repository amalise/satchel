from .base import *

DEBUG = True


# Security Settings
# https://tonyteaches.tech/django-production-server-settings/
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

#SECURE_HSTS_SECONDS = 300  # 5 minutes
#SECURE_HSTS_PRELOAD = True
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# Local Settings
try:
    from .local_settings import *
except ImportError:
    pass
