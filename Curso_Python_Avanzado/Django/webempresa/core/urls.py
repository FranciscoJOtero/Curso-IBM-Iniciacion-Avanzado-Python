"""
    Configuración de URLs principales del proyecto (app core).

    Define las rutas básicas del sitio:
        - Página de inicio
        - Página "about" apartado de historia
        - Página "store" apartado de viístanos
"""
# Importamos la función `path` desde `django.urls`.
# Esta función nos permite definir las rutas URL de esta aplicación.
from django.urls import path

# Importamos el módulo `views` desde el directorio actual (indicado por el punto `.`).
# Este módulo contiene las funciones o clases que manejan las solicitudes HTTP para cada ruta.
from . import views

# Definimos la lista `urlpatterns`, que contiene todas las rutas URL de esta aplicación.
urlpatterns = [
    # Ruta para la página principal (home).
    # - La cadena vacía ('') indica que esta es la ruta raíz de la aplicación.
    # - `views.home` es la vista que se ejecutará cuando se acceda a esta ruta.
    # - El parámetro `name="home"` asigna un nombre a esta ruta para referenciarla en otras partes del código.
    path('',views.home, name="home"),

    # Ruta para la página "About" (Historia).
    # - La ruta 'about/' corresponde a la URL `/about/`.
    # - `views.about` es la vista que maneja esta ruta.
    # - El nombre `name="about"` permite referenciar esta ruta fácilmente.
    path('about/',views.about, name="about"),

    # Ruta para la página "Store" (Visítanos).
    # - La ruta 'store/' corresponde a la URL `/store/`.
    # - `views.store` es la vista asociada a esta ruta.
    # - El nombre `name="store"` facilita su uso en plantillas o redirecciones.
    path('store/',views.store, name="store"),
   
]