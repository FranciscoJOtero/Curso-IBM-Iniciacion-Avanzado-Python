# Importamos la función `path` desde el módulo `django.urls`.
# Esta función nos permite definir las rutas URL de nuestra aplicación.
from django.urls import path

# Importamos el módulo `views` desde el directorio actual (indicado por el punto `.`).
# Este módulo contiene las funciones o clases que manejan las solicitudes HTTP para cada ruta.
from . import views

# Definimos la lista `urlpatterns`, que es obligatoria en un archivo `urls.py`.
# Esta lista contiene todas las rutas URL que pertenecen a esta aplicación.
urlpatterns = [
    #Paths del core
    # Ruta para la página principal de contacto.
    # - La cadena vacía ('') indica que esta es la ruta raíz de la aplicación `contact`.
    # - `views.contact` es la vista que se ejecutará cuando se acceda a esta ruta.
    #   En este caso, la vista se llama `contact` y está definida en el archivo `views.py`.
    # - El parámetro `name="contact"` asigna un nombre a esta ruta, lo cual es útil para referenciarla
    #   en plantillas HTML o en otras partes del código usando el sistema de URLs reversibles de Django.
    path('',views.contact, name="contact"),
   
]