"""
ASGI config for webempresa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/

Expone la aplicación ASGI como una variable a nivel de módulo llamada `application`.
Este archivo es usado por servidores ASGI como Daphne o Hypercorn para manejar
peticiones asíncronas (WebSockets, HTTP/2, etc.) en entornos de producción.
"""

import os # Para manejo de variables de entorno y rutas del sistema

from django.core.asgi import get_asgi_application # Obtiene la aplicación ASGI de Django

# Configura el módulo de settings por defecto para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webempresa.settings')

# Crea la aplicación ASGI (punto de entrada para el servidor)
application = get_asgi_application()
