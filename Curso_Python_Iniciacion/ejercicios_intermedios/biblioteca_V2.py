#/**************************************************************************************************************************************************
#/**************************************************************************************************************************************************

#Ejercicio Final curso de iniciación en Python: Gestión de Biblioteca -->
#/**************************************************************************************************************************************************
#/**************************************************************************************************************************************************

#Definimos una nueva clase llamada Libro
class Libro:

    #CÓDIGO MEJORADO CON ATRIBUTOS PRIVADOS Y @PROPERTY(MEJORA V2)
    #Este es el constructor de la clase Libro con tres parámtetros(titulo, autor, isbn)
    # self -> Es una referencia al objeto que se está creando.
    def __init__(self, titulo, autor, isbn):

        #Asignamos los valores de los parámetros a los atributos del objeto.
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        #booleano para la disponibilidad de los libros(True o False)
        self.__disponible = True # cada objeto de la clase que se cree, por defecto estará disponibe(True). Atributo privado

    #Getters y setters usando @prperty
    @property
    #Getters: métodos que permiten acceder a los valores de los atributos de una clase.
    #El método titulo (decorado con @property) permite acceder al valor del atributo privado __titulo.
    def titulo(self):
        return self.__titulo
    
    #Setters: Son métodos que permiten modificar los valores de los atributos de una clase, 
    #generalmente con validaciones para asegurar que los datos sean correctos.
    #El método titulo (decorado con @titulo.setter) permite modificar el valor de __titulo, 
    #pero solo si el nuevo valor es una cadena de texto (str).
    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo, str) and titulo.strip():#Validación simple de titulo
            self.__titulo = titulo
        else:
            raise ValueError("El título debe ser una cadena de texto no vacia.")
    
    #Funciona de manera similar al getter de titulo
    @property
    def autor(self):
        return self.__autor
    
    #Funciona de manera similar al setter de titulo
    @autor.setter
    def autor(self, autor):
        if isinstance(autor, str) and autor.strip(): #Validación simple de autor
            self.__autor = autor
        else:
            raise ValueError("El autor debe ser una cadena de texto no vacia.")
    
    ##Funciona de manera similar al getter de titulo
    @property
    def isbn(self):
        return self.__isbn
    
    ##Funciona de manera similar al setter de titulo
    @isbn.setter
    def isbn(self, isbn):
        if isinstance(isbn, str) and isbn.strip(): #Validación simple de ISBN
            self.__isbn = isbn
        else:
            raise ValueError("El ISBN debe ser una cadena de texto no vacia.")
    
    #Funciona de manera similar al getter de titulo
    @property
    def disponible(self):
        return self.__disponible

    #método que usamos para prestar libros
    def prestar(self):
        #Comprobamos si el libro esta disponible, condicional que devuelve True
        if self.__disponible:
            #modificamos la disponibilidad del libro a False
            self.__disponible = False
            #Mensaje de confirmación que incluye el nombre del libro
            print(f"Libro {self.titulo} prestado con éxito.")
        #en caso de que el condicional devuelva false...
        else:
            #mensaje de advertencia para informar de que el libro ya esta prestado.
            print(f"El libro {self.titulo} ya está prestado.")

    #método que usamos para devolver los libros prestados
    def devolver(self):
        #Condicional para comprobar la disponibilidad, si su estado es false(prestado)...
        if not self.__disponible:
            #...modificamos el valor del atributo a true(disponible para volver a prestar).
            self.__disponible = True
            #mensaje de confirmación que incluye el nombre del libro que se ha devuelto.
            print(f"Libro {self.titulo} devuelto con éxito.")
        #en caso contrario, que la disponibilidad sea true(disponible)...   
        else:
            #mensaje de aviso al usuario para indicar que dicho libro estaba ya disponible(true)
            print(f"Libro {self.titulo} ya estaba devuelto.")

    #método para mostrar todos los libros que contiene la biblioteca
    def mostrar(self):
        #operador ternario para mostrar en el estado una cosa u otra según corresponda:
        #self.disponible == True estado = "Si"
        #self.disponible == False estado = "No"
        estado = "Sí" if self.disponible else "No"
        #mensaje al usuario con todos los datos(atributos) del obejto de la clase Libro
        print(f"Título: {self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Disponible {estado}")

#/**************************************************************************************************************************************************
#/**************************************************************************************************************************************************

