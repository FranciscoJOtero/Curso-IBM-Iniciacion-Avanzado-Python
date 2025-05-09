#Importaciones
#ClienteDAO: Clase responsable de comunicarse con la base de datos (DAO = Data Access Object).
from cliente_dao import ClienteDAO
#Cliente: Clase que representa un cliente, con atributos como id, nombre, apellido, membresía.
from cliente import Cliente
#Imprime el título de la aplicación en consola.
print('--- Clientes Zona Fit ---')

opcion = None
#Crea un bucle while que se repite hasta que el usuario seleccione la opción 5 (salir).
while opcion != 5:
    #Muestra las opciones disponibles.
    print(f'''\n Menú:
          1. Listar Clientes
          2. Agregar nuevo cliente
          3. Modificar cliente
          4. Eliminar cliente
          5. Salir''')
    #Bloque try
    try:
        #Pide al usuario que introduzca una opción del 1 al 5.
        opcion = int(input('Escriba su opción (1-5): '))
    #Si el usuario introduce algo que no es un número entero, muestra un mensaje de error.
    except ValueError:
        #imprimir el mensaje de error
        print('Opción inválida, debe elejir entre 1 y 5.')
    #Si la opcion elegida es 1 - Listar Clientes
    if opcion == 1:
        #Llama al método seleccionar() de ClienteDAO, que obtiene todos los clientes de la base de datos.
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de Clientes ***')
        #Bucle que recorre e imprime cada cliente. Se mostrará porque la clase Cliente tiene definido el método __str__.
        for cliente in clientes:
            print(cliente)
    #Si la opcion elegida es 2- Agregar nuevo cliente
    elif opcion == 2:
        #Solicitamos los datos del nuevo cliente al usuario, nombre, apellido y membresía, ID es auto incrementable
        nombre_var = input('Escriba el nombre del nuevo cliente: ')
        apellido_var = input('Escriba el apellido del nuevo cliente: ')
        membresia_var = input('Introduzca la membresía del nuevo cliente: ')
        #Crear un objeto Cliente (sin id, porque se generará automáticamente).
        cliente = Cliente(nombre=nombre_var,apellido=apellido_var,membresia=membresia_var)
        #Llama a ClienteDAO.insertar(cliente).
        clientes_insertados = ClienteDAO.insertar(cliente)
        #Mostrar cuántos clientes fueron insertados.
        print(f'Clientes insertados: {clientes_insertados}')
    #Si la opcion elegida es 3- Modificar cliente
    elif opcion == 3:
        #Solicitamos al usuario que introduzca el ID del usuario que desea modificar
        id_cliente_var = int(input('Introduzca el ID del cliente que desea modificar: '))
        #Le pedimos que introduzca los nuevos datos que desea modificar, nombre apellido y membresia
        nombre_var = input('Escriba el nuevo nombre del cliente: ')
        apellido_var = input('Escriba el nuevo apellido del cliente: ')
        membresia_var = input('Introduzca la nueva membresía del cliente: ')
        #Crea el objeto Cliente con todos los valores (incluido id).
        cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        #Llama al método actualizar() de ClienteDAO.
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        #Muestra cuantos registros fueron actualizados
        print(f'Clientes actualizados: {clientes_actualizados}')
    #Si la opcion elegida es 2- Eliminar cliente
    elif opcion == 4:
        #Solicitamos al usuario que introduzca el ID del usuario que desea eliminar
        id_cliente_var = int(input('Introduzca el ID del cliente que desea eliminar: '))
        #Crea un objeto Cliente con solo el id.
        cliente = Cliente(id=id_cliente_var)
        #Llamada a ClienteDAO.eliminar(cliente).
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        #Muestra cuántos clientes fueron eliminados.
        print(f'Clientes eliminados: {clientes_eliminados}')
    #Si la opcion elegida es 2- Agregar nuevo cliente
    elif opcion == 5:
        #Mensaje de despedida
        print('Gracias por utilizar la App, vuelvan pronto!!')
    #En caso de que el usuario elija una opcion que no esta contemplada en el menú de esta App
    else:
        #Mensaje para avisar al usuario.
        print('Opción no válida, elija otra entre 1 y 5 por favor.')