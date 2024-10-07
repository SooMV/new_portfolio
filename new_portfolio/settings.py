"""
Django settings for new_portfolio project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import environ
from pathlib import Path
import os

env = environ.Env()

from django.contrib.messages import constants as messages


AUTH_USER_MODEL = 'Accounts.Customer'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR/".env")



env = environ.Env(
    DEBUG=(bool, False)
)


# Utiliser les variables d'environnement
DEBUG = env('DEBUG')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1','votre-futur-alternant.onrender.com', 'votre-futur-alternant.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    "django.contrib.sites",
    "django.contrib.redirects",
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_recaptcha',
    'new_portfolio',
    "Main",
    "Mail",
    'Accounts',
    'tailwind',
    'theme',
    'django_browser_reload',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'new_portfolio.urls'

TEMPLATES = [
    {
       "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "theme" / "templates"],
        "APP_DIRS": True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'theme.context_processors.change_theme'
            ],
        },
    },
]

WSGI_APPLICATION = 'new_portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# langue par défaut
LANGUAGE_CODE = "en-us"

# langues disponibles
LANGUAGES = [
    ('en', 'English'),
    ('fr', 'French'),
]

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True


EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL pour accéder aux fichiers statiques
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Répertoire où collectstatic va copier les fichiers
STATICFILES_DIRS = [BASE_DIR / 'static']  # Dossier de fichiers statiques supplémentaires

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

RECAPTCHA_USE_SSL = True
RECAPTCHA_VERIFY_REQUEST_TIMEOUT = 10  # Délai d'expiration pour la vérification


SECRET_KEY = env('SECRET_KEY')
RECAPTCHA_PUBLIC_KEY=env("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY=env("RECAPTCHA_PRIVATE_KEY")
EMAIL_HOST_USER=env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=env("EMAIL_HOST_PASSWORD")



MESSAGE_TAGS = {
    messages.DEBUG: 'bg-blue-100 border border-blue-400 text-blue-700',
    messages.INFO: 'bg-blue-100 border border-blue-400 text-blue-700',
    messages.SUCCESS: 'bg-green-100 border border-green-400 text-green-700',
    messages.WARNING: 'bg-yellow-100 border border-yellow-400 text-yellow-700',
    messages.ERROR: 'bg-red-100 border border-red-400 text-red-700',
}

RECAPTCHA_ERROR_MSG = {
    'required': 'Veuillez compléter le reCAPTCHA pour continuer.',
    'invalid': 'Le reCAPTCHA est invalide. Veuillez réessayer.',
    'timeout': 'Le reCAPTCHA a expiré. Veuillez rafraîchir la page et réessayer.',
    'connection_error': 'Une erreur de connexion s\'est produite. Veuillez vérifier votre connexion Internet et réessayer.'
}
