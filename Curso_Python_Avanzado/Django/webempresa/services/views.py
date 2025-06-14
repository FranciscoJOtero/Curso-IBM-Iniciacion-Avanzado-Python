''' 
Vistas para la aplicación services.

Muestra el listado completo de servicios ofrecidos por la empresa.
'''
# Importamos la función `render` desde `django.shortcuts`.
# Esta función nos permite renderizar plantillas HTML y devolver una respuesta HTTP.
from django.shortcuts import render

# Importamos el modelo `Service` desde la aplicación `services`.
# Este modelo representa los servicios que se mostrarán en el sitio.
from .models import Service

# Definimos la vista `services`, que maneja las solicitudes a la página de servicios.
def services(request):

    # Obtenemos todos los objetos del modelo `Service` usando `Service.objects.all()`.
    # Esto devuelve un queryset con todos los servicios disponibles en la base de datos.
    services = Service.objects.all()

    # Renderizamos la plantilla `services/services.html` y pasamos los servicios como contexto.
    # El contexto es un diccionario que contiene los datos que estarán disponibles en la plantilla.
    return render(request, "services/services.html", {'services':services})