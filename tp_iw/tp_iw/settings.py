"""
Django settings for tp_iw project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import django_heroku
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'riph3v-3a52v&fi^adc&qvh2%)1o0e5l=mp2(i4iq5-^f#0y&q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# Application definition
# Application definition
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # nuestras apps
    'usuario',
    'escritos',
    'home',
    'ckeditor',
    'libros',
    'comentarios',

    #ERD
    'django_extensions',

    #HAYSTACK
    'haystack',

    #ROBOTS
    'robots',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tp_iw.urls'

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
                'django.template.context_processors.request',
                #'django.template.loaders.app_directories.Loader',
                'home.context_processors.agregar_usuarios_no_seguidos',  
            ],
        },
    },
]

WSGI_APPLICATION = 'tp_iw.wsgi.application'

GRAPH_MODELS = {
    'all-applications': True,
    'group_models': True,
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '50vw',
        'toolbar': 'Custom',
        'resize_enabled' : 'true',
        'resize_dir' : 'both',

        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    },
}

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if not os.environ.get("EN_DOCKER", False): #Si NO se encuentra en Docker
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
else: #Si se encuentra en Docker
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, '..', '..', 'data','db.sqlite3'),
        }
    }
    print(os.path.join(BASE_DIR, '..', '..', 'data','db.sqlite3'))
    MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'data','media')
    MEDIA_URL = '/data/media/'

'''
if os.environ.get("IS_DOCKER", False): 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, '..','data','db.sqlite3'),
        }
    }
    MEDIA_URL = '/data/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, '..','data','media')
else: #Si NO se encuentra en Docker
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
'''

'''
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'Tp_IW_Leelo',
            'PASSWORD': 'abc2234',
            'USER': 'postgres',
            'HOST': '127.0.0.1',
            'DATABASE_PORT': '5432',
        }
}
'''
if os.environ.get('SEARCHBOX_URL'):
    # estoy corriendo en heroku
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': os.environ.get('SEARCHBOX_URL'),
            'INDEX_NAME': 'documents',
        },
    }
else:
    # estoy corriendo en mi maquina (o en heroku y me olvide de agregar
    # el addon de searchbox)
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        },
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

#Django allouth settings
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',    
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#Static files (CSS, JavaScript, Images)
#https://docs.djangoproject.com/en/3.1/howto/static-files/


#para cargar imagenes y statics

STATIC_URL = '/static/'
#MEDIA_URL = '/media/'

#MEDIA_ROOT = os.path.join(BASE_DIR,'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

LOGIN_REDIRECT_URL = '/home/homepage' # Controla el redirect luego de iniciar sesion con Google

# CONFIGURACION DEL SMTP DE GOOGLE
EMAIL_USE_TLS = True
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'leeloingweb@gmail.com'
EMAIL_HOST_PASSWORD = 'starfleet31'
EMAIL_PORT = 587

# Activate Django-Heroku.
django_heroku.settings(locals())


