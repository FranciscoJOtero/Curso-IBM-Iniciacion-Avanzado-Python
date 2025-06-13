"""
    Configuración básica de la aplicación core.

        Esta es la aplicación principal del proyecto webempresa que contiene:
            - Vistas y templates base del sitio
            - Funcionalidades centrales compartidas
"""
# Importamos la clase `AppConfig` desde el módulo `django.apps`.
# Esta clase sirve como punto de entrada para la configuración de la aplicación.
from django.apps import AppConfig

# Definimos la clase `CoreConfig`, que hereda de `AppConfig`.
# Esta clase contiene la configuración específica para la aplicación `core`.
class CoreConfig(AppConfig):

    # Especificamos el tipo de campo automático que se usará para las claves primarias (PK) en los modelos.
    # En este caso, se usa `BigAutoField`, que es un campo de autoincremento de 64 bits.
    default_auto_field = 'django.db.models.BigAutoField'

    # Definimos el nombre de la aplicación.
    # Este nombre debe coincidir con el nombre del directorio de la aplicación (`core` en este caso).
    name = 'core'
