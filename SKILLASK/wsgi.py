"""
WSGI config for SKILLASK project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

application = Cling(get_wsgi_application())
