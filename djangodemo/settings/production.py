"""Production settings.

Security-focused overrides. Configure values through environment variables.
"""
from .base import *  # noqa

DEBUG = False

# ---------------------------------------------------------------------
# Security (enable HTTPS-related settings behind a TLS terminator or directly)
# ---------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)

SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", default=True)
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default=True)

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 30  # 30 days (increase after validation)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
# REFERRER_POLICY is configured via env (see .env.example)

# ---------------------------------------------------------------------
# CORS / CSRF
# ---------------------------------------------------------------------
# In production, set CORS_ALLOWED_ORIGINS and ALLOWED_HOSTS via .env / env vars.

# ---------------------------------------------------------------------
# Email
# ---------------------------------------------------------------------
# Configure an email backend (SMTP / service) via env vars if needed.
