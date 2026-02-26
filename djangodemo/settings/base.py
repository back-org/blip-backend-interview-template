"""Base Django settings.

This project follows a *settings module per environment* pattern:

- djangodemo.settings.development
- djangodemo.settings.production

Common settings live here (base.py) and should be safe by default.
"""

from __future__ import annotations

from pathlib import Path
from typing import List

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "unsafe-dev-secret-key"),
    TIME_ZONE=(str, "UTC"),
    LANGUAGE_CODE=(str, "fr-FR"),
    DEFAULT_FROM_EMAIL=(str, "noreply@example.com"),
    ALLOWED_HOSTS=(str, "localhost,127.0.0.1"),
    CORS_ALLOWED_ORIGINS=(str, "http://localhost:3000,http://localhost:8000"),
    DB_ENGINE=(str, "sqlite"),  # sqlite|postgres|mysql
    DB_NAME=(str, "db.sqlite3"),
    DB_USER=(str, ""),
    DB_PASS=(str, ""),
    DB_HOST=(str, "localhost"),
    DB_PORT=(str, "5432"),
    REDIS_URL=(str, "redis://localhost:6379/1"),
    JSON_LOGS=(bool, False),
    SECURITY_HEADERS_ENABLED=(bool, True),
    CSP_ENABLED=(bool, False),
    CSP_REPORT_ONLY=(bool, True),
    CSP_POLICY=(str, "default-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'"),
    REFERRER_POLICY=(str, "strict-origin-when-cross-origin"),
    PERMISSIONS_POLICY=(str, "geolocation=(), microphone=(), camera=()"),
)

# Load .env if present (never required in CI/CD)
env.read_env(BASE_DIR / ".env", overwrite=False)

SECRET_KEY: str = env("SECRET_KEY")
DEBUG: bool = env.bool("DEBUG")

def _split_csv(value: str) -> List[str]:
    return [v.strip() for v in value.split(",") if v.strip()]

ALLOWED_HOSTS: List[str] = _split_csv(env("ALLOWED_HOSTS"))

SITE_ID = 1

# ---------------------------------------------------------------------
# Applications
# ---------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "django_prometheus",
    "django_extensions",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "rest_framework_simplejwt.token_blacklist",
    "silk",
]

LOCAL_APPS = [
    "apps.billing",
    "apps.pages",
    "apps.utils",
    "apps.spectacular",
    "apps.users",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ---------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------
MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "apps.utils.middleware.RequestIdMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # static files (prod-friendly)
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "apps.utils.middleware.SecurityHeadersMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

ROOT_URLCONF = "djangodemo.urls"

# CORS (restrict in production)
CORS_ALLOWED_ORIGINS = tuple(_split_csv(env("CORS_ALLOWED_ORIGINS")))
CORS_ALLOW_CREDENTIALS = True

# ---------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = "djangodemo.wsgi.application"
ASGI_APPLICATION = "djangodemo.asgi.application"

# ---------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------
DB_ENGINE = env("DB_ENGINE").lower()

if DB_ENGINE == "postgres":
    DATABASES = {
        "default": {
            "ENGINE": "django_prometheus.db.backends.postgresql",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASS"),
            "HOST": env("DB_HOST"),
            "PORT": env("DB_PORT"),
            "CONN_MAX_AGE": 60,  # performance: keep DB connections
        }
    }
elif DB_ENGINE == "mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django_prometheus.db.backends.mysql",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASS"),
            "HOST": env("DB_HOST"),
            "PORT": env("DB_PORT"),
            "CONN_MAX_AGE": 60,
            "OPTIONS": {"charset": "utf8mb4"},
        }
    }
else:  # sqlite (default)
    DATABASES = {
        "default": {
            "ENGINE": "django_prometheus.db.backends.sqlite3",
            "NAME": BASE_DIR / env("DB_NAME"),
        }
    }

# ---------------------------------------------------------------------
# Password validation
# ---------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------------------------------------------------
# Internationalization
# ---------------------------------------------------------------------
LANGUAGE_CODE = env("LANGUAGE_CODE")
TIME_ZONE = env("TIME_ZONE")
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------------------
# Static files
# ---------------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STORAGES = {
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------------
AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    # performance: pagination prevents accidental huge responses
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
    # security: basic throttling to reduce brute-force / abuse
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ),
    "DEFAULT_THROTTLE_RATES": {"anon": "100/hour", "user": "1000/hour"},
}

# ---------------------------------------------------------------------
# JWT (SimpleJWT) hardening
# ---------------------------------------------------------------------
# - Rotates refresh tokens
# - Blacklists old refresh tokens after rotation
SIMPLE_JWT = {
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    # Keep access tokens short; tune to your needs via env if desired.
    "ACCESS_TOKEN_LIFETIME": __import__("datetime").timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": __import__("datetime").timedelta(days=7),
}

# ---------------------------------------------------------------------
# Profiling (Silk) - enable only when needed
# ---------------------------------------------------------------------
SILK_ENABLED = env.bool("SILK_ENABLED", default=False)

if SILK_ENABLED:
    MIDDLEWARE.insert(3, "silk.middleware.SilkyMiddleware")

SPECTACULAR_SETTINGS = {
    "TITLE": "DjangoDemo API",
    "DESCRIPTION": "Backend API (JWT) with content management.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# ---------------------------------------------------------------------
# Extra security headers (CSP, Permissions-Policy, Referrer-Policy)
# ---------------------------------------------------------------------
SECURITY_HEADERS_ENABLED = env.bool("SECURITY_HEADERS_ENABLED")
CSP_ENABLED = env.bool("CSP_ENABLED")
CSP_REPORT_ONLY = env.bool("CSP_REPORT_ONLY")
CSP_POLICY = env("CSP_POLICY")
REFERRER_POLICY = env("REFERRER_POLICY")
PERMISSIONS_POLICY = env("PERMISSIONS_POLICY")

# ---------------------------------------------------------------------
# Cache (optional Redis)
# ---------------------------------------------------------------------
REDIS_URL = env("REDIS_URL", default="")

if REDIS_URL:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": REDIS_URL,
            "TIMEOUT": 60,
        }
    }
else:
    # Dev-friendly fallback (no Redis required)
    CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}

# ---------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "plain": {"format": "%(asctime)s %(levelname)s %(name)s [%(request_id)s] %(message)s"},
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(name)s %(request_id)s %(message)s",
        },
    },
    "filters": {
        "request_id": {"()": "apps.utils.request_id.RequestIdFilter"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json" if env.bool("JSON_LOGS") else "plain",
            "filters": ["request_id"],
        },
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}

DEFAULT_AUTO_FIELD= "django.db.models.BigAutoField"
