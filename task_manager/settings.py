# settings.py

import os
from pathlib import Path

# BASE_DIR değişkenini tanımlayın
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-8$n#2j&=$b_!7v-1n8q_!^@ur4lb1!x$olp1_#a)sm$v#2^q4s'

INSTALLED_APPS = [
    # Django'nun varsayılan uygulamaları
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Yeni uygulamanız
    'tasks',
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

ROOT_URLCONF = 'task_manager.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'task_manager.wsgi.application'

# Veritabanı ayarları (örnek için varsayılan sqlite3 kullanılıyor)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Uluslararasılaştırma
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Statik dosyalar (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Varsayılan birincil anahtar alanı tipi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Debug ve Allowed Hosts ayarları
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

LOGIN_URL = 'login'