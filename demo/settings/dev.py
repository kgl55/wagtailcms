from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b!06wd(oh=cj))7t$zylq%*bnp0jo3g)u#rj1=zw*^64g-&g8o'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# 你的邮箱账号与密码
EMAIL_HOST_USER = '*****'
EMAIL_HOST_PASSWORD = '*****'
# 由于使用25端口，一般都不使用TLS机密，SSL和TSL只需要设置一个，他们同时为True或False
EMAIL_USE_TLS = False

try:
    from .local import *
except ImportError:
    pass
