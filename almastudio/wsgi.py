"""
WSGI config for almastudio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'almastudio.settings')

application = get_wsgi_application()

"""
#for apache
import os
import sys
sys.path.append('/opt/bitnami/apps/django/django_projects/almastudio')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/almastudio/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "almastudio.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""