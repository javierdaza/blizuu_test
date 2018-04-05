"""
WSGI config for proyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

# This allows easy placement of apps within the interior
# proyecto directory.
app_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(os.path.join(app_path, 'proyecto'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
