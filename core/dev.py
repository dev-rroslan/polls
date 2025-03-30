from . import base
from pathlib import Path
from dotenv import read_dotenv # type: ignore
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

os.getenv('RESEND')
DEBUG = False
ALLOWED_HOSTS = ['polls.applikasi.tech', '165.154.203.185', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://polls.applikasi.tech']


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}