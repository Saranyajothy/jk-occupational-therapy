"""
Django settings for occupationaltherapy project.
Generated by 'django-admin startproject' using Django 4.1.1.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from pathlib import Path
import dj_database_url
import cloudinary
import os 
if os.path.exists('env.py'):
    import env
    

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['jkot.herokuapp.com', 'localhost', '127.0.01']

CSRF_TRUSTED_ORIGINS = [
    'https://8000-saranyajoth-jkoccupatio-2tcsptbr8m6.ws-eu70.gitpod.io',
    'https://jkot.herokuapp.com', 'http://jkot.herokuapp.com'
]



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
    'adminMod',
    'bootstrap4',
    'crispy_forms',
    'phonenumber_field'
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

ROOT_URLCONF = 'occupationaltherapy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'occupationaltherapy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#   'default': {
#      'ENGINE': 'django.db.backends.sqlite3',
#      'NAME': BASE_DIR / 'db.sqlite3',
# }
# }

DATABASES = {
   'default': dj_database_url.parse('postgres://ugfksseirdyoyy:fdbf2b002e5e4b6778c018105beee75569b55b40f3928974dcf00e70ad4982ec@ec2-34-241-90-235.eu-west-1.compute.amazonaws.com:5432/db2hl8c0c20vaa')
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Default settings
BOOTSTRAP3 = {

    # The complete URL to the Bootstrap CSS file
    # Note that a URL can be either
    # - a string, e.g. "//code.jquery.com/jquery.min.js"
    # - a dict like the default value below (use key "url" for the actual link)
    "css_url": {
        "url": "https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css",
        "integrity": "sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap CSS file (None means no theme)
    "theme_url": None,

    # The complete URL to the Bootstrap JavaScript file
    "javascript_url": {
        "url": "https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js",
        "integrity": "sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd",
        "crossorigin": "anonymous",
    },

    # The URL to the jQuery JavaScript file
    "jquery_url": "//code.jquery.com/jquery.min.js",

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    "javascript_in_head": False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    "include_jquery": True,

    # Label class to use in horizontal forms
    "horizontal_label_class": "col-md-3",

    # Field class to use in horizontal forms
    "horizontal_field_class": "col-md-9",

    # Set placeholder attributes to label if no placeholder is provided.
    # This also considers the "label" option of {% bootstrap_field %} tags.
    "set_placeholder": True,

    # Class to indicate required (better to set this in your Django form)
    "required_css_class": "",

    # Class to indicate error (better to set this in your Django form)
    "error_css_class": "has-error",

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    "success_css_class": "has-success",

    # Renderers (only set these if you have studied the source and understand the inner workings)
    "formset_renderers":{
        "default": "bootstrap3.renderers.FormsetRenderer",
    },
    "form_renderers": {
        "default": "bootstrap3.renderers.FormRenderer",
    },
    "field_renderers": {
        "default": "bootstrap3.renderers.FieldRenderer",
        "inline": "bootstrap3.renderers.InlineFieldRenderer",
    },
}