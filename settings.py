# -*- coding: utf-8 -*-
# Django settings for immotrade project.

#from django.contrib.sites.models import Site
#Site.objects.get_current().domain

import os
import sys

# Get project full path
PROJECT_DIR  = os.path.dirname(__file__)

sys.path.append(PROJECT_DIR)
sys.path.append(PROJECT_DIR + '/apps')
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('firstrow', 'firstrow22@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'admin_immotrade',
        'USER': 'admin_immotrade',
        'PASSWORD': 'asdf768d423',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': { 'init_command': 'SET storage_engine=MYISAM;' }
    }
}

INTERNAL_IPS = ('127.0.0.1',) # For debug toolbar

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Kiev'

PATH_TO_UPLOADS = "/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/media/"
TEMP_PATH = "/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/temp/"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', 'Русский'),
    ('en', 'English'),
    ('de', 'German'),
)

# Current site ID
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
# Use ending slash
MEDIA_ROOT = PROJECT_DIR + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media' # NO ENDING SLASH

# URL prefix for admin media -- CSS, JavaScript and photos. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Sessions
SESSION_ENGINE = "django.contrib.sessions.backends.db"

# Messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tz+gyh=7bi+_(c6u(@o%+9f(4r=2^^2x*#u6npx45dr3=1d*7b'

# How many objects display in lists
OBJECTS_PER_PAGE = 15

# Auth
LOGIN_URL = '/user/login/'
LOGIN_REDIRECT_URL = '/estates/list/'

# Image upload configs
MAX_IMAGE_WIDTH = 800
MAX_IMAGE_HEIGHT = 600
UPLOAD_IMAGE_QUALITY = 95

# Cache backend
CACHE_BACKEND = 'locmem://'

# Mail config
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_FILE_PATH = PROJECT_DIR + '/tmp_mails/'
# Email where messages from contacts page will be sent
CONTACTS_EMAIL = 'robot@worldimmotrade.ru'
ROBOT_EMAIL = 'robot@worldimmotrade.ru'

EMAIL_HOST_USER = "robot@worldimmotrade.ru"
EMAIL_HOST_PASSWORD = "123123123"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'immotrade.memoryMiddleware.memoryMiddleware',
    'immotrade.LocaleMiddleware.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "context_processors.user_profile",
    "context_processors.countries",
    "context_processors.search_form",
    "context_processors.load_banners",
    "context_processors.currencies",
    "context_processors.active_lang",
    "context_processors.total_objects",
    "context_processors.total_objects_in_cart",
    "context_processors.current_language",
    "django_messages.context_processors.inbox",
)

ROOT_URLCONF = 'immotrade.urls'

TEMPLATE_DIRS = (
    PROJECT_DIR + '/templates',
)

TRANSLATION_REGISTRY = "estates.translation"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'grappelli',
    'django.contrib.admin',
    'south',
    'django_messages',
    #'debug_toolbar',
    'modeltranslation',
    'estates',
    'world',
    'users',
    'pages',
    'banners',
    'tarifs',
    'pagination',
#    'rosetta',
)
