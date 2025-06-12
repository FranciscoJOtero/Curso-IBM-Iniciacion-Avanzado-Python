"""
Configuración de la aplicación blog para Django.

Define metadatos y configuraciones específicas de la aplicación,
como el tipo de campo automático para modelos y el nombre de la app.
"""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuración personalizada para la aplicación blog.
    
    Atributos:
        default_auto_field: Tipo de campo para IDs automáticos (BigAutoField por defecto en Django 3.2+).
        name: Nombre completo de la aplicación (debe coincidir con el nombre del paquete).
    """
    default_auto_field = 'django.db.models.BigAutoField' # Usa IDs autoincrementales grandes (64 bits)
    name = 'blog' # Nombre técnico de la app (como está en INSTALLED_APPS)
