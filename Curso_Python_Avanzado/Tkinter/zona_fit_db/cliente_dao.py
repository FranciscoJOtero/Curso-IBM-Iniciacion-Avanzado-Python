#Importaciones
#Importa la clase Conexion, que gestiona el pool de conexiones.
from conexion import Conexion
#Importa Cliente, el modelo que representa a un cliente con atributos como id, nombre, etc.
from cliente import Cliente
#Clase que agrupa métodos para trabajar con la tabla cliente.
class ClienteDAO:
    #Consultas SQL reutilizables:
    #SELECCIONAR: obtiene todos los registros.
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    #INSERT: inserta un nuevo cliente
    INSERT = 'INSERT INTO cliente(nombre,apellido,membresia) VALUES(%s,%s,%s)'
    #ACTUALIZAR: modifica un cliente ya existente.
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    #ELIMINAR: elimina un cliente según su id.
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'
    #Define un método de clase
    @classmethod
    #Método de clase que devuelve una lista de objetos Cliente a partir de los registros de la base de datos.
    def seleccionar(cls):
        conexion = None
        try:
            #Abre una conexión.
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            #Ejecuta la consulta SELECT.
            cursor.execute(cls.SELECCIONAR)
            #Recupera todos los registros 
            registros = cursor.fetchall()
            #Convierte cada fila en un objeto Cliente.
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            #Devuelve la lista de clientes.
            return clientes
        #En caso de que ocurra algún error al ejecutar la sentencia SQL
        except Exception as e:
            #Mensaje de aviso con el tipo de error que se produzca (e)
            print(f'Ocurrió un error al seleccionar clientes: {e}')
        #bloque finally
        finally:
            #Cierra cursor y libera conexión, pase lo que pase.
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    #Define un método de clase
    @classmethod
    #Método de clase para inserta un nuevo cliente.
    def insertar(cls, cliente):
        conexion = None
        #bloque try muy similar al del anterior método
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            #Usamos una tupla con los valores del objeto.
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            #Ejecutar la consulta
            cursor.execute(cls.INSERT, valores)
            #Confirmar y guardar cambios
            conexion.commit()
            #retornar cuantas filas fueron insertadas 
            return cursor.rowcount
        #esta parte tambien es similar a la del método anterior, y será tambien similar en el resto de métodos
        except Exception as e:
            print(f'Ocurrió un error al insertar el cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    #Define un método de clase
    @classmethod
    #Método de clase que actualiza un cliente ya existente según su id. 
    def actualizar(cls, cliente):
        conexion = None
        try:
            #Los nuevos datos + el id del cliente determinan qué fila actualizar.
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
    #Define un método de clase
    @classmethod
    #Método de clase para elimina un cliente según su id.
    def eliminar(cls, cliente):
        conexion = None
        try:
           conexion = Conexion.obtener_conexion()
           cursor = conexion.cursor()
           valores = (cliente.id,)
           #Ejecuta la eliminación y retorna cuántas filas se borraron.
           cursor.execute(cls.ELIMINAR, valores)
           conexion.commit()
           return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

#---------------------  PRUEBAS -------------------------------------------------------------------------------------------------------
# if __name__ == '__main__':

    #INSERTAR
    # cliente1 = Cliente(nombre='Francisco', apellido='Otero', membresia=1000)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    #ACTUALIZAR
    # cliente_actualizar = Cliente(6,'Alexa', 'Tellez', 400)
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')

    #ELIMINAR
    # cliente_eliminar = Cliente(id=6)
    # clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    # print(f'Clientes eliminados: {clientes_eliminados}')

    #SELECCIONAR
    # clientes = ClienteDAO.seleccionar()
    # for cliente in clientes:
    #     print(cliente)