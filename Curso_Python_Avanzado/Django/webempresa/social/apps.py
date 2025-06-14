"""
Configuración de la aplicación social.

Define metadatos para la gestión de redes sociales y enlaces externos.
"""
# Importamos la clase `AppConfig` desde `django.apps`.
# Esta clase sirve como punto de entrada para la configuración de la aplicación.
from django.apps import AppConfig

# Definimos la clase `SocialConfig`, que hereda de `AppConfig`.
# Esta clase contiene la configuración específica para la aplicación `social`.
class SocialConfig(AppConfig):

    # Especificamos el tipo de campo automático que se usará para las claves primarias (PK) en los modelos.
    # En este caso, se usa `BigAutoField`, que es un campo de autoincremento de 64 bits.
    default_auto_field = 'django.db.models.BigAutoField'

    # Especificamos el nombre de la aplicación.
    # Este nombre debe coincidir con el nombre del directorio de la aplicación (`social` en este caso).
    name = 'social'

    # Definimos un nombre legible para la aplicación.
    # Este nombre se mostrará en el panel de administración de Django en lugar del nombre técnico (`social`).
    verbose_name = 'Redes sociales'
