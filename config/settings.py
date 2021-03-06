"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import pymysql  # !!!

pymysql.version_info = (1, 3, 13, "final", 0)  # !!!
pymysql.install_as_MySQLdb()  # !!!

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm1weo#)ba7$pb)t1d^#$lhln!#0e$w4!0jgt2t%xruqz4_&r$o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["taeyeonshop.pythonanywhere.com", "127.0.0.1", "localhost"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'shop',
    'django.contrib.sites',  # allauth 사이트 활용을 위해서
    'allauth',  # allauth 앱
    'allauth.account',  # 계정관리
    'allauth.socialaccount',  # 소셜 계정 관리
    'allauth.socialaccount.providers.naver',  # 네이버 계정 연동
    'cart',
    'coupon',
    'order',
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

ROOT_URLCONF = 'config.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onlineshop',
        'USER': 'root',
        'PASSWORD': 'Taen47nyyyy!',  # !!! 자신의 비밀번호로 변경
        'HOST': 'localhost',  # 'onlineshop.csfyvlroglcs.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO'",
        },
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'taeyeonshop$default',
#         'USER': 'taeyeonshop',
#         'PASSWORD': 'mysql1111',  # !!! 자신의 비밀번호로 변경
#         'HOST': 'taeyeonshop.mysql.pythonanywhere-services.com',
#         'OPTIONS': {
#             'init_command':
#             "SET sql_mode='STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO'",
#         },
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko'  # 관리자 페이지의 언어를 한글로 설정

TIME_ZONE = 'Asia/Seoul'  # 시간 대역을 서울로 설정

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 이걸 False로 설정해야 Model 시간 대역도 서울로 적용됨

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 파일 맨 끝에 추가
# 장고 인증은 사용자 이름을 쓰지만, allauth 인증은 이메일을 사용
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # 장고 방식 인증
    'allauth.account.auth_backends.AuthenticationBackend',  # allauth 인증
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

CART_ID = 'cart_in_session'

IAMPORT_KEY = '4715917310574070'
IAMPORT_SECRET = '8Mpz938zLj8GqV0AYxmsD4tSBcxyXTA5F0EP4NpP7xvxtw8r4vTHAnzbz7Kw0kBFlgup4UebrKJUgSlk'
