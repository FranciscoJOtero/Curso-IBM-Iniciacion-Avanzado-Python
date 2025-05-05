#importar la clase Producto definida en el archivo producto.py
from producto import Producto
#importar el conector MySQL par Python, necesario para trabajar con bases de datos
import mysql.connector

#Definicion de la clase GestionInventario
class GestionInventario:
    #método constructor
    def __init__(self, host="localhost", user= "root", password="", database="inventario_db"):
        #asignar los parametros a los atributos del objeto
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None #se inicializa con None y luego se usará para guardar la conexión activa
    
    #deficinición de la clase conectar, sera la funcion encargada de conectar a la BBDD creada "inventario_db"
    #La base de datos se ha creado en PhpMyAdmin integrado en el servidor XAMP
    def conectar(self):
        #bloque try para controlar errores en la conexión
        try:
            #establecer la conexion a la BBDD usando los atributos proporcionados en el constructor
            self.conexion = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            #Condicional para verificar si la conexión es correcta
            if self.conexion.is_connected():
                #mensaje de Ok si todo fue correcto
                print("Conexion a la base de datos existosa.")
        #en caso de que se produzca algun tipo de error
        except mysql.connector.Error as e:
                #mostrará un mensaje con el tipo de error (e)
                print("Error al conectar a la base de datos: {e}")

    #definición del método desconectar, que utilizaremos para la desconexión de la BBDD
    def desconectar(self):
        #Condicional en el cual si la conexión esta abierta 
        if self.conexion:
            #desconectará la conexión con la BBDD
            self.conexion.close()
            #mostrará mensaje para informar de que se ha cerrado la conexión.
            print("Conexión a la base de datos cerrada.")

    #definición del método agregar_producto, el cual recibirá un objetos de la clase Producto y lo guardará en la base de datos inventario_db
    def agregar_producto(self, producto):
        #bloque try para controlar errores
        try:
            #llamada al método conectar
            self.conectar()
            #creamos un cursor para ejecutar sentencias SQL
            cursor = self.conexion.cursor()
            #Consulta SQL para insertar un porducto en la BBDD inventario_db, en la tabla productos
            sql = "INSERT INTO productos (nombre, cantidad, precio, categoria) VALUES (%s, %s, %s, %s)"
            #llenar los valores con los atributos del objeto Producto
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            #ejecutar la sentencia SQL e inserta el producto en la tabla de la BBDD
            cursor.execute(sql, valores)
            #Guardar los cambios con commit()
            self.conexion.commit()
            #mensaje para informar de que todo fue correcto
            print("Producto agregado con éxito.")

        #Si ocurre algun error
        except mysql.connector.Error as e:
            #deshace cualquier cambio pendiente
            self.conexion.rollback()
            #y muestra un mensaje de error
            print(f"Error al agregar el producto: {e}")

        #bloque finally 
        finally:
            #para cerrar siempre la conexión con la base de datos
            self.desconectar()

    #Definición del método mostrar_productos, el cual mostrará todos los productos que existen en la BBDD
    def mostrar_productos(self):
        #bloque try para controlar errores
        try:
            #llamada al método conectar() para la conexión con la BBDD
            self.conectar()
            #crear cursor para ejecutar sentencias SQL
            cursor = self.conexion.cursor()
            #ejecutamos la sentencia SQL, es una  consulta la cual selecciona todo el contenido de la tabla productos 
            cursor.execute("SELECT * FROM productos")
            #
            productos = cursor.fetchall()
            #Condicional if, si ha productos
            if productos:
                #bucle for para recorrer todos los productos
                for prodcuto in productos:
                    #imprimir cada producto en cada vuelta del bucle for
                    print(prodcuto)
            #Si no existen productos
            else:
                #mensaje informando de que no ha productos
                print("No hay productos registrados.")

        #en caso de errores 
        except mysql.connector.Error as e:
                #mensaje con información acerca del tipo de error (e)
                print(f"Error al mostrar los productos: {e}")
        #bloque finally para finalizar la conexión
        finally:
            self.desconectar()

    #Definición del método buscar_producto, el cual buscará un producto por su nombre
    def buscar_producto(self, nombre):
        #bloque try
        try:
            #llamada al método conectar
            self.conectar()
            #crear cursor para ejecutar sentencias SQL
            cursor = self.conexion.cursor()
            #Sentencia SQL, selecciona todo de la tabla productos donde el nombre coincida con el nombre introducido por el usuario
            sql = "SELECT * FROM productos WHERE nombre = %s"
            #ejecutar la sentencia SQL
            cursor.execute(sql, (nombre,))
            #Guardar en una variable 
            producto = cursor.fetchone()
            #Si encuentra coincidencias con algun producto
            if producto:
                #Mostrará mensaje de producto encontrado
                print("\n --- Producto Encontrado ---")
                #imprimir el producto que buscaba el usuario
                print(f"{producto} \n")
            #En caso de no encontrar coincidencias
            else:
                #mensaje informando de que no se ha encontrado ningún producto
                print("No existe ningún producto con ese nombre.")

        #bloque except para controlar errores de conexión
        except mysql.connector.Error as e:
            #mensaje con el tipo de error
            print(f"Error al buscar el producto: {e}")

        #bloque finally para finalizar la conexión
        finally:
            self.desconectar()

    #Definición del método actualizar_producto, el cual actualizará la información de cualquier producto de la tabla
    def actualizar_producto(self, nombre, cantidad, precio, categoria):
        #bloque try para el control de errores
        try:
            #llamada al método conectar()
            self.conectar()
            #crear cursor para ejecutar sentencias SQL
            cursor = self.conexion.cursor()
            #Sentencia SQL para actualizar cantidad, precio y categoría de un prodcuto el cual el nombre coincida con el que introduzca el usuario
            sql = "UPDATE productos SET cantidad = %s, precio = %s, categoria = %s WHERE nombre = %s"
            #Llenar los valores con los atributos actualizados del objeto
            valores = (cantidad, precio, categoria, nombre)
            #ejecutar la sentencia SQL
            cursor.execute(sql, valores)
            #guardar cambios
            self.conexion.commit()

            #rowcount devuelve el número de filas afectadas por la última operación SQL ejecutada (ya sea INSERT, UPDATE, DELETE, etc.).
            #rowcount > 0 significa que sí se encontró y modificó/eliminó al menos un producto.
            if cursor.rowcount > 0:
                #mensaje de confirmación
                print("Producto actualizado con éxito. ")
            #en caso contrario
            else:
                #mensaje de que no existen coincidencias
                print("No existe ningún producto con ese nombre. ")

        #bloque except para verificar errores de conexión
        except mysql.connector.Error as e:
            #deshacer cualquier cambio pendiente
            self.conexion.rollback()
            #informar del tipo de error que se produce
            print(f"Error al actualizar el producto: {e}")

        #bloque finally para desconectar de la BBDD
        finally:
            self.desconectar()

    #definición del método eliminar_producto, para borrar definitivamente un producto de la tabla productos de la base de datos
    def eliminar_producto(self, nombre):
        #bloque try para el control de errores
        try:
            #llamada al método conectar
            self.conectar()
            #crear cursor para ejecutar sentencias SQL
            cursor = self.conexion.cursor()
            #sentencia SQL para eliminar un producto el cual coincida con el nombre que introduzca el usuario
            sql = "DELETE FROM productos WHERE nombre = %s"
            #ejecutar la sentencia SQL
            cursor.execute(sql, (nombre,))
            #guardar cambios
            self.conexion.commit()
            
            #rowcount devuelve el número de filas afectadas por la última operación SQL ejecutada (ya sea INSERT, UPDATE, DELETE, etc.).
            #rowcount > 0 significa que sí se encontró y modificó/eliminó al menos un producto.
            if cursor.rowcount > 0:
                #mensaje de confirmación
                print("Producto eliminado correctamente. ")
            #en caso contrario
            else:
                #mensaje informando de que no hay coincidencias
                print("No existe ningún producto con ese nombre. ")

        #bloque except para errores de conexión
        except mysql.connector.Error as e:
            #deshacer cambios pendientes
            self.conexion.rollback()
            #mensjae de información con el tipo de error
            print(f"Error al eliminar el producto: {e}")

        #bloque finally para desconectar de la BBDD
        finally:
            self.desconectar()