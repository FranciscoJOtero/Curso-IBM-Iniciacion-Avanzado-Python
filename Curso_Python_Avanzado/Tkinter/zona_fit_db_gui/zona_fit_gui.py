#Este fichero esta sin terminar, también se añadiran comentarios explicativos del código próximamente
#Este código crea una aplicación gráfica (GUI) en Python usando Tkinter para gestionar una base de datos 
#de clientes de un gimnasio llamado Zona Fit. El mismo ejercicio que zona_fit_db pero añadiendo interfaz gráfica con Tkinter

#Importaciones
#tkinter: módulo base de interfaces gráficas en Python.
import tkinter as tk
#ttk: módulo de estilos mejorados para widgets de Tkinter.
from tkinter import ttk
#messagebox: para mostrar mensajes emergentes de error o información.
from tkinter.messagebox import showerror, showinfo
#Cliente y ClienteDAO: clases personalizadas importadas de otros archivos. 
#Cliente representa un cliente individual, y ClienteDAO permite interactuar con la base de datos (DAO = Data Access Object)
from cliente import Cliente
from cliente_dao import ClienteDAO

#Clase principal, crea una subclase de tk.TK, que será la ventana principal
class App(tk.Tk):
    #define un color base para el fondo de la ventana
    COLOR_VENTANA = '#1d2d44'

    #Método constructor de la clase
    def __init__(self):
        #Llama al constructor de la clase base (Tk).
        super().__init__()
        #atributo de clase inicializado a None
        self.id_cliente = None
        #métodos para configurar y mostrar la interfaz gráfica.
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    #metodo para la configuración de la ventana principal
    def configurar_ventana(self):
        #tamaño inicial de la ventana
        self.geometry('1200x750')
        #titulo de la ventana
        self.title('Zona Fit App')
        #configurar el color de fondo de la venta principal
        self.configure(background=App.COLOR_VENTANA)
        #Aplicar estilos. Configura el aspecto inicial de la ventana y los estilos visuales con ttk.Style.
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure(self, background=App.COLOR_VENTANA, foreground='white', fieldbackground='black')

    #método para confiruar el grid
    def configurar_grid(self):
        #Hace que las columnas 0 y 1 se ajusten al tamaño de la ventana.
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    #método para mostrar el titulo
    def mostrar_titulo(self):
        #Crear y mostrar una etiqueta con el título del programa en la primera fila.
        etiqueta = ttk.Label(self, text='Zona Fit GYM Franker', font=('Arial', 30), background=App.COLOR_VENTANA, foreground='white', )
        etiqueta.grid(row=0, column=0, columnspan=2, pady=40)

    #método para mostrar el formulario
    def mostrar_formulario(self):
        #Crear un Frame para agrupar los campos.
        self.frame_formu = ttk.Frame()
        #nombre
        #Muestra campos para nombre, apellido y membresía usando ttk.Entry.
        nombre_l = ttk.Label(self.frame_formu, text='Nombre: ')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_formu)
        self.nombre_t.grid(row=0, column=1)
        #apellido
        apellido_l = ttk.Label(self.frame_formu, text='Apellido: ')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_formu)
        self.apellido_t.grid(row=1, column=1)
        #membresía
        membresia_l = ttk.Label(self.frame_formu, text='Membresía: ')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_formu)
        self.membresia_t.grid(row=2, column=1)
        #publicar frame del formulario. Posicionar el Frame en la ventana.
        self.frame_formu.grid(row=1,column=0)

    #método para cargar la tabla de clientes
    def cargar_tabla(self):
        #crear un frame para mostrar la tabla
        self.frame_table = ttk.Frame(self)
        #definir estilos de la tabla
        self.estilos.configure('Treeview', background='black', foreground='white', fieldbackground='black', rowheight=20)
        #definir columnas
        columnas = ('Id', 'Nombre', 'Apellido', 'Membresia')
        #crera objeto tabla
        self.tabla = ttk.Treeview(self.frame_table, columns=columnas, show='headings')
        #Agregar las cabeceras de la tabla
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)
        #definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)
        #cargar datos de la BBDD
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            #print(cliente)
            self.tabla.insert(parent='', index=tk.END, values=(cliente.id, cliente.nombre, cliente.apellido, cliente.membresia))

        #agregar Scrollbar
        scrollbar = ttk.Scrollbar(self.frame_table, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        #publicar scrollbar
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        #Asociar evento Select
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)
        
        #publicar la tabla
        self.tabla.grid(row=0, column=0)
        #mostrar frame de tabla
        self.frame_table.grid(row=1, column=1, padx=20)
        
    #método para mostrar los botones del formulario
    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        #CREAR BOTONES
        #boton de agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar', command=self.validar_cliente)
        #publicar boton
        agregar_boton.grid(row=0, column=0, padx=40)
        #boton de eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar', command=self.eliminar_cliente)
        #publicar boton
        eliminar_boton.grid(row=0, column=1, padx=40)
        #boton de limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar', command=self.limpiar)
        #publicar boton
        limpiar_boton.grid(row=0, column=2, padx=40)

        #aplicar estilo a los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        #pulbicar frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=50)
    
    #método para validar clientes
    def validar_cliente(self):
        #Verifica que todos los campos estén llenos y que la membresía sea numérica.
        if(self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atención', message='El valor de membresía no es numérico')
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus_set()
        else:
            showerror(title='Atención', message='Debe rellenar todos los campos del formulario')
            self.nombre_t.focus_set()

    #método para validar que la membresía sea un número
    def validar_membresia(self):
        #Intenta convertir la membresía a entero. Si no puede, devuelve False.
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False
        
    #método que se va encargar de guardar clientes y actualizarlos
    def guardar_cliente(self):
        #Recuperar los valores de las cajas de texto
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        #Validar id_cliente
        #Si id_cliente es None, crea un nuevo cliente.
        if self.id_cliente is None:
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.insertar(cliente)
            showinfo(title='Agregar cliente', message='Cliente agregado')
        #Si no, actualiza uno existente.
        else: #Actualizar
            cliente = Cliente(self.id_cliente, nombre, apellido, membresia)
            ClienteDAO.actualizar(cliente)
            showinfo(title='Actualizar cliente', message='Cliente actualizado...')

        #Mostrar de nuevo los datos y limpiar el formulario
        self.recargar_datos()

    #método para cargar cliente en el formulario al seleccionarlo en la tabla
    def cargar_cliente(self, event): #Se ejecuta al seleccionar una fila en la tabla.
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values']
        #recuperar cada valor
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]
        #Antes de cargar, limpiar formulario
        self.limpiar_formulario()
        #Cargar formulario
        self.nombre_t.insert(0, nombre)
        self.apellido_t.insert(0, apellido)
        self.membresia_t.insert(0, membresia)

    #método para recargar los datos de la tabla y limpiar el formulario
    def recargar_datos(self):
        #Volver a cargar los datos en la tabla
        self.cargar_tabla()
        #limpiar datos
        self.limpiar()

    #método para eliminar un cliente
    def eliminar_cliente(self):
        #Verifica si se ha seleccionado un cliente y lo elimina de la base de datos.
        if self.id_cliente is None:
            showerror(title='Atención!!', message='Debes seleccionar un cliente para eliminar.')
        else:
            cliente = Cliente(id=self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title='Cliente Eliminado', message='Cliente eliminado...')
            self.recargar_datos()

    #método para limpiar formulario e inicializar de nuevo el id_cliente a None
    def limpiar(self):
        self.limpiar_formulario()
        self.id_cliente = None

    #método para limpiar los campos del formulario
    def limpiar_formulario(self):
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)

#Punto de entrada
if __name__ == '__main__':
    #Crear una instancia de App.
    app = App()
    #Llamar a mainloop() para iniciar la aplicación y que responda a eventos.
    app.mainloop()