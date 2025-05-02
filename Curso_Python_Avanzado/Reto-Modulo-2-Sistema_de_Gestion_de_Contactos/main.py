#Importar la clase GestionContactos desde otro archivo
from GestionContactos import GestionContactos

#Funcion principal (main) para mostrar el menú del programa
def menu():
    """Menú principal del sistema de gestión de contactos"""
    #Inicializacion, gestion es una instancia de la clase que gestiona la lista de contactos
    gestion = GestionContactos()
    #controla el bucle while del menu, mientras sea true, el menu seguira activo
    parar = True

    #bucle while, mientras sea distinto de false, el menu seguira activo
    while parar != False:
        #Menu de las opciones del programa
        print("\n--- Sistema de Gestión de Contactos ---\n")
        print("1. Agregar Contacto \n")
        print("2. Mostrar Contactos \n")
        print("3. Buscar Contacto \n")
        print("4. Eliminar Contacto \n")
        print("5. Salir \n")

        #bloque try para controlar errores
        try:
            #pedir al usuario que elija una opcion, y lo convertimos a int
            opcion = int(input("Elige una opción válida: "))
        #Si el usuario introduce algo que no sea un numero, lanzará un error
        except ValueError:
            #mensaje de error para informar al usuario
            print("Error: Por favor, introduce un número válido.")
            #Vuelve al inicio del bucle while
            continue
        
        #Menu de opciones, opcion 1, para agregar usuario
        if opcion == 1:
            #bloque try para controlar errores
            try:
                #datos que introduce el usuario
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                #llamada al metodo para guardar el contacto
                gestion.agregar_contacto(nombre, telefono, email)
            #En caso de errores
            except ValueError as e:
                #mostrara mensaje con el tipo de error
                print(f"Error: {e}")
        
        #Opcion 2, para mostrar los contactos existentes
        elif opcion == 2:
            #llamada al metodo para mostrar los contactos
            gestion.mostrar_contactos()
        
        #Opcion 3, para buscar un contacto por su nombre
        elif opcion == 3:
            #pedimos al usuario que introduzca el nombre que desea buscar
            nombre = input("Introduce el nombre del contacto a buscar: ")
            #llamada al metodo que se encarga de buscar contactos por su nombre
            gestion.buscar_contacto(nombre)

        #Opcion 4, para eliminar un contacto
        elif opcion == 4:
            #peir al usuario que introduzca un nombre
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            #llamada al metodo para eliminar contactos
            gestion.eliminar_contacto(nombre)
        
        #Opcion 5, salir del programa
        elif opcion == 5:
            #llamada al metodo para guardar los contactos
            gestion.guardar_contactos()
            #mensaje de despedida
            print("Saliendo del sistema, hasta pronto!!")
            #detener el bucle, el menu deja de estar activo
            parar = False

        #en caso de que introduzca una opcion numerica no valida
        else:
            print("Opción inválida. Por favor, selecciona una opción válida. ")

#Punto de entrada principal
if __name__ == "__main__":
    #Permite que el menú se ejecute solo si el script es ejecutado directamente (no si se importa desde otro archivo).
    menu()