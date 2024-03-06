<<<<<<< HEAD
"""
WSGI config for books project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")

application = get_wsgi_application()
=======
"""
WSGI config for books project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")

application = get_wsgi_application()
>>>>>>> 1d221d9c65af698a7761a514f421d3a52566b2c1
