from . import settings
from pathlib import Path
#from dotenv import read_dotenv # type: ignore
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

RESEND=os.getenv('RESEND')
DEBUG=os.getenv('DEBUG')
ALLOWED_HOSTS = ['*']
#CSRF_TRUSTED_ORIGINS = ['https://polls.applikasi.tech']


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_DEV_NAME'),
        'USER': os.getenv('DB_DEV_USER'),
        'PASSWORD': os.getenv('DB_DEV_PASSWORD'),
        'HOST': os.getenv('DB_DEV_HOST'),
        'PORT': os.getenv('DB_DEV_PORT'),
    }
}

SECRET_KEY=os.getenv('SECRET_KEY')
