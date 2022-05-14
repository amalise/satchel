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


# DO NOT use on production, test key is available in the URL below
# https://developers.google.com/recaptcha/docs/faq
RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
NOCAPTCHA = True
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]


# Local Settings
try:
    from .local_settings import *
except ImportError:
    pass

