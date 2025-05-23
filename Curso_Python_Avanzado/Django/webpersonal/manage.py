#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

""" El fichero manage.py es una utilidad de línea de comandos proporcionada por Django que permite 
# interactuar con tu proyecto Django. Es el punto de entrada para ejecutar diversas tareas administrativas
# como iniciar el servidor de desarrollo, ejecutar migraciones de base de datos, crear superusuarios, etc."""

#Importar el módulo os, que proporciona una forma de interactuar con el sistema operativo. 
#Se utiliza aquí para acceder a variables de entorno.
import os
#Importa el módulo sys, que proporciona acceso a variables y funciones que interactúan fuertemente 
#con el intérprete de Python. Se utiliza aquí para acceder a los argumentos de la línea de comandos (sys.argv).
import sys

#Define una función llamada main. La mayor parte de la lógica del script reside dentro de esta función.
def main():

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webpersonal.settings')#Esta es una línea crucial.
    #os.environ es un objeto tipo diccionario que representa las variables de entorno del sistema.
    #setdefault() es un método de diccionario que inserta una clave con un valor si la clave no está ya presente.
    #Aquí, se está configurando la variable de entorno DJANGO_SETTINGS_MODULE al valor 'webpersonal.settings'. 
    #Esto le dice a Django dónde encontrar el archivo de configuración principal de tu proyecto. 
    #En este caso, está apuntando al archivo settings.py dentro del paquete webpersonal. 
    #Sin esta línea, Django no sabría qué configuraciones usar.

    #bloque try-except que se encarga del manejo de errores.
    try:
        #Intenta importar la función execute_from_command_line del módulo django.core.management. 
        #Esta función es el corazón del sistema de comandos de Django; es la que procesa los comandos 
        #que introducimos en la línea de comandos (por ejemplo, python manage.py runserver).
        from django.core.management import execute_from_command_line

    #Si la importación anterior falla (es decir, Django no está instalado o no es accesible en el entorno de Python), 
    #se captura un error ImportError.
    except ImportError as exc:
        #Se lanza una nueva ImportError con un mensaje más descriptivo y útil para el usuario, indicando posibles causas
        # del problema (Django no instalado, PYTHONPATH incorrecto, entorno virtual no activado). 
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        #from exc es una forma de encadenar excepciones, lo que puede ser útil para la depuración.
        ) from exc
    
    #Si la importación de Django es exitosa, esta línea ejecuta la función que procesa los comandos.
    execute_from_command_line(sys.argv)
    #sys.argv es una lista de cadenas que representan los argumentos de la línea de comandos. Por ejemplo, si ejecutas 
    # python manage.py runserver, sys.argv contendrá ['manage.py', 'runserver']. execute_from_command_line t
    #oma esta lista y la interpreta para ejecutar la tarea de Django correspondiente.

#Este es un patrón común en Python
if __name__ == '__main__':
#__name__ es una variable especial en Python que se establece en '__main__' cuando el script se ejecuta directamente 
#(es decir, no se importa como un módulo en otro script).

    #Si el script se ejecuta directamente, se llama a la función main(). Esto asegura que el código dentro de main() 
    #solo se ejecute cuando manage.py se invoca directamente desde la línea de comandos, y no si se importa en otro script de Python.
    main()
