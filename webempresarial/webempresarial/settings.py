
import os
import json



from pathlib import Path
from django.core.exceptions import ImproperlyConfigured




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-=b+_2j5i!qgytzz&-p=qz$g9y$^3eie83iiaxy+!@_ef4@71&p'


with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))


SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_secret('DEBUG')

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'contact',
    'ckeditor',
    'servicios',
    'blog',
    'social',
    'pages.apps.PagesConfig',
    
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

ROOT_URLCONF = 'webempresarial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.processors.contexto',
                'core.processors.navegacion',
            ],
        },
    },
]

WSGI_APPLICATION = 'webempresarial.wsgi.application'


#Database
#https://docs.djangoproject.com/en/4.0/ref/settings/#databases




DATABASES = {
    'default':{
        'ENGINE':get_secret( 'ENGINE'),
        'NAME':get_secret('NAME'),
        'USER':get_secret('USER'),
        'PASSWORD':get_secret('PASSWORD'),
        'HOST':get_secret('HOST'),
        'PORT':get_secret('PORT')
        
    }
}
"""


DATABASES = {
    'default': {
        'ENGINE': get_secret('NAME'),
        'NAME': BASE_DIR / 'db.sqlite3',
        
    }
}
"""



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')


# Ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}


# Default primary key field type
# https://doc.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#configuracion de email



"""
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST =  "smtp.gmail.com"
EMAIL_HOST_PASSWORD = "Mosan#12345"
EMAIL_HOST_USER = "molinaconstruction2021@gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
"""


EMAIL_SETTINGS_FILE = os.path.join(BASE_DIR, 'email_settings.json')

with open(EMAIL_SETTINGS_FILE) as data_file:
    email_settings = json.load(data_file)


EMAIL_BAKEND= email_settings['EMAIL_BAKEND']
EMAIL_HOST=email_settings['EMAIL_HOST']
EMAIL_USE_TLS=email_settings['EMAIL_USE_TLS']
EMAIL_PORT=email_settings['EMAIL_PORT']
EMAIL_HOST_USER=email_settings['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD=email_settings['EMAIL_HOST_PASSWORD']

