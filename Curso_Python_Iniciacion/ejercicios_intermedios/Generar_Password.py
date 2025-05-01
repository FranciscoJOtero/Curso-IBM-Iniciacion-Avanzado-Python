#GENERADOR DE CONTRASEÑAS:
#Solicitamos al usuario la longitud de la contraseña y se genera una aleatoria.

#importar libreria random:
import random

#definir las listas
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%^&*."

#combinar todos los caracteres
todos_caracteres = mayusculas + minusculas + numeros + simbolos

#/******************************************************************************************************************************************
#Funcion para validar longitud, debe ser mayor a 4 caracteres
def validar_longitud():
    #Bucle while para que se repita hasta que el usuario ingrese los datos correctos
    while True:
        #bloque try-except para manejar los errores si el usuario ingresa algo que no sea correcto
        try:
            #solicitar la longitud de la contraseña al usuario:
            longitud = int(input("Introduce la longitud de tu contraseña(mínimo 4 caracteres): "))
            #Condicional para asegurarnos de que la contraseña contenga al menos 4 caracteres.
            if longitud >= 4:
                #retornamos el valor de longitud y se detiene el bucle while
                return longitud
            #en el else le indicamos que la longitud es incorrecta, se repite el bucle y vuelve a pedir la longitud
            else:
                print("Longitud no admitida, debe ser superior a 4 caracteres.")
        #En este caso controlamos con este bloque si el usuario introduce algo que no sea un número entero
        except ValueError:
            print("Solo se admiten números enteros.")
#/*******************************************************************************************************************************************
#Función para que el usuario seleccione los tipos de caracteres para su contraseña
def seleccionar_caracteres():
    #Pedimos al usuario que seleccione con s/n el tipo de caracteres
    print("Selecciona los tipos de caracteres para la contraseña:")
    #Variables donde el usuario introduce s/n para elegir sus caracteres
    #.lower()-> convierte lo que introduzca el usuario en minusculas
    #Comparamos si la respuesta del usuario es igual a 's', si es asi devuelve true, de lo contrario devolverá false
    usar_mayusculas = input("incluir mayusculas? (s/n): ").lower() == 's'
    usar_minusculas = input("incluir minusculas? (s/n): ").lower() =='s'
    usar_numeros = input("incluir números? (s/n): ").lower() =='s'
    usar_simbolos = input("incluir simbolos? (s/n): ").lower() =='s'

    #inicializar una cadena vacia para almacenar los caracteres seleccionados
    caracteres = ""
    #si el usuario elegio incluir mayusculas, añade el contendio de la variable mayusculas a la variable caracteres
    if usar_mayusculas:
        caracteres += mayusculas
    #si el usuario elegio incluir minusculas, añade el contendio de la variable minusculas a la variable caracteres
    if usar_minusculas:
        caracteres += minusculas
    #si el usuario elegio incluir números, añade el contendio de la variable numeros a la variable caracteres
    if usar_numeros:
        caracteres += numeros
    #si el usuario elegio incluir símbolos, añade el contendio de la variable simbolos a la variable caracteres
    if usar_simbolos:
        caracteres += simbolos
    #Verificar si la cadena caracteres no está vacia, si está vacia, se volverá a repetir de nuevo la función
    if not caracteres:
        #mensaje de error
        print("Debes seleccionar al menos un tipo de caracter. ")
        #llamada recursiva a la la propia función
        return seleccionar_caracteres()
    #Si todo a ido bien, la función devolverá el valor de la cadena caracteres
    return caracteres
#/******************************************************************************************************************************
#Función para generar múltiples contraseñas
#Definimos la función que recibe 3 parámetros de entrada
def generar_varias_contrasenias(cantidad, longitud, caracteres):

    #lista vacia para almacenar las contraseñas que se generen.
    contrasenias = []

    #bucle for que itera lastantas veces como tenga el valor de la variable cantidad
    # "_" es una variable descartable, se usa cuando no necesitamos el valor del indice(cuando queremos repetir algo un nº específico de veces)
    for _ in range(cantidad):

        #"".join(...)-> Une todos los caracteres seleccionados en una sola cadena. 
        # Por ejemplo, si los caracteres seleccionados son ['A', '1', '@'], el resultado será "A1@".
        #random.choice(caracteres)-> Selecciona un carácter aleatorio del conjunto caracteres
        #for _ in range(longitud) :-> Repite la selección de caracteres longitud veces. Esto crea una secuencia de longitud caracteres aleatorios.
        contrasenia = "".join(random.choice(caracteres) for _ in range(longitud))

        #Agrega la contraseña generada (contrasenia) a la lista contrasenias
        contrasenias.append(contrasenia)
    #Después de generar todas las contraseñas, la función devuelve la lista completa
    return contrasenias
#/**********************************************************************************************************************************
#Funcion para guardar las contraseñas generadas en un archivo .txt
def guardar_contrasenias(contrasenias, archivo='contrasenias.txt'):

    #Abrir el archivo en modo escritura
    #Si el archivo ya existe, su contenido será sobreescrito
    #Si el archivo no existe, se creará automáticamente
    #El uso de with, nos asegura que el archivo se cierre automáticamente después de terminar el bloque, incluso si ocurre un error.
    with open(archivo, "w") as f:

        #Itera sobre la lista contrasenias usando enumerate().
        #enumerate()-> devuelve tanto el índice (i) como el valor (contrasenia) de cada elemento en la lista.
        #start=1-> indica que los índices deben comenzar desde 1 en lugar de 0.
        for i, contrasenia in enumerate(contrasenias, start=1):

            #Escribe una línea en el archivo con el formato "Contraseña X: <contraseña>".
            #f"..." es una f-string , que permite insertar variables dentro de un string.
            #\n añade un salto de línea al final de cada contraseña para que cada una aparezca en una línea separada.
            f.write(f"Contraseña {i}: {contrasenia}\n")

        #Mostrar el mensaje de que se han guardado en nombreArchivo.txt
        print(f"Las contraseñas se han guardado en '{archivo}'.")
#/**********************************************************************************************************************************       
#obtener la longitud llamando a la funcion anterior
longitud = validar_longitud()

#Seleccionar los tipos de caracteres llamando a la funcion anterior
caracteres = seleccionar_caracteres()

#Pedir la cantidad de contraseñas a generar
cantidad = int(input("Introduce la cantidad de contraseñas que deseas generar: "))

#Generar las contraseñas
contrasenias = generar_varias_contrasenias(cantidad, longitud, caracteres)

#Mostrar las contraseñas generadas
print("\nContraseñas generadas: ")
for i, contrasenia in enumerate(contrasenias, start=1):
    print(f"Contraseña {i}: {contrasenia}")

#Guardamos las contraseñas en un archivo
guardar_contrasenias(contrasenias)