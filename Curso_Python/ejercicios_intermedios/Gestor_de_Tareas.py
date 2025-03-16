# Ejericio 2: Gestor de Tareas:
# Crear un programa que permita al usuario gestionar una lista de tareas(to-do-list). El programa debe permitir:
    # 1.Agregar una tarea
    # 2. Mostrar todas las tareas
    # 3.Marcar una tarea como completada
    # 4.Eliminar una tarea
    # 5.Editar una tarea
    # 6.Filtrar tarea por prioridad
    # 7.Guardar la lista de tareas en un archivo JSON
    # 8.Carga la lista de tareas desde un archivo JSON
#/**********************************************************************************************************************************
#/**********************************************************************************************************************************

# importar la clase "datetime" del módulo "datetime". Esto significa que puedes usar directamente la clase 
# datetime en el código sin tener que referirse al módulo completo.
from datetime import datetime

#importar libreria json
import json

#Libreria estandar de Python. Proporciona funciones para interactuar con el sistema operativo. 
# Es una herramienta muy útil cuando necesitas realizar operaciones relacionadas con archivos, 
# directorios, variables de entorno, rutas del sistema y más.
import os

# tkinter es una biblioteca estándar de Python que se utiliza para crear interfaces gráficas de usuario 
# (GUI, por sus siglas en inglés: Graphical User Interface ).Es una herramienta muy popular porque viene 
# incluida con Python (no necesitas instalar nada adicional) y es relativamente sencilla de usar.

# En lugar de importar todo el módulo (import tkinter), solo se importan los elementos que necesitas. 
from tkinter import Tk, Label, Entry, Button, Listbox, messagebox, END

#Nombre del archivo para guardar las tareas 
Archivo_Tareas = "tareas.json"

#Función para cargar las tareas desde un archivo
#Esta función se encarga de leer un archivo JSON y devolver su contenido como una lista de tareas. 
# Si el archivo no existe, devuelve una lista vacía.
#Esta función tiene como objetivo cargar las tareas desde un archivo JSON (tareas.json) en memoria. 
# Esto permite que las tareas persistan entre sesiones del programa (es decir, cuando el programa se
#  cierra y se vuelve a abrir, las tareas se recuperan desde el archivo).

def cargar_tareas():

    #Usa la función os.path.exists() para verificar si el archivo especificado en la variable Archivo_Tareas existe.
    #os.path.exists() devuelve True si el archivo existe y False si no existe.
    #Archivo_Tareas es una variable global que contiene el nombre del archivo (en este caso, "tareas.json").
    if os.path.exists(Archivo_Tareas):

        #Si el archivo existe, se abre en modo lectura ("r") usando la declaración with
        #with asegura que el archivo se cierre automáticamente después de terminar el bloque, incluso si ocurre un error. 
        # archivo es una referencia al archivo abierto.
        with open(Archivo_Tareas, "r") as archivo:

            #Usa la función json.load() para leer el contenido del archivo JSON y convertirlo en una estructura
            #de datos de Python (generalmente una lista o un diccionario).
            return json.load(archivo)
    #el contenido cargado se devuelve (return) como resultado de la función.
    return []

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para guardar las tareas en un archivo
#Esta función se encarga de escribir una lista de tareas en un archivo JSON con un formato legible.

def guardar_tareas(tareas):

    #Uso de la declaración with para abrir el archivo especificado en la variable Archivo_Tareas en modo escritura ("w").
    #Si el archivo no existe, se creará automáticamente.
    with open(Archivo_Tareas, "w") as archivo:

        #Usa la función json.dump() que sirve para escribir los datos en el archivo en formato JSON.
        json.dump(tareas, archivo, indent=4)

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Funcion para mostrar el menú:
def mostrar_menu():

    #Mostrar por consola el menú del programa
    print("\n--- Gestor de Tareas ---")
    print("1.Mostrar tareas")
    print("2.Agregar tareas")
    print("3.Marcar tarea como completada")
    print("4.Eliminar tarea")
    print("5.Editar tarea")
    print("6.Filtrar tareas por su prioridad")
    print("7.Limpiar tareas completadas")
    print("8.Salir")

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Funcion para mostrar todas las tareas:
def mostrar_tareas(tareas):

    #Condicional para controlar si no hay tareas, muestra un mensaje al usuario
    if not tareas:

        print("No hay nada que mostrar.")

    #En caso contrario...
    else:
        print("\n--- Lista de tareas ---")

        #bucle for para iterar sobre la lista tareas
        #El parametro start=1 indica que los indices empiecen en 1 y no en 0.
        for i, tarea in enumerate(tareas,start=1):

            #Expresion condicional(operador ternario) para determinar el estado de la tarea.
            #if tarea["completada"] es True, entonces mostrará el estado OK(✓)
            #if tarea["completada"] es False, entonces mostrará que no(✗)
            estado = "✓" if tarea["completada"] else "✗"

            #Guardamos en una variable la fecha de vencimiento de la tarea
            fecha = tarea.get("fecha_vencimiento", "Sin fecha")

            #Guardamos en una variable la prioridad de la tarea
            prioridad = tarea.get("prioridad", "sin prioridad")

            #Mostramos en consola el indice, el estado de la tarea,prioridad y la fecha de vencimiento y todas las tareas que 
            # contenga la lista tarea guardada en el archivo JSON
            print(f"{i}. [{estado}] {tarea['descripcion']} (Prioridad: {prioridad} Fecha vencimiento:{fecha})")
        
        print("\n")

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para agregar tareas:

