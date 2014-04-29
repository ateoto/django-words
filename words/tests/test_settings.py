"""
Settings for tests
"""
import os

from unipath import Path

APP_ROOT = Path(__file__).parent

SECRET_KEY = 'NotALegitSecretKey'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'crispy_forms',
    'ckeditor',
    'taggit',
    'django_summernote',
]

INTERNAL_APPS = [
    'words',
    'words.tests.test_app',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

CRISPY_TEMPLATE_PACK = 'bootstrap3'

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'

SUMMERNOTE_CONFIG = {
    'iframe': False,
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'words.tests.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(APP_ROOT.parent, 'static'),
)

STATIC_ROOT = os.path.join(APP_ROOT.parent, 'app_static')
MEDIA_ROOT = os.path.join(APP_ROOT.parent, 'app_media')

TEMPLATE_DIRS = (
    Path(APP_ROOT + 'templates'),
)