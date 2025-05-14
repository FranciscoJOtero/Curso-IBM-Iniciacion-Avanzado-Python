# Este código se ha reutilizado de la App llamada zona_fit_db
from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    SELECCIONAR_ID = 'SELECT * FROM cliente WHERE id=%s'
    INSERT = 'INSERT INTO cliente(nombre,apellido,membresia) VALUES(%s,%s,%s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)

            return clientes

        except Exception as e:
            print(f'Ocurrió un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    #Hemos añadido este método nuevo respecto al ejercicio del que corresponde esta plantilla, muy similar al de seleccionar
    #Este decorador se usa para definir métodos que pertenecen a la clase, no a las instancias de la clase. 
    #El primer parámetro de la función es siempre cls (la clase misma), y no una instancia de la clase.
    @classmethod
    #es un método de clase y no necesita que se cree un objeto de la clase ClienteDAO para llamarlo.
    def seleccionar_por_id(cls, id):
        #Se inicializa la variable conexion como None. Esto asegura que la variable exista en el alcance de la función,
        #incluso si ocurre algún error antes de obtener la conexión a la base de datos.
        conexion = None

        try:
            #Obtención de conexión: Llama a la función obtener_conexion de la clase Conexion para obtener una conexión activa a la base de datos. Esto establece la conexión que se utilizará para ejecutar las consultas SQL.
            conexion = Conexion.obtener_conexion()
            #Se crea un cursor a partir de la conexión. Un cursor permite ejecutar consultas SQL y recuperar los resultados.
            #Es el mecanismo que se utiliza para interactuar con la base de datos.
            cursor = conexion.cursor()
            #Se prepara el valor del parámetro id como una tupla. Es importante usar una tupla, incluso si es un solo valor, 
            #porque el método execute espera una secuencia de parámetros. 
            #Esto asegura que el id se pase de manera correcta a la consulta SQL.
            valores = (id,)
            #Ejecutar consulta SQL: Llama a execute en el cursor para ejecutar la consulta SQL, que está definida por cls.SELECCIONAR_ID.
            cursor.execute(cls.SELECCIONAR_ID, valores)
            #Recuperar un solo resultado: Llama a fetchone() para obtener el primer registro de los resultados de la consulta SQL. 
            #Si hay registros que coinciden con el ID proporcionado, se devolverá una tupla con los datos del cliente.
            #Si no hay registros (es decir, no existe un cliente con ese ID), registro será None.
            registro = cursor.fetchone()
            #Crear objeto Cliente: Se crea un objeto Cliente utilizando los datos obtenidos en registro[0], 
            #registro[1], registro[2] y registro[3].Se asume que la consulta SQL devuelve los datos en el 
            #siguiente orden: ID, nombre, apellido y membresía. Si hay más o menos campos, deberás ajustar esto. 
            # Este paso convierte los datos crudos obtenidos de la base de datos en una instancia de la clase Cliente.
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
            #Devolver el cliente: Finalmente, la función devuelve el objeto cliente que ha sido creado 
            #con los datos obtenidos de la base de datos.
            return cliente
        #Manejo de excepciones: Si ocurre algún error en cualquier parte del bloque try, 
        #se captura la excepción y se imprime un mensaje de error. Esto ayuda a depurar y entender 
        #si algo salió mal durante la ejecución de la consulta.
        except Exception as e:
            #Mensaje informando del error
            print(f'Ocurrió un error al seleccionar un cliente por ID: {e}')
        #Bloque finally: Este bloque se ejecuta siempre, independientemente de si hubo un error o no.
        #Se asegura de que la conexión y el cursor se cierren adecuadamente, lo cual es una buena práctica
        # en el manejo de conexiones a bases de datos para evitar posibles fugas de recursos.
        finally:
            #Verifica si la conexión fue abierta antes de intentar cerrarla y liberar los recursos. 
            #Si la conexión no es None, se procede a cerrar el cursor y liberar la conexión.
            if conexion is not None:
                #Cierra el cursor después de usarlo. Es importante liberar este recurso para evitar problemas de rendimiento.
                cursor.close()
                #lama al método liberar_conexion de la clase Conexion, que se encarga de liberar la conexión a la base de datos.
                #Esto garantiza que la conexión sea devuelta al pool de conexiones o cerrada adecuadamente.
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERT, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar el cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar el cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
           conexion = Conexion.obtener_conexion()
           cursor = conexion.cursor()
           valores = (cliente.id,)
           cursor.execute(cls.ELIMINAR, valores)
           conexion.commit()
           return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)