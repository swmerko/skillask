"""
Django settings for SKILLASK project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Parse database configuration from $DATABASE_URL
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u=&4_%b^b&cg_-cc$=k(c8%5id_y7j9cnhvz$g#7zf^fr_(3nw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # pip
    'treebeard',
    'rest_framework',
    'django_filters',
    'social.apps.django_app.default',
    'sorl.thumbnail',
    'oauth2_provider',
    'corsheaders',
    # custom
    'accounts',
    'skills',
    'home',
    'search',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'SKILLASK.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'SKILLASK.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ],
    # 'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope'},
    'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

CORS_ORIGIN_ALLOW_ALL = True

# python social auth

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.linkedin.LinkedinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '771zsqdcdo6g9g'
SOCIAL_AUTH_FACEBOOK_SECRET = 'ZsJPEKGTrrk48IRx'
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
    'public_profile',
    'user_friends',
    'user_website',
    'user_location',
    'user_about_me'
]

SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'ZsJPEKGTrrk48IRx'
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '771zsqdcdo6g9g'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = [
    'r_basicprofile',
    'r_emailaddress',
    'rw_company_admin',
    'w_share'
]
SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [
    ('id', 'id'),
    ('firstName', 'first_name'),
    ('lastName', 'last_name'),
    ('emailAddress', 'email_address'),
    ('headline', 'headline'),
    ('industry', 'industry'),
    ('skills', 'skills'),
]

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'accounts.pipeline.save_profile_picture',
    'accounts.pipeline.save_location',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'post_social_login'

try:
    if os.environ['S3_ID'] == 'LIVE':
        CURRENT_ENV = 'LIVE'
    else:
        CURRENT_ENV = 'LOCAL'

except KeyError:
    CURRENT_ENV = 'LOCAL'

if CURRENT_ENV == 'LIVE':
    # Amazon S3
    AWS_STORAGE_BUCKET_NAME = 'skillaskmedia'
    AWS_ACCESS_KEY_ID = os.environ['S3_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['S3_KEY']

    # Tell django-storages that when coming up with the URL for an item in S3 storage, keep
    # it simple - just use this domain plus the path. (If this isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
    # We also use it in the next setting.
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
    # you run `collectstatic`).

    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'core.custom_storages.MediaStorage'
    DATABASES['default'] = dj_database_url.config()
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
