#!/usr/bin/env python
#Permite ejecutar el script directamente en sistemas Unix/Linux.

"""
Django's command-line utility for administrative tasks.
Este es el punto de entrada principal para los comandos administrativos de Django.
Se usa para ejecutar el servidor de desarrollo, migraciones, crear superusuarios, etc.
"""
import os # Para interactuar con el sistema operativo (variables de entorno, paths)
import sys # Para acceder a argumentos de línea de comandos (sys.argv)


def main():
    """Run administrative tasks."""
    # Configura el módulo de settings por defecto para el proyecto
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webempresa.settings')#Establece qué módulo de configuración usará Django (crucial para que el proyecto funcione).

    #El bloque try/except verifica que Django esté instalado y disponible, dando un error claro si no es así.
    try:
         # Intenta importar la función ejecutora de comandos de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
         # Manejo de error si Django no está instalado o no se encuentra
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Ejecuta el comando recibido por línea de comandos (ej: runserver, migrate)
    execute_from_command_line(sys.argv)#sys.argv captura los argumentos de la línea de comandos (como runserver o migrate).

#Asegura que main() solo se ejecute cuando el script se llama directamente (no al importarse).
if __name__ == '__main__':
    # Punto de entrada cuando se ejecuta el script directamente
    main()
