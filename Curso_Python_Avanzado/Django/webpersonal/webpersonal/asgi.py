"""
ASGI config for webpersonal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
""" El archivo asgi.py es el punto de entrada para nuestra aplicación Django cuando se despliega
 usando un servidor compatible con ASGI (Asynchronous Server Gateway Interface) """

import os

# Importa la función get_asgi_application del módulo django.core.asgi. 
# Esta función es la que genera la aplicación ASGI principal de Django, 
# que es capaz de manejar las solicitudes HTTP y enrutar el tráfico a las vistas y URLs.
from django.core.asgi import get_asgi_application

#Esta línea es idéntica a la que se vio en manage.py y cumple la misma función crucial: Le dice a Django 
#dónde encontrar el archivo de configuración principal del proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webpersonal.settings')

""" Esta es la línea más importante. """
#Llama a la función get_asgi_application(), que inicializa y devuelve la aplicación ASGI de Django.
application = get_asgi_application()

#El resultado de esta llamada se asigna a la variable application. Esta variable es el "callable" ASGI 
#que el servidor de despliegue (por ejemplo, Gunicorn con Uvicorn worker, o Daphne) buscará y ejecutará 
# para manejar las solicitudes entrantes dirigidas a la aplicación Django.

"""

El archivo asgi.py actúa como un puente entre un servidor web que entiende ASGI y la aplicación Django. 
Cuando un servidor ASGI recibe una solicitud (por ejemplo, una petición HTTP o una conexión WebSocket), 
llama al objeto application definido en este archivo. Este objeto, a su vez, se encarga de dirigir la solicitud 
a la parte correspondiente del proyecto Django (tus URLs, vistas, etc.) para su procesamiento.

Aunque para un proyecto pequeño o si no utilizmos características asíncronas explícitamente, wsgi.py sería suficiente, 
asgi.py nos prepara para el futuro y para escenarios de despliegue más avanzados o con requisitos de tiempo real.

"""