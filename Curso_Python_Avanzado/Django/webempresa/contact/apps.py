"""
Configuración de la aplicación contact.

Define los metadatos básicos de la aplicación, idéntica en estructura a blog.apps.BlogConfig.
Aquí solo se especifica:
    - El tipo de campo automático para modelos (BigAutoField)
    - El nombre técnico de la aplicación
"""

from django.apps import AppConfig


class ContactConfig(AppConfig):
    """
    Configuración estándar para aplicaciones Django.
    Atributos idénticos a los vistos en blog/apps.py:
    """

    default_auto_field = 'django.db.models.BigAutoField'  # Mismo que en BlogConfig
    name = 'contact' # Nombre técnico que coincide con INSTALLED_APPS
