"""
Django settings for uraz project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '82_w8$t2w(6uiy==l#(f_ht_iynvj(o#p#pyt&4-q$%lpi8ue)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ="smtp.yandex.com"
EMAIL_HOST_USER ="webservice@centralwebagency.com"
EMAIL_HOST_PASSWORD = "jango4848"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cart',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'user',
    'yoga',
    'shop',
    'orders',
    'pwa',

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

ROOT_URLCONF = 'uraz.urls'

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

WSGI_APPLICATION = 'uraz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
 ]

STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")


MEDIA_URL = '/media/'
MEDIA_ROOT =os.path.join(BASE_DIR,'media')


SITE_ID = 1

####################################
    ##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CART_SESSION_ID = 'cart'




DEFAULT_AUTO_FIELD='django.db.models.AutoField'


#PWA_APP_NAME = 'Defectıve Sound'
#PWA_APP_DESCRIPTION = "Void Ses Sistemleri"
#PWA_APP_THEME_COLOR = '#C20D1D'
#PWA_APP_BACKGROUND_COLOR = '#ffffff'
#PWA_APP_DISPLAY = 'standalone'
#PWA_APP_SCOPE = 'http://127.0.0.1:8000/'
#PWA_APP_ORIENTATION = 'any'
#PWA_APP_START_URL = 'http://127.0.0.1:8000/'
#PWA_APP_STATUS_BAR_COLOR = 'default'
#PWA_APP_ICONS = [
#    {
#        'src': '/static/pwa/img/fav.png',
#        'sizes': '160x160'
#    },
#    {
#        'src': '/static/pwa/img/512.png',
#        'sizes': '512x512'
#    },
#]
#PWA_APP_ICONS_APPLE = [
#    {
#        'src': '/static/pwa/img/fav.png',
#        'sizes': '160x160'
#    },
#    {
#        'src': '/static/pwa/img/512.png',
#        'sizes': '512x512'
#    },
#]
#PWA_APP_SPLASH_SCREEN = [
#    {
#        'src': '/static/pwa/img/fav.png',
#        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
#    }
#]
#PWA_APP_DIR = 'ltr'
#PWA_APP_LANG = 'en-US'

#PWA_SERVICE_WORKER_PATH = 'static/pwa/js/sw.js'

