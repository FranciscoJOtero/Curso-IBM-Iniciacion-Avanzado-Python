#Importar la clase Contacto del fichero Contacto.py
from Contacto import Contacto 

class GestionContactos:
    def __init__(self, archivo = "contactos.txt"):
        self.archivo = archivo
        self.contactos = []
        self.cargar_contactos()

    def cargar_contactos(self):
        """Carga todos los contactos desde el archivo de texto"""
        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                for linea in file:
                    nombre, telefono, email = linea.strip().split(",")
                    # Normalizar el nombre al cargarlo
                    nombre = nombre.strip().lower()  
                    self.contactos.append(Contacto(nombre.strip(), telefono.strip(), email.strip()))
        except FileNotFoundError:
            print("El archivo de contactos no existe. Se creará uno nuevo al guardar.")

    def guardar_contactos(self):
        """Guarda los contactos en el archivo de texto."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as file:
                for contacto in self.contactos:
                    file.write(f"{contacto.nombre}, {contacto.telefono}, {contacto.email} \n")
                print("Contactos guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar los contactos en el archivo: {e}")

    def agregar_contacto(self, nombre, telefono, email):
        """Agregar nuevo contacto a la lista"""
        if not nombre or not telefono or not email:
            raise ValueError("Todos los campos son obligatorios.")
        if not Contacto.validar_email(email):
            raise ValueError("Formato de email incorrecto.")
        if any(c.email == email for c in self.contactos):
            raise ValueError("Ya existe un contacto con este correo electrónico.")
        self.contactos.append(Contacto(nombre,telefono,email))
        print("Contacto agregado con éxito.")

    def mostrar_contactos(self):
        """Muestra todos los contactos que existen en el archivo de texto"""
        if not self.contactos:
            print("No hay contactos registrados.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self, nombre):
        """Buscar un contacto por su nombre"""
        nombre_normalizado = nombre.strip().lower()
        encontrado = False
        for contacto in self.contactos:
            nombre_contacto = contacto.nombre
            if nombre_contacto == nombre_normalizado:
                print(f"Contacto encontrado: {contacto}")
                encontrado = True
                break
        if not encontrado:
            print("No existe ningún contacto con ese nombre.")

    def eliminar_contacto(self, nombre):
        """Eliminar un contacto localizado mediante su nombre"""
        nombre_normalizado = nombre.strip().lower()
        eliminado = False
        contactos_a_mantener = []
        for contacto in self.contactos:
            nombre_contacto = contacto.nombre.strip().lower()
            if nombre_contacto == nombre_normalizado:
                eliminado = True
            else:
                contactos_a_mantener.append(contacto)
        if eliminado:
            self.contactos = contactos_a_mantener
            print(f"El contacto de nombre {nombre} ha sido eliminado con éxito.")
        else:
            print("No existe ningún contacto con ese nombre.")

