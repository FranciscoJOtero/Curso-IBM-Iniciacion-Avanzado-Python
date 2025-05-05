#Este código define una clase para representar productos con nombre, cantidad, precio y categoría. 
#También incluye un método para mostrar esos datos de forma clara cuando se imprime el objeto.

#Definir la clase Prdocuto
class Producto:
    #Definir el constructor de la clase con los parámetros que recibe
    def __init__(self, nombre, cantidad, precio, categoria):
        #Asignar el valor de los parámetros al atributo del objeto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio =  precio
        self.categoria = categoria

    #método para devolver una representación en texto del obejto cuando se imprime "print()"
    def __str__(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}, Categoria: {self.categoria}"