#declaramos una clase Biblioteca
class Biblioteca:

    #Este es el constructor de la clase. Se llama automáticamente cuando se crea un nuevo objeto Biblioteca.
    def __init__(self):
        #Inicializamos un atributo llamado "libros" como una lista vacía. Esta lista almacenará 
        #los objetos Libro que se agreguen a la biblioteca.
        self.__libros = [] #Atributo privado

    #método para agregar libros a la biblioteca con 3 parametros(titulo, autor, isbn)
    def agregar(self, titulo, autor, isbn):

        #Verificamos si el ISBN ya existe
        for libro in self.__libros:

            #Si el ISBN ya existe
            if libro.isbn == isbn:
                #mostramos mensaje de error al usuario
                print("Error: Ya existe un libro con este ISBN.")
                #fin del método
                return
            
        #Variable nuevo_libro donde almacenamos un nuevo objeto de la clase Libro
        nuevo_libro = Libro(titulo, autor, isbn)
        #Añadimos nuevo_libro con .append la lista vacia "libros"
        self.__libros.append(nuevo_libro)
        #mensaje de confirmación, el libro se ha añadido a la biblioteca
        print("Libro agregado con éxito! Gracias.")

    #método para prestar un libro de la biblioteca
    def prestar(self,isbn):
        #declaramos un bucle for para recorrer la lista "libros"
        for libro in self.__libros:
            #Si el atributo isbn de alguno de los libros coincide con el que introduce el usuario...
            if libro.isbn == isbn:
                #...llamamos al método prestar() de la clase libro para que preste el libro y cambie la 
                #disponibilidad del mismo
                libro.prestar()
                #finaliza el método
                return
        #si tras recorrer la lista no encontramos coincidencias, mensaje de aviso para el usuario
        print("Libro no encontrado.")

    #método para devolver un libro a la biblioteca(muy parecida a la anterior)
    def devolver(self, isbn):
        #recorrer la lista "libros"
        for libro in self.__libros:
            #si hay coincidencias en el isbn
            if libro.isbn == isbn:
                #llamada al método devolver de la clase Libro
                libro.devolver()
                #finaliza el método
                return
        #mensaje de aviso al usuario si no hay coincidencias
        print("Libro no encontrado.")

    #mostrar los libros que hay en la biblioteca
    def mostrar(self):
        #Condicional para comprobar si la lista libros esta vacia...
        if not self.__libros:
            #Avisamos al usuario de que esta vacia
            print("Biblioteca vacía.")
        #en caso contrario, la lista "libros" si contiene algun "libro"
        else:
            #mensaje del listado
            print("\n Listado de Libros existentes en la Biblioteca: ")
            #recorremos la lista libros con el bucle for, en cada iteración 
            #hace la llamada al método mostrar() de la clase Libro
            for libro in self.__libros:
                #llamada al método mostrar() de la clase Libro
                libro.mostrar()

    #método para buscar un libro introduciendo su ISBN
    def buscar(self, isbn):
        #mediante un bucle for recorremos la lista...
        for libro in self.__libros:
            #si encuentra coincidencias con el isbn introducido...
            if libro.isbn == isbn:
                #llamada a la función mostrar de la clase Libro
                libro.mostrar()
                #fin del método
                return
        #si tras recorrer la lista no hay coincidencias, avisamos al usuario con un mensaje
        print("Libro no encontrado.")

#/**************************************************************************************************************************************************
#/**************************************************************************************************************************************************

#método principal para mostrar el menú del programa y controlar la lógica del programa
def main():
    #Creamos un objeto Biblioteca llamado biblioteca.
    #Este objeto se utilizará para gestionar los libros en la biblioteca.
    biblioteca = Biblioteca()

    #Bucle while infinito que muestra el menú de opciones al usuario.
    while True:
        #mensaje de bienvenida y las opciones del menú
        print("\n Bienvenidos al Sistema de Gestión de Biblioteca:")
        print("1.Agregar libro")
        print("2.Prestar libro")
        print("3.Devolver libro")
        print("4.Mostrar libros")
        print("5.Buscar libro por ISBN")
        print("6.Salir")

        #Se añade un bloque "try-except" para capturar errores de conversión (ValueError) en caso de que
        #ocurra algún problema inesperado(mejora v2).
        try:
            #capturamos el valor que introduzca el usuario en una variable
            option = int(input("Eliga una opción del menú: "))
        except ValueError:
            print("Debes ingresar un número válido.")

        try:
            #Si la opcion del usuario fue 1
            if option == 1:
                #solicitamos los datos del nuevo libro al usuario
                titulo = input("Título: ") 
                autor = input("Autor: ")     
                isbn = input("ISBN: ")
                #llamamos al método agregar() de la clase Biblioteca para agregar el nuevo libro a la biblioteca.
                biblioteca.agregar(titulo, autor, isbn)

            #Si la opción del usuario fue 2
            elif option == 2:
                #solicitamos al usuario que introduzca el isbn del libro para prestarselo...
                isbn = input("Ingresa el ISBN: ")
                #llamamos al método prestar() de la clase Biblioteca.
                biblioteca.prestar(isbn)

            #Si la opción del usuario fue 3
            elif option == 3:
                #solicitamos al usuario que introduzca el isbn del libro para que lo devuelva...
                isbn = input("Ingresa el ISBN: ")
                #llamamos al método devolver() de la clase Biblioteca.
                biblioteca.devolver(isbn)
            #Si la opción del usuario fue 4
            elif option == 4:
                #llamamos al método mostrar() de la clase Biblioteca para mostrar la lista de libros al usuario
                biblioteca.mostrar()
            #Si la opción del usuario fue 5
            elif option == 5:
                #solicitamos al usuario que introduzca el isbn del libro para buscarlo...
                isbn = input("Ingresa el ISBN: ")
                #llamamos al método buscar() de la clase Biblioteca.
                biblioteca.buscar(isbn)
            #Si la opción del usuario fue 6
            elif option == 6:
                #mensaje de agradecimiento y despedida al usuario.
                print("Cerrando Sistema de Gestión de Biblioteca. \n Gracias por si visita, vuelvan pronto!!Saludos.")
                #termina el bucle infinito while
                break
            #si introduce cualquier otra opción le mostramos mensaje de error
            else:
                #mensaje de error para que vuelva a seleccionar una nueva opción
                print("Debe seleccionar una opción válida, vuelva a intentarlo. ")

        except Exception as e:
                print(f"Error: {e}")
                
#/**************************************************************************************************************************************************
#/**************************************************************************************************************************************************

#Esta línea verifica si el script se está ejecutando como programa principal.
if __name__ == "__main__":

    #Si es así, se llama a la función main()
    main()

#/**************************************************************************************************************************************************
#/**************************************************************************************************************************************************

#EJERCICIO REALIZADO POR EL ALUMNO FRANCISCO JAVIER OTERO HERRERO, CURSO INICIACIÓN EN PYTHON IMPARTIDO POR IBM

#/**************************************************************************************************************************************************
#/**************************************************************************************************************************************************
