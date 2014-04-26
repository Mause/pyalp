from os.path import abspath, dirname, join
from configurations import Configuration

PROJECT_ROOT = dirname(dirname(abspath(__file__)))
PROJECT_NAME = 'pyalp'


class InvalidVarException(object):
    def __mod__(self, missing):
        try:
            missing_str = str(missing)
        except:
            missing_str = 'failed to create string representation'

        raise Exception('Unknown template variable %r %s' % (
            missing, missing_str
        ))

    def __contains__(self, search):
        if search == '%s':
            return True
        return False

    def __str__(self):
        return ''


class RedisCache(object):
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '127.0.0.1:6379',
            'OPTIONS': {
                'DB': 1,
                'PARSER_CLASS': 'redis.connection.HiredisParser'
            },
        },
    }


class Common(Configuration):
    ADMINS = (
        ('Dominic May', 'me@mause.me'),
    )

    MANAGERS = ADMINS

    SITE_ID = 'pyalp'

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'randomstring'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    TEMPLATE_DEBUG = True
    TEMPLATE_STRING_IF_INVALID = InvalidVarException()
    TEMPLATE_LOADERS = [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'skins.skin_template_loader.Loader'
    ]
    TEMPLATE_CONTEXT_PROCESSORS = [
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",

        "pyalp.contexts.app_name",
        "pyalp.contexts.url_name",
        "pyalp.contexts.skin",
        "pyalp.contexts.modules",
        "pyalp.contexts.lan"
    ]
    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.admindocs',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_jenkins',
        'django_extensions',
        # 'raven.contrib.django.raven_compat',
        # 'debug_toolbar',
        'floppyforms',
        'south',
        'chosen',
        'jsonify',
        'pipeline',

        # pyalp plugins
        'pyalp_translation',
        'custom_template_tags',
        'pyalp_page',
        'listjs',

        # pyalp apps
        'common',
        'pizza',
        'flags',
        'skins',
        'cl_module',
        'tournaments'
    ]

    MIDDLEWARE_CLASSES = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # 'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    ROOT_URLCONF = 'pyalp.urls'

    WSGI_APPLICATION = 'pyalp.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en//ref/settings/#databases
    # http://django-configurations.readthedocs.org/en/latest/values/
    # #configurations.values.DatabaseURLValue

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'dev.sqlite',
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en//topics/i18n/

    LANGUAGE_CODE = 'en-GB'

    TIME_ZONE = 'Australia/Perth'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en//howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = join(PROJECT_ROOT, 'static_root')
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
        "skins.skin_staticfile_finder.SkinStaticFileFinder"
        # "skins.skin_cssfile_finder.SkinCSSFileFinder"
    )
    PIPELINE_COMPILERS = 'skins.skin_cssfile_compiler.SkinCSSFileCompiler'
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = join(PROJECT_ROOT, 'media')

    # Additional locations of static files
    STATICFILES_DIRS = [
        join(PROJECT_ROOT, 'static')
    ]

    TEMPLATE_DIRS = [
        join(PROJECT_ROOT, 'templates'),
    ]
    SKIN_DIR = join(PROJECT_ROOT, 'skins', 'skins')

    FIXTURE_DIRS = [
        join(PROJECT_ROOT, 'fixtures')
    ]

    # App settings

    # django-jenkins
    PROJECT_APPS = [app for app in INSTALLED_APPS if app.startswith('pyalp.')]
    JENKINS_TASKS = ('django_jenkins.tasks.run_pylint',
                     'django_jenkins.tasks.django_tests',
                     'django_jenkins.tasks.run_pep8',
                     'django_jenkins.tasks.with_coverage')

    # django-debug-toolbar
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
    INTERNAL_IPS = ('127.0.0.1', 'warbell', '10.0.0.4', '::2')

    ALP_TOURNAMENT_MODE = False
    ALP_TOURNAMENT_MODE_COMPUTER_GAMES = False


class Dev(Common):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = '/tmp/app-emails'


class DevPostgres(Dev):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'pyalp_db',
            'USER': 'pyalp',
            'PASSWORD': 'pass',
            'HOST': 'localhost',
            'OPTIONS': {
                'autocommit': True
            }
        }
    }


class Deployed(RedisCache, Common):
    """
    Settings which are for a non local deployment, served behind nginx.
    """
    PUBLIC_ROOT = join(PROJECT_ROOT, '../public/')
    STATIC_ROOT = join(PUBLIC_ROOT, 'static')
    MEDIA_ROOT = join(PUBLIC_ROOT, 'media')
    COMPRESS_OUTPUT_DIR = ''

    # SESSION_ENGINE = 'redis_sessions.session'

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    DEFAULT_FROM_EMAIL = ''
    SERVER_EMAIL = ''


class Stage(Deployed):
    # see https://docs.djangoproject.com/en/dev/ref/databases/#autocommit-mode
    # about autocommit

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'OPTIONS': {
                'autocommit': True
            }
        }
    }


class Prod(Deployed):
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    # see https://docs.djangoproject.com/en/dev/ref/databases/#autocommit-mode
    # about autocommit

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'OPTIONS': {
                'autocommit': True
            }
        }
    }

    ALLOWED_HOSTS = ['http://mause.me', ]  # add deployment domain here

    RAVEN_CONFIG = {
        'dsn': ''
    }
