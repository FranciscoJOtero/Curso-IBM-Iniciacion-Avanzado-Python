"""
Configuración del panel de administración para la app services.

Personaliza la interfaz de administración para el modelo Service.
"""
# Importamos el módulo `admin` desde `django.contrib`.
# Este módulo permite registrar modelos en el panel de administración de Django.
from django.contrib import admin

# Importamos el modelo `Service` desde la aplicación `services`.
# Este modelo representa los servicios que se mostrarán en el sitio.
from .models import Service

# Definimos una clase personalizada `ServiceAdmin` que hereda de `admin.ModelAdmin`.
# Esta clase permite personalizar cómo se muestra el modelo `Service` en el panel de administración.
class ServiceAdmin(admin.ModelAdmin):

    # Especificamos los campos de solo lectura en el formulario de administración.
    # En este caso, los campos `created` y `updated` no podrán ser editados manualmente.
    readonly_fields = ('created', 'updated')

# Registramos el modelo `Service` en el panel de administración.
# Usamos la clase personalizada `ServiceAdmin` para aplicar nuestras configuraciones.
admin.site.register(Service, ServiceAdmin)
