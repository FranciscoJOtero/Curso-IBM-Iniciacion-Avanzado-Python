# Este código se ha reutilizado de la App llamada zona_fit_db
from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
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