from django.contrib.messages import constants as messages
from django.utils.translation import ugettext_lazy as _
from pathlib import Path
import os, sys, json
from setup import env

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG']
ALLOWED_HOSTS = json.loads(os.environ['ALLOWED_HOSTS'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    # third party apps
    'rest_framework',
    'django_filters',
    'corsheaders',
    # my apps
    'app_example',
    'stock_prices',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'

# database
USE_SQLITE = os.environ['USE_SQLITE']
if USE_SQLITE: # sqlite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else: # other
    DATABASES = json.loads(os.environ['DATABASES'])


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# time zone and language
LANGUAGES = (
    ('en', _('English')),
    ('pt-br', _('Portuguese')),
)
LANGUAGE_CODE = os.environ['LANGUAGE_CODE']
TIME_ZONE = os.environ['TIME_ZONE']
USE_I18N = True
USE_L10N = True
USE_TZ = True

# locale
LOCALE_PATHS = [ BASE_DIR / 'locale' ]

# cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUD_NAME'],
    'API_KEY': os.environ['API_KEY'],
    'API_SECRET': os.environ['API_SECRET'],
}

# static and media
USE_S3 = os.environ['USE_S3']
USE_CLOUDINARY = os.environ['USE_CLOUDINARY']
STATICFILES_DIRS = [ BASE_DIR / 'setup/static' ]

# aws s3
AWS_STATIC_LOCATION = 'static'
AWS_PRIVATE_MEDIA_LOCATION = os.environ['AWS_PRIVATE_MEDIA_LOCATION']
AWS_PUBLIC_MEDIA_LOCATION = os.environ['AWS_PUBLIC_MEDIA_LOCATION']

if not USE_S3:
    STATIC_ROOT = BASE_DIR / 'static'
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

    if USE_CLOUDINARY:
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
else:
    AWS_QUERYSTRING_AUTH = False
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

    AWS_S3_CUSTOM_DOMAIN = f'{ AWS_STORAGE_BUCKET_NAME }.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_DEFAULT_ACL = None
    STATIC_URL = f'https://{ AWS_S3_CUSTOM_DOMAIN }/{ AWS_STATIC_LOCATION }/'
    STATICFILES_STORAGE = os.environ['STATICFILES_STORAGE']
    DEFAULT_FILE_STORAGE = os.environ['DEFAULT_FILE_STORAGE']
    PRIVATE_FILE_STORAGE = os.environ['PRIVATE_FILE_STORAGE']

# apps folder
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success',
}

# API configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
}

# CORS
CORS_ALLOWED_ORIGINS = json.loads(os.environ['CORS_ALLOWED_ORIGINS'])
