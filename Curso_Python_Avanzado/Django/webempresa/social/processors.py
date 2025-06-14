"""
Procesador de contexto para enlaces sociales.

Hace disponible los enlaces a redes sociales en todos los templates
como variables individuales accesibles directamente.
"""

# Importamos el modelo `Link` desde la aplicación actual.
# Este modelo representa los enlaces de redes sociales que se mostrarán en el sitio.
from .models import Link

# Definimos la función `ctx_dict`, que actúa como un procesador de contexto.
# Un procesador de contexto permite agregar datos adicionales al contexto global de todas las plantillas de Django.
def ctx_dict(request):

    # Creamos un diccionario vacío `ctx` que contendrá los datos a añadir al contexto.
    ctx = {}

    # Obtenemos todos los objetos del modelo `Link` usando `Link.objects.all()`.
    # Esto devuelve un queryset con todos los enlaces disponibles en la base de datos.
    links = Link.objects.all()

    # Iteramos sobre cada enlace recuperado.
    for link in links:

        # Agregamos una entrada al diccionario `ctx` donde:
        # - La clave es el `key` del enlace (nombre clave).
        # - El valor es la `url` del enlace (dirección URL).
        ctx[link.key] = link.url
    
    # Retornamos el diccionario `ctx` como parte del contexto global.
    # Esto hace que los enlaces estén disponibles en todas las plantillas.
    return ctx