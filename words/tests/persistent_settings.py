from .test_settings import *  # NOQA

EXTERNAL_APPS += ['south']

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

SOUTH_MIGRATION_MODULES = {
	'taggit': 'taggit.south_migrations',
    'words': 'words.south_migrations',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}