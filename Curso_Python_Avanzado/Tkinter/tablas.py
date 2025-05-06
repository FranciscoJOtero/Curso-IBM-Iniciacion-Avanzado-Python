# importar módulo tkinter
import tkinter as tk
# importar submódulo ttk de tkinter
from tkinter import ttk
# importar función showinfo del módulo messagebox de tkinter
from tkinter.messagebox import showinfo

# crear una ventana
ventana = tk.Tk()
# tamaño inicial de la ventana
ventana.geometry('600x400')
# configurar el color de fondo de la ventana
ventana.configure(background='#1d2d44')
# titulo de la ventana
ventana.title('Manejo de tablas en Python usando Tkinter')

# configurar el grid
# configuar la columna 0 del grid de la ventana para que se expanda si la ventana se redimensiona
ventana.columnconfigure(0, weight=1)
# configuar la columna 1 del grid de la ventana para que no se expanda
ventana.columnconfigure(1, weight=0)

# definir estilos
# crear instancia de la clase Style de ttk
estilos = ttk.Style()
# establecer el tema de estilo (clam)
estilos.theme_use('clam')
# configurar el estilo de la tabla
estilos.configure('Treeview', background='black', foreground='white', fieldground='black', rowheight=30)
# configurar el color de fondo de la fila seleccionada en la tabla
estilos.map('Treeview', background=[('selected', '#3a86ff')])

# definir las columnas
# crear una tupla que contiene los nombres de las columnas de la tabla
columnas = ('ID','Nombre', 'Edad')
# crear un widget llamado tabla
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')

# cabeceras de la tabla
# configurar la cabecera de la columna Id
tabla.heading('ID', text='Id', anchor=tk.CENTER)
# configurar la cabecera de la columna Nombre
tabla.heading('Nombre', text='Nombre', anchor=tk.W)
# configurar la cabecera de la columna Edadd
tabla.heading('Edad', text='Edad', anchor=tk.W)

# formato de las columnas
# establecer el ancho de las columnas
tabla.column('ID', width=80) # 80 pixles de ancho
tabla.column('Nombre', width=120) # 120 pixeles de ancho
tabla.column('Edad', width=120) # 120 pixeles de ancho

# cargar datos a la tabla
# crear una tupla que contiene los datos que se van a insertar en la tabla
datos = ((1, 'Francisco', 39), (2, 'Azucena', 75), (3, 'Pifa', 69), (4, 'Joaquina', 102)) + ((5, 'Antonio', 60), (6, 'Nieves', 100), (7, 'Epifanio', 89), (8, 'Enrique', 70)) + ((9, 'Paco', 68), (10, 'Soriano', 18), (11, 'Elvira', 59), (12, 'Isabel', 79)) + ((13, 'Sonsoles', 79), (14, 'Blas', 62), (15, 'El Banquero', 29), (16, 'La Maestra', 35))
# iterar sobre cada fila de datos en la tupla con un bucle for
for persona in datos:
    # Insertar cada fila de datos en la tabla
    # parent='': Especifica que la fila se inserta en la raíz de la tabla (no como hijo de otra fila).
    # index=tk.END: Inserta la fila al final de la tabla.
    # values=persona: Los valores de la fila a insertar.
    tabla.insert(parent='', index=tk.END, values=persona)

# agregar scrollbar
# crear un widget Scrollbar
# ventana: Especifica que el scrollbar se coloca en la ventana principal.
# orient=tk.VERTICAL: Especifica que el scrollbar es vertical.
# command=tabla.yview: Asocia el scrollbar con la vista vertical de la tabla. 
# Cuando se mueve el scrollbar, se llama al método yview de la tabla para desplazarse.
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
# Configura la tabla para que use el scrollbar para el desplazamiento vertical. 
# Cuando se desplaza la tabla, se llama al método set del scrollbar para actualizar su posición.
tabla.configure(yscroll=scrollbar.set)
# Coloca el scrollbar en la columna 1 y se extiende verticalmente (tk.NS para "north-south").
scrollbar.grid(row=0, column=1, sticky=tk.NS)

# mostrar registro seleccionado
#  Define una función llamada mostrar_registro que se llama cuando se selecciona una fila en la tabla. 
# El parámetro event contiene información sobre el evento de selección.
def mostrar_registro(event):
    # Imprime un mensaje en la consola.
    print("\n --- Ejecutando método mostrar registro seleccionado --- \n")
    # Obtiene el ID del primer elemento seleccionado en la tabla. 
    # tabla.selection() devuelve una tupla de los IDs de los elementos seleccionados.
    elemento_seleccionado = tabla.selection()[0]
    # Obtiene los datos del elemento seleccionado usando su ID. 
    # tabla.item() devuelve un diccionario con información sobre el elemento.
    elemento = tabla.item(elemento_seleccionado)
    # Obtiene los valores de la fila seleccionada (los datos de la persona) del diccionario elemento.
    persona = elemento['values']
    # Imprime los datos de la persona en la consola.
    print(persona)
    # Muestra un cuadro de diálogo informativo con los datos de la persona seleccionada.
    showinfo(title='Persona seleccionada', message=f'Persona seleccionada {persona}')

# asociar el evento select de la tabla
# Asocia la función mostrar_registro con el evento <<TreeviewSelect>> de la tabla. 
# Este evento se dispara cuando el usuario selecciona una fila en la tabla.
tabla.bind('<<TreeviewSelect>>', mostrar_registro)
 
# publicar la tabla
# Coloca la tabla en la columna 0 y se extiende en todas las direcciones (tk.NSEW para "north-south-east-west") 
# para ocupar el espacio disponible.
tabla.grid(row=0, column=0, sticky=tk.NSEW)
# Inicia el bucle principal de la aplicación, que escucha los eventos del usuario (clics, pulsaciones de teclas, etc.) 
# y actualiza la GUI en consecuencia.
ventana.mainloop()