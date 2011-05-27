# Django settings for supervise project.

__author__ = "Oscar Carballal Prego"
__copyright__ = "Copyright 2011 Oscar Carballal Prego"
__credits__ = ["Oscar Carballal"]
__license__ = "BSD"
__version__ = "0.1"
__maintainer__ = "Oscar Carballal Prego"
__email__ = "oscarcp@clionesoftware.com"
__status__ = "Alpha"

# Get the current directory
import os
cwd = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db/database.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'es-ES'
LANGUAGES = (
    ('es', 'Espanol'),
    ('en', 'English'),
    ('gl', 'Galego'),
)

SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = cwd + '/uploads/'
MEDIA_URL = '/uploads'
STATIC_ROOT = cwd + '/static/'
STATIC_URL = '/static'

# Check this, this value is the default for new projects, we will replace it
# for an old value from django 1.2
#ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_MEDIA_PREFIX = '/media/'

# Additional locations of static files
#STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'z^w6b2%qw_z=f4^)x&96qw(#erx5+58o=w47c_wjlgz6vs9_-@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "supervise.apps.userprofile.context_processors.css_classes",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'supervise.urls'

TEMPLATE_DIRS = (
    cwd + '/templates',
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRDPARTY_APPS = (
    'supervise.apps.userprofile',
)

SUPERVISE_APPS = (
    'supervise.apps.profiles',
    #'supervise.apps.issues',
    #'supervise.apps.projects',
    #'supervise.apps.news',
    #'supervise.apps.wiki',
)

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + SUPERVISE_APPS

# django-profile settings
# E-Mail settings
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
REQUIRE_EMAIL_CONFIRMATION = True

# Google Maps. Change this API key. This one is registered to 127.0.0.1:8000
GOOGLE_MAPS_API_KEY = 'ABQIAAAA06IJoYHDPFMx4u3hTtaghxTpH3CbXHjuCVmaTc5MkkU4wO1RRhST5bKY_U7dUG1ZGu1S-n-ukXGNjQ'

# Avatar settings
DEFAULT_AVATAR = os.path.join(STATIC_ROOT, 'userprofile/generic.jpg')
AVATAR_WEBSEARCH = False
AVATAR_QUOTA = 8

# Profile settings
AUTH_PROFILE_MODULE = "profiles.UserProfile"
LOGIN_URL = '/user/login'
LOGIN_REDIRECT_URL = '/user'
USERPROFILE_CSS_CLASSES = 'blueprint'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
