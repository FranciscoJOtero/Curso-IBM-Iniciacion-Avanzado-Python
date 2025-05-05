#Punto de entrada de la aplicación de gestión de inventario

#importar las clases GestionInventario y Producto definidas en el fichero gestion_inventario.py
from gestion_inventario import GestionInventario, Producto

#Definición del método menu, el cual mostrará el menu de la aplicación
def menu():
    #Crea una "instancia" de la clase `GestionInventario`, que manejará toda la conexión con la base de datos y operaciones CRUD (crear, leer, actualizar, eliminar).
    gestion = GestionInventario()
    #bucle while infinito, estará siempre activo hasta que pulsemos sobre la opción 6
    while True:
        #imprimir el menú de la App
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar un producto")
        print("4. Actualziar un producto")
        print("5. Eliminar un producto")
        print("6. Salir")

        #bloque try para controlar errores
        try:
            #Solicitar al usuario que seleccione una opción
            opcion = int(input("Selecciona una opción válida: "))

        #En caso de que el usuario introduzca algo que no sea un número
        except ValueError:
            #mensaje para informar al usuario
            print("Por favor, introduce un número entre el 1 y el 6")
            #volver al inicio del bucle
            continue

        #Opción 1- agregar producto
        if opcion == 1:
            #datos del prodcuto
            nombre = input("Nombre del producto: ") 
            cantidad = input("Cantidad: ")
            precio = float(input("Precio del producto: "))
            categoria = input("Categoría del producto: ")
            #crear objeto de la clase Producto 
            producto = Producto(nombre, cantidad, precio, categoria)
            #llamada al metodo de agregar para guardarlo en la BBDD
            gestion.agregar_producto(producto)

        #Opción 2- mostrar producto
        elif opcion == 2:
            #llamada a la función para mostrar todos los productos
            gestion.mostrar_productos()

        #Opción 3- Buscar producto
        elif opcion == 3:
            #solicitamos al usuario que introduzca un nombre para buscar un producto
            nombre = input("Introduce el nombre del producto que desea buscar: ")
            #llamada al método para buscar un producto
            gestion.buscar_producto(nombre)

        #Opción 4- Actualizar producto
        elif opcion == 4:
            #solicitamos al usuario que introduzca un nombre para actualizar ese producto
            nombre = input("Introduce el nombre del producto que desea actualizar: ")
            #solicitamos los nuevos datos del producto
            cantidad = input("Nueva cantidad: ")
            precio = float(input("Precio del producto: "))
            categoria = input("Categoría del producto: ")
            #llamada al método de actualizar
            gestion.actualizar_producto(nombre, cantidad, precio, categoria)

        #Opción 5- Eliminar producto
        elif opcion == 5:
            #solicitamos al usuario que introduzca un nombre para eliminar ese producto
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            #llamada al método para eliminar el producto
            gestion.eliminar_producto(nombre)

        #Opción 6- Salir del programa
        elif opcion == 6:
            #mensaje de despedida
            print("Saliendo del programa...")
            #finalizar bucle while, el menu dejará de estar activo
            break
        #en caso de que el usuario elija una opción incorrecta
        else:
            #mensaje para informar
            print("Opción no válida, intentelo de nuevo.")

#Significa que solo se ejecutará menu() si este archivo se ejecuta directamente (no si se importa desde otro script).
#Es una buena práctica en Python para evitar que el programa arranque accidentalmente al importar el archivo desde otro módulo.
if __name__ == "__main__":
    menu()