"""Development settings.

Safe defaults for local development.
"""
from .base import *  # noqa

DEBUG = True

# In dev we often allow localhost + docker hostnames
ALLOWED_HOSTS = list(set(ALLOWED_HOSTS + ["0.0.0.0"]))  # noqa
