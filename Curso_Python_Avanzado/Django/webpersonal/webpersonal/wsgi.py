"""
WSGI config for webpersonal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
#Importa el módulo os, que se utiliza para interactuar con el sistema operativo. En este caso, se usa para acceder y configurar variables de entorno
import os

#Importa la función get_wsgi_application del módulo django.core.wsgi. 
#Esta función es la que genera la aplicación WSGI principal de Django, 
#capaz de manejar las solicitudes HTTP y enrutar el tráfico a nuestras vistas y URLs.
from django.core.wsgi import get_wsgi_application

#Esta línea es idéntica a las que se vio en manage.py y asgi.py, y cumple la misma función crucial:
    #Le indica a Django dónde encontrar el archivo de configuración principal de tu proyecto (settings.py).
    #setdefault() asegura que esta variable de entorno se establezca solo si aún no ha sido definida.
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webpersonal.settings')

#Esta es la línea más importante.
#Llama a la función get_wsgi_application(), que inicializa y devuelve la aplicación WSGI de Django.
application = get_wsgi_application()
#El resultado de esta llamada se asigna a la variable application. 
#Esta variable es el "callable" WSGI que el servidor de despliegue (por ejemplo, Gunicorn, uWSGI)
#buscará y ejecutará para manejar las solicitudes entrantes dirigidas a la aplicación Django. 
#Es el punto de entrada para que el servidor web se comunique con nuestra aplicación.



"""
    El archivo wsgi.py es fundamental para el despliegue de la aplicación Django en un entorno de producción que utiliza un servidor WSGI. 
    Sirve como el puente que permite que el servidor web pase las solicitudes a la aplicación Django
    para que las procese y, a su vez, reciba las respuestas de vuelta para enviarlas al cliente.

    Qué es WSGI y para qué sirve?
    
        WSGI es el estándar de interfaz entre los servidores web (como Apache con mod_wsgi o Nginx con Gunicorn/uWSGI) y las aplicaciones web escritas en Python. Permite que un servidor web "hable" con la aplicación Django de una manera estandarizada.

        En términos sencillos: cuando un servidor web recibe una solicitud HTTP para el sitio Django, no sabe directamente cómo ejecutar nuestro código Python. wsgi.py es el "traductor" o "adaptador" que le dice al servidor web cómo interactuar con la aplicación Django para procesar esa solicitud.

        Aunque Django ahora también soporta ASGI para funcionalidades asíncronas (como WebSockets), WSGI sigue siendo la interfaz más común y adecuada para la mayoría de las aplicaciones web Django tradicionales que manejan solicitudes HTTP/HTTPS de forma síncrona.

"""
