# Proximamente se añadirán comentarios explicando el código
#Definir la clase Cliente(POO), plantilla para crear objetos.
class Cliente:
    #Método constructor de la clase Cliente, se ejecuta automáticamente cuando se crea una nueva instancia de la clase
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        #Asignar los valores de los parámetros a los atributos del obejto de la clase Cliente
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia
    #Método especial __str__ que indica como se represntará el objeto como cadena
    def __str__(self):
        return (f'ID: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresía: {self.membresia}')
    