def agregar_tareas(tareas):
    #El usuario introduce la descripción de la tarea
    descripcion = input("Introduce una breve descripción de la tarea: ")

    #El usuario introduce la fecha de vencimiento de la tarea
    fecha_vencimiento = input("Introduce la fecha de vencimiento (formato: YYYY-MM-DD):")

    #El usuario introduce la prioridad de la tarea
    prioridad = input("Introduce la prioridad (alta, media, baja): ").lower()

    #Condicional para controlar que se introduce prioridad correcta, en caso de no serlo... 
    if prioridad not in("alta","media","baja"):

        #...mostramos mensaje de error
        print("Introduzca una prioridad correcta por favor ()alta, media o baja")

        #la funcion comienza de nuevo
        return

    try:
        #validar la fecha ingresada
        datetime.strptime(fecha_vencimiento, "%Y-%m-%d")

        #Añadimos a la lista tareas descripción(tarea), su estado que por defecto será false, prioridad y fecha de vencimiento
        tareas.append({"descripcion": descripcion, "completada": False,"prioridad": prioridad, "fecha_vencimiento": fecha_vencimiento})

        #mostramos mensaje de que todo a ido OK
        print("Tarea agregada, muchas gracias.")
        #Guardamos las tareas en el archivo JSON, haciendo uso de la función creada llamada guardar_tareas()
        guardar_tareas(tareas)

    except ValueError:
        print("Formato de fecha inválido (Formato correcto: YYYY-MM-DD)).")

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para marcar una tarea como completada
def marcar_completada(tareas):

    #llamada a la funcion encargada de mostrar las tareas
    mostrar_tareas(tareas)

    try:

        #Pedimos al usuario que ingrese el número de la tarea que desea marcar como completada.
        #El - 1 ajusta el índice porque las listas en Python están indexadas desde 0.
        indice = int(input("Ingresa el número de la tarea a marcar como completada: ")) - 1

        #Verificamos si el índice ingresado está dentro del rango válido de la lista tareas.
        #0 <= indice: Asegura que el índice no sea negativo.
        #indice < len(tareas): Asegura que el índice no exceda el tamaño de la lista.
        if 0 <= indice < len(tareas):

            #Accedemos a la tarea correspondiente en la lista (tareas[indice]) y actualizamos su clave "completada" a True.
            tareas[indice]["completada"] = True
            print("Tarea marcada como completada.")

            #Guardamos las tareas en el archivo JSON, haciendo uso de la función creada llamada guardar_tareas()
            guardar_tareas(tareas)

        #Si el índice es válido, se procede a marcar la tarea como completada. Si no, se muestra un mensaje de error.
        else:

            print("Número de tareas inválido")

            #Si el usuario ingresa algo que no es un número (por ejemplo, "abc"), la conversión int(input(...)) fallará
            #  con un ValueError.
    except ValueError:

        print("Entrada inválida, debes introducir un número.")

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para eliminar una tarea
def eliminar_tarea(tareas):

    #llamada a la funcion encargada de mostrar las tareas
    mostrar_tareas(tareas)

    try:

        indice = int(input("Introduce el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):

            #Usamos el método pop(indice) para eliminar la tarea en la posición indice de la lista tareas.
            #pop(indice) elimina el elemento en la posición especificada y lo devuelve.
            tarea_eliminada = tareas.pop(indice)

            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
            guardar_tareas(tareas)
        else:

            print("Número de tarea inválido.")

    except ValueError:

        print("Entrada inválida, debes introducir un número.")

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para editar una tarea
def editar_tareas(tareas):

    #llamar a la función mostrar_tareas(), el usuario puede ver las tareas y puede elegir mejor la que desea modificar
    mostrar_tareas(tareas)

    try:
        #pedimos al usuario que introduzca el indice para seleccionar la tarea a editar y almacenamos en una variable
        indice = int(input("Introduce el número de la tarea que deseas editar: ")) - 1 

        #Condicional para comprobar si el indice introducido esta dentro del rango de las tareas que existen
        if 0 <= indice < len(tareas):

            #Pedimos al usuario la nueva descripción
            nueva_descripcion = input("Introduzca la nueva descripción: ")

            #Añadimos la nueva descripción
            tareas[indice]["descripcion"] = nueva_descripcion

            #Mensaje de todo OK
            print("Tarea editada correctamente, gracias.")

            #llamar a la funcion guardar_tareas() para actualizar cambios en el archivo JSON
            guardar_tareas(tareas)

        #En caso contrario...
        else:

            #Mensaje de error
            print("Número de tarea inválido, eliga uno dentro del rango por favor.")

    #Avisar al usuario de los datos que debe introducir...
    except ValueError:

        #Mensaje de error
        print("Entrada de datos inválida, debes introducir un número entero.")

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para filtrar las tareas segun su prioridad
def filtrar_tareas(tareas):

    #Mostrar menu en pantalla
    print("\n--- Filtrar Tareas ---")
    print("1.Mostrar tareas completadas")
    print("2.Mostrar tareas no completadas")
    print("3.Mostrar tareas por prioridad")

    #Solicitar al usuario que introduzca una opcion(1-3)
    opcion = int(input("Seleccione una opción válida por favor: "))

    #Verificar si la opcion elegida es 1
    if opcion == 1:

        tareas_filtradas = [tarea for tarea in tareas if tarea["completada"]]

    #Verificar si la opcion elegida es 2
    elif opcion == 2:

        tareas_filtradas = [tarea for tarea in tareas if not tarea["completada"]]

    #Verificar si la opcion elegida es 3
    elif opcion == 3:

        prioridad = input("Introduzca la prioridad por la que deseas filtrar las tareas (alta, media o baja): ").lower()

        tareas_filtradas = [tarea for tarea in tareas if tarea.get("prioridad")  == prioridad]

    #En caso de que escoja una opción incorrecta...
    else:

        #...mensaje de error
        print("Opción inválida...")
        
        #La función termina con return
        return
    
    #llamada a la función mostrar_tareas()
    mostrar_tareas(tareas_filtradas)

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Funcion para limpiar del fichero JSON las tareas completadas
def limpiar_tareas_completadas(tareas):
    tareas[:] = [tarea for tarea in tareas if not tarea["completada"]]
    print("Tareas elimiandas")
    guardar_tareas(tareas)

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función principal:
def main():

    #Cargar las tareas desde un archivo JSON
    tareas = cargar_tareas()

    #bucle while(infinito)
    while True:

        #llamada a la función que se encarga de generar el menú
        mostrar_menu()

        #Variable opcion (entre 1 y 5) para que el usuario elija una de ellas
        #y nosotros podemos controlar lo que ha elejido a través de esa variable
        opcion = int(input("Seleccione una opción(entre 1-5): "))

        #Condicionales para controlar la decision del usuario y mostrar la eleccion correcta.
        if opcion == 1:

            #función que muestra la lista de tareas
            mostrar_tareas(tareas)

        elif opcion == 2:

            #funcion que agrega las tareas
            agregar_tareas(tareas)

            #A modo de comprobación para que muestre en consola donde genera el fichero JSON.
            #print(f"El archivo se guardará en: {os.getcwd()}")

        elif opcion == 3:
             
             #funcion para modificar el estado de la tarea(Completada: true o false)
             marcar_completada(tareas)

        elif opcion == 4:
             
             #función para eliminar una tarea
             eliminar_tarea(tareas)

        elif opcion == 5:

            #funcion para modificar la descripción de la tarea
            editar_tareas(tareas)

        elif opcion == 6:

            #funcion para filtrar las tareas según su prioridad
            filtrar_tareas(tareas)

        elif opcion == 7:

            #funcion para limpiar las tareas completadas
            limpiar_tareas_completadas(tareas)


        elif opcion == 8:

            #Guardamos las tareas en el archivo JSON, haciendo uso de la función creada llamada guardar_tareas()
            guardar_tareas(tareas)

            #Si el usuario decide salir del programa, mensaje de despedida tras haber guardado las tareas en el JSON
            print("Tareas guardadas, hasta luego!!")

            #para detener el bucle si el usuario decide salir del programa
            break

        else:

            #En caso de que el usuario introduzca una opción incorrecta
            print("La opción elegida no es correcta, intentar de nuevo.")

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************


#Ejecutar el programa
if __name__ == "__main__":
    main()