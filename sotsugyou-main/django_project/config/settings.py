"""
Django settings for the meeting room reservation system project.
"""
import os

# --- CORE SETTINGS ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# シークレットキーは本番環境では必ず環境変数から読み込む必要があります。
SECRET_KEY = 'django-insecure-j%&i@x^o@%q8r#j0j%p5v5!w-59&k=9@t@51h^q_p'

DEBUG = True

ALLOWED_HOSTS = ['*'] # Docker環境からのアクセスを許可

# --- APPLICATION DEFINITION ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'meeting_rooms',  # ★作成した会議室アプリを登録
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # 共通テンプレートフォルダ
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

WSGI_APPLICATION = 'config.wsgi.application'


# --- DATABASE CONFIGURATION ---
# Docker Composeで定義した環境変数からDB接続情報を取得
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}


# --- AUTHENTICATION AND VALIDATION ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'ja'  # 日本語設定

TIME_ZONE = 'Asia/Tokyo' # 日本時間設定

USE_I18N = True
USE_L10N = True
USE_TZ = True


# --- STATIC FILES (CSS, JavaScript, Images) ---
STATIC_URL = '/static/'
