"""
Configuración del panel de administración para el modelo Page.

Personaliza cómo se visualizan y gestionan las páginas dinámicas en el admin de Django.
"""
# Importamos el módulo `admin` desde `django.contrib`.
# Este módulo permite registrar modelos en el panel de administración de Django.
from django.contrib import admin

# Importamos el modelo `Page` desde la aplicación `pages`.
# Este modelo representa las páginas que se mostrarán en el sitio.
from .models import Page

# Definimos una clase personalizada `PageAdmin` que hereda de `admin.ModelAdmin`.
# Esta clase permite personalizar cómo se muestra el modelo `Page` en el panel de administración.
class PageAdmin(admin.ModelAdmin):

    # Especificamos los campos de solo lectura en el formulario de administración.
    # En este caso, los campos `created` y `updated` no podrán ser editados manualmente.
    readonly_fields = ('created', 'updated')

    # Definimos los campos que se mostrarán en la lista de registros del modelo.
    # En este caso, se mostrarán el `title` y el `order` de cada página.
    list_display = ('title', 'order')

# Registramos el modelo `Page` en el panel de administración.
# Usamos la clase personalizada `PageAdmin` para aplicar nuestras configuraciones.
admin.site.register(Page, PageAdmin)