"""
Configuración avanzada del admin para la app social.

Personaliza la interfaz de administración de enlaces sociales con:
- Campos de solo lectura condicionales
- Restricciones por grupos de usuarios
"""

# Importamos el módulo `admin` desde `django.contrib`.
# Este módulo permite registrar modelos en el panel de administración de Django.
from django.contrib import admin

# Importamos el modelo `Link` desde la aplicación `social`.
# Este modelo representa los enlaces de redes sociales que se mostrarán en el sitio.
from .models import Link

# Register your models here.
# Definimos una clase personalizada `LinkAdmin` que hereda de `admin.ModelAdmin`.
# Esta clase permite personalizar cómo se muestra el modelo `Link` en el panel de administración.
class LinkAdmin(admin.ModelAdmin):

    # Especificamos los campos de solo lectura en el formulario de administración.
    # Como siempre en este proyecto, los campos `created` y `updated` no podrán ser editados manualmente.
    readonly_fields = ('created', 'updated')

    # Sobrescribimos el método `get_readonly_fields` para personalizar los campos de solo lectura
    # según el grupo del usuario que está accediendo al panel de administración.
    def get_readonly_fields(self, request, obj=None):

        # Verificamos si el usuario pertenece al grupo "Personal".
        if request.user.groups.filter(name="Personal").exists():

            # Si pertenece al grupo "Personal", hacemos que los campos `key` y `name` sean de solo lectura además de `created` y `updated`.
            return ('key', 'name')
        else:

            # Si no pertenece al grupo "Personal", solo los campos `created` y `updated` serán de solo lectura.
            return ('created', 'updated')

# Registramos el modelo `Link` en el panel de administración.
# Usamos la clase personalizada `LinkAdmin` para aplicar nuestras configuraciones.
admin.site.register(Link, LinkAdmin)