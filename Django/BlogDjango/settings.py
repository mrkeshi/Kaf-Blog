import os
import sys
import locale
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Mode
MODE = os.getenv('MODE', 'development')

# Debug Mode

# Secret Key
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-u94yalk5h0opwa0w+re68=%!_h^mkm-kdi-joboaj*!sj6o3eo')

# Allowed Hosts
if MODE == 'production':
    DEBUG=False
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
else:
    ALLOWED_HOSTS = []
    DEBUG=True


# Base URL
BASE_URL = os.getenv('BASE_URL', 'http://localhost:3000/')

# VAPID Key
VAPID_PRIVATE_KEY = os.getenv('VAPID_PRIVATE_KEY', 'VdQh39PVZiSYLNqG8yhHDtnloDQyuG67sqT429XdZpI')

# Installed Apps
INSTALLED_APPS = [
    "corsheaders",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'jalali_date',
    'axes',
    'rest_framework',
    'drf_yasg',
    'Setting',
    'Contact',
    'Post'
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware'
]

# URL Config
ROOT_URLCONF = 'BlogDjango.urls'

# Auth Backends
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'BlogDjango.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Language and Timezone
LANGUAGE_CODE = 'fa'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static and Media Files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
CKEDITOR_UPLOAD_PATH = "uploads/"

# Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jalali Settings
JALALI_DATE_DEFAULTS = {
    'LIST_DISPLAY_AUTO_CONVERT': False,
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': ['admin/js/django_jalali.min.js'],
        'css': {'all': ['admin/css/django_jalali.min.css']}
    },
}

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '150/hour' if MODE == 'production' else '1000/hour',
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 8,
}

# Disable Browsable API in production
if MODE == 'production':
    from rest_framework.renderers import JSONRenderer
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
     'rest_framework.renderers.JSONRenderer',
    )
else:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
# Locale
if sys.platform.startswith('win32'):
    locale.setlocale(locale.LC_ALL, "Persian_Iran.UTF-8")
else:
    locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")


FRONTEND_DOMAINS = os.getenv("FRONTEND_DOMAINS","http://localhost:3000").split(",")

if MODE == 'production':
    CORS_ALLOWED_ORIGINS = FRONTEND_DOMAINS
    CSRF_TRUSTED_ORIGINS = FRONTEND_DOMAINS
    CORS_ALLOW_CREDENTIALS = True
    CSRF_COOKIE_HTTPONLY = False
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'Lax'
else:
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOWED_ORIGINS = FRONTEND_DOMAINS

