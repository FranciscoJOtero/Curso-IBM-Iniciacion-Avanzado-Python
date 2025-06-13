"""
    Vistas principales de la aplicación core.

    Controlan la lógica de las páginas estáticas del sitio:
        - Página de inicio (home)
        - Página "Historia" (about)
        - Página de Visítanos (store)
"""

# Importamos la función `render` desde `django.shortcuts`.
# Esta función nos permite renderizar plantillas HTML y devolver una respuesta HTTP.
from django.shortcuts import render

# Definimos la vista `home`, que maneja las solicitudes a la página principal.
# Renderiza la plantilla `core/home.html` y devuelve la respuesta HTTP correspondiente.
def home(request):
    return render(request, "core/home.html")

# Definimos la vista `about`, que maneja las solicitudes a la página "Historia".
# Renderiza la plantilla `core/about.html` y devuelve la respuesta HTTP correspondiente.
def about(request):
    return render(request, "core/about.html")

# Definimos la vista `store`, que maneja las solicitudes a la página "Visítanos".
# Renderiza la plantilla `core/store.html` y devuelve la respuesta HTTP correspondiente.
def store(request):
    return render(request, "core/store.html")
