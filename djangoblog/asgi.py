"""
ASGI config for djangoblog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os # this import standard with django

from django.core.asgi import get_asgi_application # this import standard with django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoblog.settings')  # standard with Django

application = get_asgi_application()  # standard with Django
