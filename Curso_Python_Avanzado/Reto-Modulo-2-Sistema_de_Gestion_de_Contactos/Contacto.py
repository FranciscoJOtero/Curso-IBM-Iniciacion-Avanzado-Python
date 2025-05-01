import re

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre =  nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return (f'Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}')
        
    @staticmethod
    def validar_email(email):
        """Validar el formato del correo electrónico"""
        patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(patron, email)