#Importar la clase Contacto del fichero Contacto.py
from Contacto import Contacto 

#Definir la clase GestionContactos
class GestionContactos:
    #Constructor de la clase
    #le pasamos como parametro (archivo) el nombre del fichero donde se guardarán los contactos
    def __init__(self, archivo = "contactos.txt"):
        self.archivo = archivo #Almacena el nombre del archivo
        #lista para almacenar objetos de la clase Contacto
        self.contactos = []
        #llamada al metodo cargar_contactos() para cargar los contactos desde el archivo
        self.cargar_contactos()

    #Definir metodo cargar_contactos()
    def cargar_contactos(self):
        """Carga todos los contactos desde el archivo de texto"""
        #bloque try para controlar errores en caso de que el archivo no exista
        try:
            #abrir el archivo en modo lectura, declaramos la codificación para evitar errores, en nuestro caso utf-8.
            with open(self.archivo, "r", encoding="utf-8") as file:
                #bucle for para recorrer linea a linea el archivo que contiene los contactos
                for linea in file:
                    #strip() elimina los espacios en blanco al principio y al final de la linea.
                    #split() divide linea en una lista de tres cadenas separadas por comas.
                    nombre, telefono, email = linea.strip().split(",")
                    # Normalizar el nombre al cargarlo, eliminando espacios y convirtiendo a minusculas
                    nombre = nombre.strip().lower()
                    #Crear un nuevo objeto de la clase Contacto con los datos de la linea y lo añade a la lista self.contactos
                    self.contactos.append(Contacto(nombre.strip(), telefono.strip(), email.strip()))
        #en caso de que el archivo no exista mostrará mensaje de aviso.
        except FileNotFoundError:
            print("El archivo de contactos no existe. Se creará uno nuevo al guardar.")

    #Definir el metodo guardar_contactos
    def guardar_contactos(self):
        """Guarda los contactos en el archivo de texto."""
        #bloque try para controlar errores
        try:
            #abrir el archivo en modo escritura
            with open(self.archivo, "w", encoding="utf-8") as file:
                #recorrer la lista self.contactos 
                for contacto in self.contactos:
                    #a cada vuelta de bucle for, escribira en el archivo todos los objetos creados de la clase Contacto
                    file.write(f"{contacto.nombre}, {contacto.telefono}, {contacto.email} \n")
                #mensaje de info para avisar de que todo OK
                print("Contactos guardados correctamente.")
        #En caso de que ocurra algun error.
        except Exception as e:
            #mensaje de aviso para el usuario
            print(f"Error al guardar los contactos en el archivo: {e}")
    #Definir la clase agregar_contacto con sus parametros de entrada
    def agregar_contacto(self, nombre, telefono, email):
        """Agregar nuevo contacto a la lista"""
        #Si alguno de los atributos esta vacio mostrara mensaje de error
        if not nombre or not telefono or not email:
            #mensaje de aviso
            raise ValueError("Todos los campos son obligatorios.")
        #Si el formato del correo electronico no es correcto, mostrara mensaje de aviso
        if not Contacto.validar_email(email):
            #mensaje de aviso
            raise ValueError("Formato de email incorrecto.")
        #Si el correo electronico existe mostrara mensaje de alerta
        if any(c.email == email for c in self.contactos):
            #mensaje de aviso
            raise ValueError("Ya existe un contacto con este correo electrónico.")
        
        #Si todo es correcto, crea un nuevo objeto de la clase Contacto con los datos facilitados por el usuario
        self.contactos.append(Contacto(nombre,telefono,email))
        #mensaje para informar que todo OK.
        print("Contacto agregado con éxito.")

    #Definir el metodo mostrar_contacto
    def mostrar_contactos(self):
        """Muestra todos los contactos que existen en el archivo de texto"""
        #En caso de que no haya contactos
        if not self.contactos:
            #mensaje para infomar
            print("No hay contactos registrados.")
        #En caso contrario
        else:
            #Bucle para recorrer la lista de contactos
            for contacto in self.contactos:
                #En cada vuelta muestra un contacto
                print(contacto)

    #Definir el metodo buscar_contacto
    def buscar_contacto(self, nombre):
        """Buscar un contacto por su nombre"""
        #Guardamos el nombre nomralizado en una variable
        nombre_normalizado = nombre.strip().lower()
        #inicializamos una variable con valor false
        encontrado = False
        #bucle para recorrer la lista de contactos
        for contacto in self.contactos:
            nombre_contacto = contacto.nombre
            #Si hay coincidencia en los nombres, el que introduce el usuario, y de los existentes ne la lista
            if nombre_contacto == nombre_normalizado:
                #Mostrar en pantalla el contacto y el nombre del mismo
                print(f"Contacto encontrado: {contacto}")
                #cambiar el valor a true de la variable
                encontrado = True
                #detener el bucle
                break
        #Si tras recorrer la lista no hay coincidencia
        if not encontrado:
            #mensaje para informar al usuario
            print("No existe ningún contacto con ese nombre.")

    #definir metodo eliminar_contacto
    def eliminar_contacto(self, nombre):
        """Eliminar un contacto localizado mediante su nombre"""
        #Normalizar para evitar problemas de espacios, mayusculas o minusculas
        nombre_normalizado = nombre.strip().lower()
        #bandera para saber si se encontro y se elimino el usuario
        eliminado = False
        #nueva lista que guardará todos los contactos que no deben ser borrados
        contactos_a_mantener = []
        #bucle for para recorrer la lista
        for contacto in self.contactos:
            #Para cada contacto se normaliza su nombre
            nombre_contacto = contacto.nombre.strip().lower()
            #Si hay coindicencia se marca como eliminado y no se guarda en la lista nueva
            if nombre_contacto == nombre_normalizado:
                eliminado = True
            #Si no hay coincidencia
            else:
                #Se añade a contactos_a_mantener
                contactos_a_mantener.append(contacto)
        #Si se encontro y elimino el contacto
        if eliminado:
            #Se actualiza la lista de contactos
            self.contactos = contactos_a_mantener
            #mensaje de que todo OK
            print(f"El contacto de nombre {nombre} ha sido eliminado con éxito.")
        #En caso contrario
        else:
            #Mensaje para informar de que no hay contactos que coincidan
            print("No existe ningún contacto con ese nombre.")

