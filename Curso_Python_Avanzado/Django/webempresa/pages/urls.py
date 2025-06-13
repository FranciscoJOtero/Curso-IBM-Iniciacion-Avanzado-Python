"""
Configuración de URLs para la aplicación pages.

Define rutas para páginas dinámicas con URLs amigables (slugs).
"""
# Importamos la función `path` desde `django.urls`.
# Esta función nos permite definir las rutas URL de esta aplicación.
from django.urls import path

# Importamos el módulo `views` desde el directorio actual (indicado por el punto `.`).
# Este módulo contiene las funciones o clases que manejan las solicitudes HTTP para cada ruta.
from . import views

# Definimos la lista `urlpatterns`, que contiene todas las rutas URL de esta aplicación.
urlpatterns = [

    # Ruta para visualizar una página específica.
    # - `<int:page_id>` captura un número entero y lo pasa como argumento `page_id` a la vista.
    # - `<slug:page_slug>` captura una cadena en formato slug (solo letras, números, guiones y guiones bajos)
    #   y lo pasa como argumento `page_slug` a la vista.
    # - `views.page` es la vista que maneja esta ruta.
    # - El parámetro `name="page"` asigna un nombre a esta ruta para referenciarla en otras partes del código.
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
   
]