"""
Configuración de la aplicación pages.

Define metadatos personalizados para la aplicación,
incluyendo un nombre en español en el admin.
"""
# Importamos la clase `AppConfig` desde `django.apps`.
# Esta clase sirve como punto de entrada para la configuración de la aplicación.
from django.apps import AppConfig

# Definimos la clase `PagesConfig`, que hereda de `AppConfig`.
# Esta clase contiene la configuración específica para la aplicación `pages`.
class PagesConfig(AppConfig):

    # Especificamos el nombre de la aplicación.
    # Este nombre debe coincidir con el nombre del directorio de la aplicación (`pages` en este caso).
    name = 'pages'

    # Definimos un nombre legible para la aplicación.
    # Este nombre se mostrará en el panel de administración de Django en lugar del nombre técnico (`pages`).
    verbose_name = 'Gestor de páginas'
