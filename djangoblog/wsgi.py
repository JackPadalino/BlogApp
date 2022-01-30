"""
WSGI config for djangoblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os # standard with Django

from django.core.wsgi import get_wsgi_application # standard with Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoblog.settings') # standard with Django

application = get_wsgi_application() # standard with Django
