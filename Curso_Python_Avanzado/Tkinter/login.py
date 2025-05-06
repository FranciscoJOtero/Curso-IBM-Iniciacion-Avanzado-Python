"""Este script crea una interfaz gráfica de login usando tkinter, 
   que es una librería estándar de Python para interfaces gráficas."""

# importar la libreria tk
import tkinter as tk
# submódulo de tkinter con widgets con estilo moderno
from tkinter import ttk
# funciones para mostrar mensajes emergentes (pop-ups)
from tkinter.messagebox import showerror, showinfo

# crear la ventana principal
ventana = tk.Tk()
# tamaño inicial de la ventana
ventana.geometry('600x400')
# título de la ventana
ventana.title('Login')
# asignar el fondo de color azul oscuro con colores hexadecimales
ventana.configure(background='#1d2d44')

# Configurar el sistema de rejilla (grid) de la ventana
# asignar el peso al grid de la ventana que permite que los widgets se expandan proporcionalmente si se redimensiona
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# crear estilos
#crear un obejto de estilo (Style)
estilos = ttk.Style()
# asignar el tema "clam", que es más personalizable que el de por defecto
estilos.theme_use('clam')
# aplicar fondo oscuro y texto blanco a la ventana
estilos.configure(ventana, background='#1d2d44', foreground='white', fieldbackground='black')
# aplicar estilos a los botones, en este caso color de fondo
estilos.configure('TButton', background='#005f73')
# aplicar estilos esta vez solo cuando el boton esta activo, es decir, al pasar el ratón por encima del botón
estilos.map('TButton', background=[('active', '#0a9396')])

# Crear un Frame, es una especie de contenedor para los widgets
# crear el contenedor
frame = ttk.Frame(ventana)
# asignar peso diferente a las columnas para controlar el ancho de etiquetas y cajas de texto
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# título del formulario
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
# Ocupa dos columnas, para conseguir centrar el título
etiqueta.grid(row=0, column=0, columnspan=2)

# Usuario
# crear etiqueta para el nombre de usuario dentro del formulario
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
# crear etiqueta alineada a la izquierda (sticky) y añadiendo márgenes (padx y pady)
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

# caja de texto para escribir el nombre de usuario alineada a la derecha (sticky) 
usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# Password
# crear etiqueta para la contraseña dentro del formulario
password_etiqueta = ttk.Label(frame, text='Contraseña: ')
# etiqueta alineada a la izquierda (sticky) y añadiendo márgenes (padx y pady)
password_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

# caja de texto para escribir la contraseña alineada a la derecha (sticky), con show ocultamos lo que se escribe dentro
password_caja_texto = ttk.Entry(frame,show='*')
password_caja_texto.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# Botón
# crear un botón para enviar el formulario 
login_boton = ttk.Button(frame, text='Enviar')
# se expande dos columnas (columnspan)
login_boton.grid(row=3, column=0 ,columnspan=2, padx=5, pady=5)

# función para validar el login, la cual recibe un evento (event) como parámetro
def validar(event):
    # variables para almacenar el contenido de las cajas de texto de usuario y contraseña
    usuario = usuario_caja_texto.get()
    password = password_caja_texto.get()

    # Si los datos introducidos coinciden con los de este condicional
    if usuario == 'root' and password == 'admin':
        # la aplicación mostrará un pop-up de información indicando que los datos son correctos
        showinfo(title='Login', message='Datos Correctos!!')
    # en caso contrario
    else:
        # el pop-up será de error para indicar que los datos son incorrectos
        showerror(title='Login', message='Datos Incorrectos...')

#Asociar eventos, en este caso para el botón de Enviar
login_boton.bind('<Return>', validar) #captura el evento de la tecla Enter
login_boton.bind('<Button-1>', validar) #captura el evento del click izquierdo del ratón

# Mostrar el frame en la ventana, lo situa en la posición (0,0)
frame.grid(row=0, column=0)

# Inicia el bucle principal de la ventana. A partir de aquí, espera acciones del usuario (eventos).
ventana.mainloop()