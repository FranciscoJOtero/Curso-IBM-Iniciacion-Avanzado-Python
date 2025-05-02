#Importar el módulo "re" que se utiliza para trabajar con expresiones regulares
import re

#Definir la clase Contacto
class Contacto:
    #Constructor de la clase, se llama automaticamente cuando se crea un nuevo objeto de la clase Contacto
    def __init__(self, nombre, telefono, email):
        #Self es una referencia al objeto actual
        #nombre, telefono y email son los parametros que se pasan al constructor para inicializar los atributos del objeto.
        self.nombre =  nombre
        self.telefono = telefono
        self.email = email

    #Definir el metodo __str__
    #Metodo especial que se llama cuando se intenta convertir un objeto a una cadena.
    def __str__(self):
        return (f'Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}')
    
    #decorador que indica que este metodo es un metodo estatico
    @staticmethod
    #nombre del método
    def validar_email(email):
        """Validar el formato del correo electrónico"""
        #Expresion regular para formato de correo electronico basico
        patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        #Metodo re.match() devuelve un objeto de coincidencia si coincidencia tiene exito,
        #en caso contrario devuelve NONE
        return re.match(patron, email)