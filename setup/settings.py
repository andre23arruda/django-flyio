from pathlib import Path
import json, os, sys
import dj_database_url
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
envpath = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=envpath)

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '["*"]')
DEBUG = json.loads(os.getenv('DEBUG', 'false'))
ENVIRONMENT = os.getenv('ENVIRONMENT', 'DEV')
SECRET_KEY = os.getenv('SECRET_KEY')

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party apps
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    # my apps
    'library',
    'ping',
    'profiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Database
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# apps folder
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# DRF settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT =  'static/'
STATICFILES_DIRS = [ 'setup/static' ]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Swagger/Django will serve over http, force https here
if ENVIRONMENT == 'PROD':
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    MIDDLEWARE.insert(1,'whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = json.loads(os.getenv('CORS_ALLOWED_ORIGINS', '[]'))

from .config.swagger import SWAGGER_SETTINGS
from .config.theme import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS