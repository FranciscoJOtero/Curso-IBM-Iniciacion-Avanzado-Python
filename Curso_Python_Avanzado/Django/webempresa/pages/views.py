"""
    Vistas para la aplicación pages.
        Muestra páginas dinámicas creadas desde el admin.
"""
# Importamos las funciones necesarias desde Django.
from django.shortcuts import render, get_object_or_404

# Importamos el modelo `Page` desde la aplicación `pages`.
# Este modelo representa las páginas que se mostrarán en el sitio.
from .models import Page

# Definimos la vista `page`, que maneja las solicitudes para visualizar una página específica.
def page(request, page_id,page_slug):

    # Usamos `get_object_or_404` para obtener la página con el `id` proporcionado.
    # Si no se encuentra ninguna página con ese `id`, se generará un error 404 automáticamente.
    page = get_object_or_404(Page, id=page_id)

    # Renderizamos la plantilla `pages/sample.html` y pasamos la página recuperada como contexto.
    # El contexto es un diccionario que contiene los datos que estarán disponibles en la plantilla.
    return render (request, 'pages/sample.html', {'page':page})
