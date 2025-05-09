# Importar elementos del paquete mysql.connector
#pooling para usar pols de conexiones a MySQL
from mysql.connector import pooling
#Error para capturar excepciones especificas de errores MySQL
from mysql.connector import Error
#Define una clase llamada Conexion, encargada de gestionar el acceso a la base de datos.
class Conexion:
    #Nombre de la base de datos a la que se conectará.
    DATABASE = 'zona_fit_db'
    #Nombre de usuario para acceder a la base de datos.
    USERNAME = 'root'
    #Contraseña asociada al usuario. En este caso, está vacía.
    PASSWORD = ''
    #Puerto en el que corre el servicio de MySQL (por defecto es 3306).
    DB_PORT = '3306'
    #Dirección del servidor de base de datos. localhost indica que está en el mismo equipo.
    HOST = 'localhost'
    #Cantidad de conexiones que tendrá el pool.
    POLL_SIZE = 5
    #Nombre identificador del pool de conexiones.
    POOL_NAME = 'zona_fit_pool'
    #Inicializa el atributo de clase pool. Al principio, no hay ningún pool creado.
    pool = None
    #Define un método de clase
    @classmethod
    #metodo de clase que se ocupa de obtener el pool de conexiones
    def obtener_pool(cls):
        #Condicional. Si aún no se ha creado el pool, se entra al bloque try.
        if cls.pool is None:
            #bloque try. Se intenta crear un pool de conexiones y se guarda como cls.pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POLL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                #Después de crearlo, se devuelve el pool para ser usado.
                return cls.pool
            #Si ocurre algún error al crear el pool, se captura e imprime el mensaje.
            except Error as e:
                print(f'Ocurrió un error al obtener pool: {e}')
        #Condiconal. Si el pool ya existe, simplemente se retorna el existente.
        else:
            return cls.pool
    #Define un método de clase
    @classmethod
    #Este método obtiene el pool (creándolo si es necesario) y devuelve una conexión libre del pool, lista para ser usada
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    #Define un método de clase
    @classmethod
    #Este método cierra la conexión, lo que en un pool realmente la devuelve al pool para su reutilización (no la destruye).
    def liberar_conexion(cls, conexion):
        conexion.close()

#---------------------  PRUEBAS -------------------------------------------------------------------------------------------------------
#Este es un bloque condicional especial en Python.
#Sirve para que este código solo se ejecute si el archivo se ejecuta directamente (por ejemplo, con python mi_archivo.py) y no si se importa
# como módulo desde otro archivo.
#Es muy útil para pruebas o demostraciones.
# if __name__ == '__main__':
      #Llama al método obtener_pool() de la clase Conexion.
      # Si el pool ya existe, lo devuelve.
      # Si no, lo crea con los datos de configuración.
      # Se guarda el objeto MySQLConnectionPool en la variable pool.
#     pool = Conexion.obtener_pool()
      #Imprime el objeto pool para verificar que se ha creado correctamente.
#     print(pool)
      #Solicita una conexión del pool. Es decir, una conexión libre (disponible) para usarla.
      #Se guarda en la variable conexion1.
#     conexion1 = pool.get_connection()
#     print(conexion1)
      #Llama al método liberar_conexion() de la clase Conexion, que simplemente ejecuta conexion1.close().
      #Como es una conexión del pool, al cerrarla vuelve a estar disponible para ser reutilizada por otra parte del programa.
#     Conexion.liberar_conexion(conexion1)
#     print(f'se ha liberado la conexion del objeto {conexion1}')


