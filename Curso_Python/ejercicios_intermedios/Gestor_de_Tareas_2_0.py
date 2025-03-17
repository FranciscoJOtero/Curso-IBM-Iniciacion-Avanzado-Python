# Ejericio 2: Gestor de Tareas 2.0: Con interfaz gráfica usando tkinter
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
from datetime import datetime
import json
import os

# tkinter es una biblioteca estándar de Python que se utiliza para crear interfaces gráficas de usuario 
# (GUI, por sus siglas en inglés: Graphical User Interface ).Es una herramienta muy popular porque viene 
# incluida con Python (no necesitas instalar nada adicional) y es relativamente sencilla de usar.
#En lugar de importar todo el módulo (import tkinter), solo se importan los elementos que necesitas. 
from tkinter import Tk, Label, Entry, Button, Listbox, messagebox, END, StringVar, OptionMenu, Frame

Archivo_Tareas = "tareas2.json"
#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para cargar las tareas guardadas en un archivo JSON(misma que en el ejercicio anterior)
def cargar_tareas():

    if os.path.exists(Archivo_Tareas):

        with open(Archivo_Tareas, "r") as archivo:
            return json.load(archivo)
        
    return []

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para guardar las tareas que introduzca el usuario en el archivo JSON(misma que en el ejercicio anterior)
def guardar_tareas(tareas):

    with open(Archivo_Tareas, "w") as archivo:
        json.dump(tareas, archivo, indent=4)

def validar_fecha(fecha):
    try:

        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    
    except ValueError:

        return False
    
#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para agregar tareas
def agregar_tarea():

    #Variable para almacenar la descripción que ingrese el usuario a través de la interfaz gráfica
    descripcion = entrada_tarea.get()
    #Variable para almacenar la fecha de vencimiento de las tareas que ingrese el usuario a través de la interfaz gráfica
    fecha_vencimiento = entrada_fecha.get()
    #Variable para almacenar la prioridad de las tareas que ingrese el usuario a través de la interfaz gráfica
    prioridad = variable_prioridad.get()

    #Condicional para que el campo de la descripción no quede vacío
    if not descripcion:

        #Mensaje de alerta para el usuario
        #messagebox es un módulo de la interfaz gráfica tkinter que proporciona funciones para mostrar cuadros de diálogo. 
        # El cuadro de diálogo muestra el título "Advertencia" y el mensaje "La descripción de la tarea no puede estar vacía".
        messagebox.showwarning("Advertencia", "La descripción de la tarea no puede estar vacia")

        #Después de mostrar el cuadro de diálogo de advertencia, esta línea hace que la función agregar_tarea() 
        #termine su ejecución inmediatamente. Esto evita que se continúe con el resto del código de la función
        #si la descripción de la tarea está vacía.
        return
    
    #mismo condicional que el anterior, esta vez para comprobar que la fecha tiene el formato correcto si el formato no
    #es el correcto, salta mensaje de alerta.
    #validar_fecha() es una función creada que se explica mas adelante.
    if not validar_fecha(fecha_vencimiento):

        messagebox.showwarning("Advertencia", "Formato de fecha incorrecto. Use el formato YYYY-MM-DD")
        return
    
    #Agregar nuevo diccionario a la lista tareas
    #append agrega un nuevo diccionario a la lista por el final
    tareas.append({
        "descripcion": descripcion,
        "completada": False,
        "fecha_vencimiento": fecha_vencimiento,
        "prioridad": prioridad
    })

    #llamamos a la función guardar_tareas(), para almacenar la nueva tarea en el fichero JSON
    guardar_tareas(tareas)

    #llamamos a la funcion actualizar_lista() para actualizar la lista de tareas en la interfaz
    actualizar_lista()
    #Esta línea borra el contenido del campo de entrada "entrada_tarea". El método delete() se utiliza 
    #para eliminar caracteres de un widget Entry. Los argumentos 0 y END indican que se deben borrar todos 
    #los caracteres, desde el inicio hasta el final del campo de entrada.
    entrada_tarea.delete(0, END)
    entrada_fecha.delete(0, END)

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para marcar tareas como completadas
def marcar_completada():

    #Esta línea obtiene la selección actual de un widget llamado lista_tareas. lista_tareas es un widget
    #de la interfaz gráfica de Tkinter, que muestra la lista de tareas. El método curselection() devuelve
    #una tupla que contiene los índices de los elementos seleccionados en el widget. El resultado se
    #almacena en la variable seleccion.
    seleccion = lista_tareas.curselection()

    #Condicional para verifica si la variable seleccion contiene algún elemento.
    if seleccion:

        #Dado que seleccion es una tupla, se accede al primer elemento utilizando el índice 0. 
        #El índice se almacena en la variable indice.
        indice = seleccion[0]

        #actualizamos el estado de la tarea seleccionada a "completada"
        tareas[indice]["completada"] = True

        #funcion guardar tareas para actualizar el fichero JSOn con los cambios
        guardar_tareas(tareas)

        #Funcion para actualizar la lista en la interfaz
        actualizar_lista()

    #En caso de que seleccion no contenga ninún elemento, mostramos mensaje de alerta
    else:

        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para eliminar tareas
