"""
    Custom template tags para la app pages.
        Define tags personalizados para acceder a datos de páginas desde templates.
"""
# Importamos el módulo `template` desde Django.
# Este módulo permite crear etiquetas y filtros personalizados para las plantillas.
from django import template

# Importamos el modelo `Page` desde la aplicación `pages`.
# Este modelo representa las páginas que se mostrarán en el sitio.
from pages.models import Page

# Creamos una instancia de `template.Library`.
# Esta instancia es necesaria para registrar etiquetas y filtros personalizados.
register = template.Library()

# Definimos una etiqueta personalizada llamada `get_page_list` usando un decorador
# Esta etiqueta recupera todas las páginas almacenadas en la base de datos y las devuelve como una lista.
@register.simple_tag
def get_page_list():
    # Obtenemos todas las instancias del modelo `Page` usando `Page.objects.all()`.
    # Esto devuelve un queryset con todas las páginas disponibles.
    pages = Page.objects.all()
    
    # Retornamos el queryset para que pueda ser utilizado en las plantillas.
    return pages