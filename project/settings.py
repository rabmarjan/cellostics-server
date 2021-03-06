import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# Django settings for project.
SECRET_KEY = 'u^xf+2cz5ikm-e7x_p^5f7gwr_mq9)+-yb92dwlo=ocf_=eied'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    )
}
DEBUG = True
#TEMPLATE_DEBUG = DEBUG
#TEMPLATE_DEBUG = False

# TEMPLATES = [
#     {
#         'OPTIONS': {
#             'debug': DEBUG,
#         },
#     },
# ]
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     #'django.template.loaders.eggs.Loader',
# )
# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': 'db.sqlite3',                      # Or path to database file if using sqlite3.
        # 'USER': '',
        # 'PASSWORD': '',
        # 'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        # 'PORT': '',                      # Set to empty string for default.
    # }
# }
DATABASES = {
    'default': {
        'HOST': 'localhost',   #Host name
        'NAME': 'auth_data',     # Database name
        'ENGINE': 'django.db.backends.postgresql',  # postgres driver name
        'USER': 'postgres',
        'PASSWORD': '21198321mm',
    }
}

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

# TEMPLATE_DIRS = (
#     os.path.join(PROJECT_PATH, "templates"),
#     os.path.join(PROJECT_PATH, "static"),
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
# )

INSTALLED_APPS = (
    'django.contrib.auth',
    'corsheaders',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.admin',
    'rest_framework.authtoken',
    'rest_framework',
    'django_extensions',
  #  'push_notifications',
    'channels',
    'app',
    'dauth',
)

PUSH_NOTIFICATIONS_SETTINGS = {
"GCM_API_KEY": "<your api="" key="">",
"APNS_CERTIFICATE": "/path/to/your/certificate.pem",
}

APPEND_SLASH=False
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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
STATIC_ROOT = ''

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    
)



DEBUG_APPS = ()

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#     'localhost:8000',
#     'localhost:8080',
#     '192.168.2.174:8000',
#     'localhost:63342',
#     '192.168.2.174:8080',
#     'localhost/',
#     '192.168.2.174/',
#     '192.168.2.99',
#     '192.168.2.99:8080',
#     '192.168.5.96',
#     '192.168.5.96:8080'
#     '192.168.5.96:8000',
#     '[::]:8080',
# )

try:
    from local_settings import *
    INSTALLED_APPS += DEBUG_APPS
except ImportError:
    pass
