# Proximamente se añadirán comentarios explicando el código
from cliente_dao import ClienteDAO
from cliente import Cliente

print('--- Clientes Zona Fit ---')

opcion = None
while opcion != 5:
    print(f'''\n Menú:
          1. Listar Clientes
          2. Agregar nuevo cliente
          3. Modificar cliente
          4. Eliminar cliente
          5. Salir''')
    try:
        opcion = int(input('Escriba su opción (1-5): '))
    except ValueError:
        print('Opción inválida, debe elejir entre 1 y 5.')

    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:
        nombre_var = input('Escriba el nombre del nuevo cliente: ')
        apellido_var = input('Escriba el apellido del nuevo cliente: ')
        membresia_var = input('Introduzca la membresía del nuevo cliente: ')
        cliente = Cliente(nombre=nombre_var,apellido=apellido_var,membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}')
    elif opcion == 3:
        id_cliente_var = int(input('Introduzca el ID del cliente que desea modificar: '))
        nombre_var = input('Escriba el nuevo nombre del cliente: ')
        apellido_var = input('Escriba el nuevo apellido del cliente: ')
        membresia_var = input('Introduzca la nueva membresía del cliente: ')
        cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'Clientes actualizados: {clientes_actualizados}')
    elif opcion == 4:
        id_cliente_var = int(input('Introduzca el ID del cliente que desea eliminar: '))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Clientes eliminados: {clientes_eliminados}')

    elif opcion == 5:
        print('Gracias por utilizar la App, vuelvan pronto!!')
    else:
        print('Opción no válida, elija otra entre 1 y 5 por favor.')