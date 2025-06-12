"""
WSGI config for webempresa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/

Configuración WSGI (Web Server Gateway Interface) para webempresa.

Este archivo define la interfaz entre el servidor web (como Apache o Nginx) y tu aplicación Django.
Es el punto de entrada para despliegues en producción con servidores tradicionales (HTTP/1.1).

"""

import os

from django.core.wsgi import get_wsgi_application # Importa la aplicación WSGI de Django

# Establece el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webempresa.settings')

# Crea la aplicación WSGI (la variable 'application' es estándar para servidores)
application = get_wsgi_application()
