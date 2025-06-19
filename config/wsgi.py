"""
Конфигурация WSGI для проекта конфигурации.

Он предоставляет вызываемый WSGI как переменную уровня модуля с именем ``application``.

Более подробную информацию об этом файле см.
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
