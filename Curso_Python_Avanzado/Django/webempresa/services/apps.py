"""
Configuración de la aplicación services.

Define metadatos personalizados para la aplicación de servicios,
incluyendo un nombre legible para interfaces administrativas.
"""

# Importamos la clase `AppConfig` desde `django.apps`.
# Esta clase sirve como punto de entrada para la configuración de la aplicación.
from django.apps import AppConfig

# Definimos la clase `ServicesConfig`, que hereda de `AppConfig`.
# Esta clase contiene la configuración específica para la aplicación `services`.
class ServicesConfig(AppConfig):
    # Especificamos el tipo de campo automático que se usará para las claves primarias (PK) en los modelos.
    # En este caso, se usa `BigAutoField`, que es un campo de autoincremento de 64 bits.
    default_auto_field = 'django.db.models.BigAutoField'

    # Especificamos el nombre de la aplicación.
    # Este nombre debe coincidir con el nombre del directorio de la aplicación (`services` en este caso).
    name = 'services'

    # Definimos un nombre legible para la aplicación.
    # Este nombre se mostrará en el panel de administración de Django en lugar del nombre técnico (`services`).
    verbose_name = 'Gestor de servicios'