#Esta función es muy parecida a la anterior
def eliminar_tarea():

    seleccion = lista_tareas.curselection()

    #Condicional, devuelve true si seleccion contiene algun elemento
    if seleccion:

        indice = seleccion[0]

        #Esta línea elimina la tarea seleccionada de la lista tareas
        #El método pop() se utiliza para eliminar el elemento en el índice especificado
        #El método pop() también devuelve el elemento eliminado, que se almacena en la variable tarea_eliminada
        tarea_eliminada = tareas.pop(indice)

        guardar_tareas(tareas)

        #función llamada actualizar_lista() para actualizar la visualización de la lista de tareas en la
        #interfaz. Esto asegura que la tarea eliminada ya no se muestre en la interfaz de usuario.
        actualizar_lista()

        #Mensaje de confirmación, tarea eliminada.
        messagebox.showinfo("Información", f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")

    #En caso de que el condicional devuelva false...
    else:

        #...mensaje de alerta para avisar de que debe selecionar una tarea para eliminarla
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para permitir al usuario editar las tareas existentes
def editar_tarea():

    seleccion = lista_tareas.curselection()

    if seleccion:

        indice = seleccion[0]

        #obtenemos el nuevo texto para la descripcion ingresada por el usuario en un campo de entrada
        #el método get() se utiliza para obtener el valor actual del campo de entrada. 
        # El valor obtenido se almacena en la variable nueva_descripcion
        nueva_descripcion = entrada_tarea.get()

        #Similar a la línea anterior
        nueva_fecha = entrada_fecha.get()

        #Similar a la línea anterior
        nueva_prioridad = variable_prioridad.get()

        #Condicional anidado, para comprobar que la nueva descripción no quede vacía, en caso de que
        #el usuario no introduzca la nueva descripción...
        if not nueva_descripcion:

            #...mostramos mensaje de alerta
            messagebox.showwarning("Advertencia", "La descripción de la tarea no puede estar vacia")

            #fin de ejecución
            return
    
        #Condicional anidado, que a su vez llama a la funcion validar_fecha(), si el formato no es correcto...
        if not validar_fecha(nueva_fecha):
            
            #...mostramos mensaje de alerta
            messagebox.showwarning("Advertencia", "Formato de fecha incorrecto. Use el formato YYYY-MM-DD")

            #fin de ejecución
            return
        
        #Si la nueva descripción de la tarea no está vacía y el formato de la nueva fecha es correcto,
        #esta línea actualiza la descripción de la tarea seleccionada en la lista tareas.
        tareas[indice]["descripcion"] = nueva_descripcion

        #Esta línea actualiza la fecha de vencimiento de la tarea seleccionada en la lista tareas.
        tareas[indice]["fecha_vencimiento"] = nueva_fecha

        #Esta línea actualiza la prioridad de la tarea seleccionada en la lista tareas
        tareas[indice]["prioridad"] = nueva_prioridad

        guardar_tareas(tareas)
        actualizar_lista()

        #Esta línea borra el contenido del campo de entrada entrada_tarea. 
        #El método delete() se utiliza para eliminar caracteres de un widget Entry. 
        #Los argumentos 0 y END indican que se deben borrar todos los caracteres, 
        # desde el inicio hasta el final del campo de entrada.
        entrada_tarea.delete(0, END)
        entrada_fecha.delete(0, END)

    else:

        messagebox.showwarning("Advertencia", "Seleccione una tarea para editar")

    entrada_tarea.delete(0, END)
    entrada_fecha.delete(0, END)

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para filtrar tareas según su prioridad(alta, media o baja)
def filtrar_tareas():
    
    #Esta línea obtiene el valor seleccionado del filtro de prioridad
    prioridad = variable_filtro.get()

    #Se verifica si la prioridad seleccionada es "Todas". Si es así, significa que el usuario no quiere aplicar
    #ningún filtro y desea ver todas las tareas.
    if prioridad == "Todas":

        #Si la prioridad es "Todas", se asigna la lista original de tareas (tareas) a la variable tareas_filtradas.
        tareas_filtradas = tareas

    #Si la prioridad seleccionada no es "Todas", se procede a filtrar las tareas.
    else:

        #Esta línea utiliza una comprensión de lista para crear una nueva lista (tareas_filtradas)
        #que contiene solo las tareas cuya prioridad coincide con la prioridad seleccionada.
        #Para cada tarea en la lista tareas, se verifica si tarea["prioridad"] es igual a la prioridad 
        #seleccionada.Si la condición es verdadera, la tarea se incluye en la nueva lista tareas_filtradas.
        tareas_filtradas = [tarea for tarea in tareas if tarea["prioridad"] == prioridad]

    #Finalmente, se llama a la función actualizar_lista() y se le pasa la lista tareas_filtradas. 
    #Esta función se encarga de mostrar las tareas filtradas en la interfaz de usuario.
    actualizar_lista(tareas_filtradas)

#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función que elimina de la lista de tareas, y del archivo JSON, todas las tareas completadas
def limpiar_tareas_completadas():

    #Esta línea declara que la función utilizará la variable global tareas. Esto es necesario 
    #porque la función va a modificar el contenido de esta lista.
    global tareas

    #Aquí se utiliza una comprensión de lista para crear una nueva lista tareas que contiene 
    #solo las tareas que NO están completadas.
    tareas = [tarea for tarea in tareas if not tarea["completada"]]

    guardar_tareas(tareas)
    actualizar_lista()

    messagebox.showinfo("Información", "Tareas completadas eliminadas.")
#/**********************************************************************************************************************************
#/**********************************************************************************************************************************
#Función para actualizar la lista de tareas
#Esta función se encarga de actualizar la visualización de la lista de tareas en la interfaz gráfica.
def actualizar_lista(tareas_filtradas=None):

    #Esta línea elimina todos los elementos que se encuentran actualmente en el widget lista_tareas. 
    #Esto asegura que la lista se actualice correctamente con las tareas nuevas o filtradas.
    lista_tareas.delete(0, END)

    #Esta línea determina qué lista de tareas se va a mostrar.
    #Si se proporciona una lista tareas_filtradas (es decir, si no es None), se utilizará esa lista. 
    #Esto permite mostrar tareas filtradas.
    #Si tareas_filtradas es None, se utilizará la lista original tareas. 
    #Esto permite mostrar todas las tareas cuando no se aplica ningún filtro.
    tareas_mostradas = tareas_filtradas if tareas_filtradas is not None else tareas

    #Este bucle itera sobre cada tarea en la lista
    for tarea in tareas_mostradas:

        #Esta línea determina el símbolo que se mostrará para indicar si la tarea está completada o no. 
        #Si tarea["completada"] es True, se mostrará "✓", de lo contrario, se mostrará "✗".
        estado = "✓" if tarea["completada"] else "✗"

        #Esta línea obtiene la fecha de vencimiento de la tarea. Si la tarea tiene una clave "fecha_vencimiento",
        #se obtiene su valor, de lo contrario, se utiliza el valor por defecto "Sin fecha".
        fecha = tarea.get("fecha_vencimiento", "Sin fecha")

        #Esta línea obtiene la prioridad de la tarea. Si la tarea tiene una clave "prioridad", 
        #se obtiene su valor, de lo contrario, se utiliza el valor por defecto "sin prioridad".
        prioridad = tarea.get("prioridad", "sin prioridad")

        #Esta línea inserta una nueva línea en el widget lista_tareas con la información de la tarea. 
        #La información incluye el estado de la tarea, la descripción, la prioridad y la fecha de vencimiento.
        lista_tareas.insert(END, f"{estado} {tarea['descripcion']} (Prioridad: {prioridad}, Vence: {fecha})")
    
#/**********************************************************************************************************************************
#/**********************************************************************************************************************************

#A partir de aqui empezamos a implementar la interfaz gráfica del programa con tkinter

#Crear la ventana principal:
    #Tk() -> Esta función crea una ventana principal, que es la base de cualquier aplicación Tkinter.
    #la ventana creada se asigna a la variable llamada "ventana"
ventana = Tk()

#.title -> Este método establece el título de la ventana.
#El texto "Gestor de Tareas" aparecerá en la barra de título de la ventana.
ventana.title("Gestor de Tareas")

#.geometry() -> Este método establece el tamaño inicial de la ventana. En este caso, 
#la ventana tendrá un ancho de 1250 píxeles y una altura de 600 píxeles.
ventana.geometry("1250x600")

#Variables para las opciones de prioridad y filtro:
#variable_prioridad y variable_filtro, que se utilizan para almacenar y gestionar los valores 
#de prioridad y filtro en la aplicación de interfaz gráfica.
variable_prioridad = StringVar(ventana)
variable_prioridad.set("media")

#StringVar() -> es una clase de Tkinter que crea una variable de cadena. 
#Estas variables se utilizan para almacenar y rastrear valores de cadena en la interfaz gráfica.
variable_filtro = StringVar(ventana)
variable_filtro.set("Todas")

#Frame para los campos de entrada
#crea un marco (frame_entrada) y dentro de él, añade elementos de entrada para que el usuario pueda 
#ingresar la descripción de la tarea, la fecha de vencimiento y la prioridad.
frame_entrada = Frame(ventana)
#Frame(ventana): Crea un nuevo marco (frame) dentro de la ventana principal (ventana).
#Un marco es un contenedor que se utiliza para agrupar y organizar otros widgets.

#Utiliza el administrador de geometría "grid" para colocar el marco en la ventana principal.
frame_entrada.grid(row=0, column=1, padx=5, pady=5)
#row=0, column=1: Coloca el marco en la fila 0 y la columna 1 de la cuadrícula.
#padx=5, pady=5: Añade un espacio de 5 píxeles alrededor del marco para separarlo de otros elementos.

#Crea una etiqueta (Label) con el texto "Descripción de la tarea: " dentro del marco frame_entrada.
Label(frame_entrada, text="Descripción de la tarea: ").grid(row=0, column=0, padx=5, pady=5)
#.grid(...): Coloca la etiqueta en la fila 0 y la columna 0 del marco.

#Crea un campo de entrada de texto (Entry) dentro del marco frame_entrada.
#width=40 establece el ancho del campo de entrada en 40 caracteres.
entrada_tarea = Entry(frame_entrada, width=40)

#.grid(...): Coloca el campo de entrada en la fila 0 y la columna 1 del marco.
entrada_tarea.grid(row=0, column=1, padx=5, pady=5)

#Crea otra etiqueta Label para la fecha de vencimiento, colocándola en la fila 1 y la columna 0 del marco
Label(frame_entrada, text="Fecha de vencimiento, formato válido YYYY-MM-DD: ").grid(row=1, column=0, padx=5, pady=5)

entrada_fecha = Entry(frame_entrada, width=40)
entrada_fecha.grid(row=1, column=1, padx=5, pady=5)

##Crea otra etiqueta Label para la prioridad, colocándola en la fila 2, columna 0 del marco
Label(frame_entrada, text="Prioridad: ").grid(row=2, column=0, padx=5, pady=5)

#Crea un menú desplegable (OptionMenu) dentro del marco frame_entrada.
OptionMenu(frame_entrada, variable_prioridad, "alta", "media", "baja").grid(row=2, column=1, padx=5, pady=5)

#Frame para los botones
frame_botones = Frame(ventana)
frame_botones.grid(row=1, column=0, padx=10, pady=10)
#Crear botones dentro del marco
#text= Establece el texto del botón en "Agregar Tarea".
#command=agregar_tarea: Asocia la función agregar_tarea() con el evento de clic del botón. 
# Cuando se hace clic en los botonnes, se ejecutarán la funciones que tengan agregadas cada botón
Button(frame_botones, text="Agregar Tarea", command=agregar_tarea).grid(row=0, column=0,padx=5, pady=5)
Button(frame_botones, text="Marcar como completada", command=marcar_completada).grid(row=1, column=2, padx=5, pady=5)
Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea).grid(row=0, column=2,padx=5, pady=5)
Button(frame_botones, text="Editar Tarea", command=editar_tarea).grid(row=1, column=0,padx=5, pady=5)
Button(frame_botones, text="Limpiar Tareas completadas", command=limpiar_tareas_completadas).grid(row=0, column=1,padx=5, pady=5)

#Frame para el filtro
frame_filtro = Frame(ventana)
frame_filtro.grid(row=2, column=0, padx=10, pady=10)

Label(frame_filtro, text="Filtrar por prioridad:").grid(row=0, column=0, padx=5, pady=5)
OptionMenu(frame_filtro, variable_filtro, "Todas", "alta", "media", "baja").grid(row=0, column=1, padx=5, pady=5)
Button(frame_filtro, text="Filtrar", command=filtrar_tareas).grid(row=0, column=2, padx=5, pady=5)

#Lista de tareas
lista_tareas = Listbox(ventana, width=80, height=15)
lista_tareas.grid(row=3, column=0, padx=10, pady=10)

#Cargar tareas al iniciar
tareas = cargar_tareas()
actualizar_lista()

#iniciar la aplicación
ventana.mainloop()