#Este fichero esta sin terminar, también se añadiran comentarios explicativos del código próximamente
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from cliente_dao import ClienteDAO

class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('1200x750')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        #Aplicar estilos
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure(self, background=App.COLOR_VENTANA, foreground='white', fieldbackground='black')

    def configurar_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit GYM Franker', font=('Arial', 30), background=App.COLOR_VENTANA, foreground='white', )
        etiqueta.grid(row=0, column=0, columnspan=2, pady=40)

    def mostrar_formulario(self):
        self.frame_formu = ttk.Frame()
        #nombre
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
        #publicar frame del formulario
        self.frame_formu.grid(row=1,column=0)

    def mostrar_tabla(self):
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
        
        #publicar la tabla
        self.tabla.grid(row=0, column=0)
        #mostrar frame de tabla
        self.frame_table.grid(row=1, column=1, padx=20)
        
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
    
    def validar_cliente(self):
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

    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False
        
    def guardar_cliente():
        #PRÓXIMAMENTE
        pass

    def eliminar_cliente(self):
        #PRÓXIMAMENTE
        pass

    def limpiar(self):
        #PRÓXIMAMENTE
        pass

# ---------------------------------------- PRUEBAS -------------------------------------------------------------------------------
if __name__ == '__main__':
    app = App()
    app.mainloop()