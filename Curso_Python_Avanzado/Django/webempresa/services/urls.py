"""
Configuración de URLs para la aplicación services.

Define la ruta principal para visualizar los servicios ofrecidos.
"""

# Importamos la función `path` desde `django.urls`.
# Esta función nos permite definir las rutas URL de esta aplicación.
from django.urls import path

# Importamos el módulo `views` desde el directorio actual (indicado por el punto `.`).
# Este módulo contiene las funciones o clases que manejan las solicitudes HTTP para cada ruta.
from . import views

# Definimos la lista `urlpatterns`, que contiene todas las rutas URL de esta aplicación.
urlpatterns = [

    #Paths del core
     # Ruta para la página de servicios.
    # - La cadena vacía ('') indica que esta es la ruta raíz de la aplicación `services`.
    # - `views.services` es la vista que se ejecutará cuando se acceda a esta ruta.
    # - El parámetro `name="services"` asigna un nombre a esta ruta para referenciarla en otras partes del código.
    path('',views.services, name="services"),
]
   