from GestionContactos import GestionContactos

def menu():
    """Menú principal del sistema de gestión de contactos"""
    gestion = GestionContactos()
    parar = True

    while parar != False:
        print("\n--- Sistema de Gestión de Contactos ---\n")
        print("1. Agregar Contacto \n")
        print("2. Mostrar Contactos \n")
        print("3. Buscar Contacto \n")
        print("4. Eliminar Contacto \n")
        print("5. Salir \n")

        try:
            opcion = int(input("Elige una opción válida: "))
        except ValueError:
            print("Error: Por favor, introduce un número válido.")
            continue  # Vuelve al inicio del bucle while

        if opcion == 1:
            try:
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                gestion.agregar_contacto(nombre, telefono, email)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == 2:
            gestion.mostrar_contactos()
        elif opcion == 3:
            nombre = input("Introduce el nombre del contacto a buscar: ")
            gestion.buscar_contacto(nombre)
        elif opcion == 4:
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            gestion.eliminar_contacto(nombre)
        elif opcion == 5:
            gestion.guardar_contactos()
            print("Saliendo del sistema, hasta pronto!!")
            parar = False
        else:
            print("Opción inválida. Por favor, selecciona una opción válida. ")

if __name__ == "__main__":
    menu()