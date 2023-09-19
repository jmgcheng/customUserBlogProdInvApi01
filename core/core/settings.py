"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-czg^jv%69m%0%v)f!(rx9&y+803(mv2%_fc7e0++5*o-h+8*=3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'posts.apps.PostsConfig',
    'files.apps.FilesConfig',
    'products.apps.ProductsConfig',
    'purchases.apps.PurchasesConfig',
    'sales.apps.SalesConfig',

    'crispy_forms',
    'crispy_bootstrap4',

    'rest_framework',
    'rest_framework.authtoken',
    'api',    

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

# overrides the default behavior that's built in with django
# instead, I'm authenticating user using this custom one that I built
AUTH_USER_MODEL = 'users.CustomUser'

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
        BASE_DIR / "static",
        BASE_DIR / 'media',
    ]
STATIC_ROOT = BASE_DIR / "static_cdn"
# MEDIA_ROOT = BASE_DIR / 'media_cdn'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# do this if you use from django.contrib.auth import views as auth_views to manage your login
# so that django will not redirect to profile "default" after logging in
LOGIN_REDIRECT_URL = 'home'

# users get redirected here if trying to access page that needs authentication
LOGIN_URL = 'login'


HTML_SANITIZERS = {
    'default': {
        'tags': {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'img'},
        "attributes": {"img": ("src",)},
        'empty': {'img'},
        'separate': {'p'},
        "keep_typographic_whitespace": True,
    },
}

# for resetting password
# watch link below for continue setup
# https://youtu.be/-tyBEsHSv7w?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&t=729
# https://myaccount.google.com › apppasswords
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'emailUsername'
EMAIL_HOST_PASSWORD = 'passGeneratedByGoogleAppPasswords'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
