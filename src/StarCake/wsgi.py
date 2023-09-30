"""
WSGI config for StarCake project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StarCake.settings')

application = get_wsgi_application()
application = WhiteNoise(application)
