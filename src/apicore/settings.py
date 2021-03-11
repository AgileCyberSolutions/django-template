"""
Django settings for apicore project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-6s%4@1dk%awnszxk8@64n_z!!sftzle==b6-xp@9h2=j+by85'
OAUTH_CLIENTID = 'LL82l2q1pkNBRbOaxFJ0N8IKtkALzmDZcWWkn5U1'
OAUTH_CLIENT_SECRET = 'V0F7FIDXmNkyyR42FkJeITnjkspOXCCa1PufRShArPGdR2PhMSBLGYrAF01j3CURxDMeor7RzukeKU6ED8yTKHMxKS4NZBtBvZu3plC0KmErLQ77qr6PpoGWCLSGF4UU'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TO MAKE TRAILING SLASH IN URL OPTIONAL
APPEND_SLASH=False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # our custom apps
    'modules.user',
    'modules.sample',
    #oauth
    'oauth2_provider',
    'corsheaders',
    # swagger
    'drf_yasg',
    # for rest framework
    'rest_framework', 
    'rest_framework.authtoken', 
    'rest_framework_jwt',    
    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS_DEV = [
       
]

if DEBUG:
    INSTALLED_APPS.extend(INSTALLED_APPS_DEV)


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

CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'apicore.urls'

AUTH_USER_MODEL ='user.user'
REST_FRAMEWORK = { 
  'DEFAULT_PERMISSION_CLASSES': ( 
      'rest_framework.permissions.IsAuthenticated', 
  ), 
  'DEFAULT_AUTHENTICATION_CLASSES': ( 
      'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    #  'rest_framework.authentication.TokenAuthentication',
   #   'rest_framework_jwt.authentication.JSONWebTokenAuthentication', 
   #   'rest_framework.authentication.SessionAuthentication', 
   #   'rest_framework.authentication.BasicAuthentication', 
  ), 
} 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'apicore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
