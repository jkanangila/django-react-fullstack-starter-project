import os
from pathlib import Path

from dj_database_url import config as database_config
from manage import PROJECT_NAME
from utils import get_log_folder_path

from .additional_settings import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# LOAD ENVIRONMENT VARIABLES
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = bool(os.environ.get("DEBUG", 1))
DATABASE_URL = os.environ.get("DATABASE_URL")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
LOGS_DIRECTORY = get_log_folder_path(ENVIRONMENT)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
]

# Add development only apps
if ENVIRONMENT == "dev":
    INSTALLED_APPS += [
        "django_extensions",
        "livereload",
    ]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
    ),
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Add development only middlewares
if ENVIRONMENT == "dev":
    MIDDLEWARE += [
        "livereload.middleware.LiveReloadScript",
    ]

ROOT_URLCONF = f"{PROJECT_NAME}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = f"{PROJECT_NAME}.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    "default": database_config(
        default=DATABASE_URL,
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# LOGINS

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "color": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s %(asctime)s [%(levelname)-s] %(filename)-4s %(message)s",
            "log_colors": {
                "DEBUG": "blue",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
            "style": "%",
        },
        "verbose": {
            "format": "{asctime} [{levelname}] {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "color",
        },
        "mail_admins": {
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
            "formatter": "color",
        },
        "runtime": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGS_DIRECTORY,
            "maxBytes": 15728640,  # 1024 * 1024 * 15B = 15MB
            "backupCount": 10,
            "formatter": "verbose",
        },
        "null": {
            "level": "INFO",
            "class": "logging.NullHandler",
        },
    },
    "root": {
        "handlers": ["console", "runtime"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console", "runtime"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
        "django.utils.autoreload": {
            "handlers": ["null"],
            "propagate": False,
            "level": "CRITICAL",
        },
    },
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "dist",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Generate ERD that can be visualized in graphviz
GRAPH_MODELS = {
    "all_applications": True,
    "graph_models": True,
}
