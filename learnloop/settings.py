#
# """
# Django settings for learnloop project.
# Agentic AI Learning Platform - Backend Architecture
# """
#
# from pathlib import Path
# from datetime import timedelta
# import os
# from dotenv import load_dotenv
#
# # Load environment variables
# load_dotenv()
#
# # Build paths inside the project
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-change-me-in-production')
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() in ('true', '1', 'yes')
#
# ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
#
# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#
#     # Third-party apps
#     'rest_framework',
#     'corsheaders',
#     'drf_yasg',  # API documentation (optional)
#
#     # Local apps
#     'core',
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'learnloop.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'learnloop.wsgi.application'
#
# # Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DATABASE_NAME', 'learnloop'),
#         'USER': os.getenv('DATABASE_USER', 'learnloop'),
#         'PASSWORD': os.getenv('DATABASE_PASSWORD', 'learnloop'),
#         'HOST': os.getenv('DATABASE_HOST', 'localhost'),
#         'PORT': os.getenv('DATABASE_PORT', '5432'),
#         'CONN_MAX_AGE': 60,  # Persistent connections
#     }
# }
#
# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]
#
# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True
#
# # Static files (CSS, JavaScript, Images)
# STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
#
# # Default primary key field type
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# # =============================================================================
# # REST FRAMEWORK CONFIGURATION
# # =============================================================================
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 20,
#     'DEFAULT_THROTTLE_CLASSES': [
#         'rest_framework.throttling.AnonRateThrottle',
#         'rest_framework.throttling.UserRateThrottle',
#     ],
#     'DEFAULT_THROTTLE_RATES': {
#         'anon': '100/day',
#         'user': '1000/day',
#     },
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#     ],
# }
#
# # =============================================================================
# # CORS CONFIGURATION
# # =============================================================================
# CORS_ALLOWED_ORIGINS = os.getenv(
#     'CORS_ALLOWED_ORIGINS',
#     'http://localhost:3000,http://localhost:8000'
# ).split(',')
#
# CORS_ALLOW_CREDENTIALS = True
#
# # =============================================================================
# # CELERY CONFIGURATION
# # =============================================================================
# CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
# CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = TIME_ZONE
# CELERY_WORKER_PREFETCH_MULTIPLIER = 1
# CELERY_TASK_ACKS_LATE = True
#
# # Task routes for different agent types
# CELERY_ROUTES = {
#     'core.tasks.process_learning_interaction': {'queue': 'agent_tasks'},
#     'core.tasks.evaluate_interaction': {'queue': 'evaluation_tasks'},
# }
#
# # =============================================================================
# # LOGGING CONFIGURATION
# # =============================================================================
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#         },
#         'file': {
#             'class': 'logging.FileHandler',
#             'filename': BASE_DIR / 'logs' / 'learnloop.log',
#             'formatter': 'verbose',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'level': os.getenv('LOG_LEVEL', 'INFO'),
#             'propagate': True,
#         },
#         'core.agents': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#         },
#         'core.evaluation': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#         },
#     },
# }
#
# # =============================================================================
# # AI/ML CONFIGURATION
# # =============================================================================
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
# OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4-turbo')
# OPENAI_TEMPERATURE = float(os.getenv('OPENAI_TEMPERATURE', '0.7'))
#
# # Agent configuration
# AGENT_CONFIG = {
#     'max_tokens': 1000,
#     'timeout': 30,
#     'retry_attempts': 3,
# }
#
# # Evaluation configuration
# EVALUATION_CONFIG = {
#     'scoring_model': os.getenv('EVALUATION_MODEL', 'gpt-4-turbo'),
#     'enable_auto_scoring': True,
#     'min_score_threshold': 0.5,
# }
#
# # =============================================================================
# # SECURITY SETTINGS (Production)
# # =============================================================================
# if not DEBUG:
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True
#     SECURE_BROWSER_XSS_FILTER = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
#     X_FRAME_OPTIONS = 'DENY'
#     SECURE_HSTS_SECONDS = 31536000
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_PRELOAD = True
#
# # =============================================================================
# # RATE LIMITING (Redis-based for production)
# # =============================================================================
# RATELIMIT_ENABLE = not DEBUG
# RATELIMIT_USE_CACHE = 'default'
#
# # =============================================================================
# # API DOCUMENTATION (Optional)
# # =============================================================================
# SWAGGER_SETTINGS = {
#     'SECURITY_DEFINITIONS': {
#         'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header',
#         }
#     },
# }




"""
Django settings for learnloop project.

Generated by 'django-admin startproject' using Django 6.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aj=c=j%+z8n!9&&p118i!7i9v8rv-c^6nn%$x3*jmv)9cy5@6i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

   # Third-party apps
    'rest_framework',
    'corsheaders',
    'drf_yasg',  # API documentation (optional)

     # Local apps
    'core',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learnloop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'learnloop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'










