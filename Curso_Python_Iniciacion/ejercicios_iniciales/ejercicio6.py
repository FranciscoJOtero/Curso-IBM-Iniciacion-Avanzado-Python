#EJERCICIO 6: Adivina el número.
#Escribir un programa que genere un número aleatorio entre 1 y 10 y le pida al usuario que lo adivine.
#El programa debe indicar si el número es mayor o menor que el ingresado.

#Importar metodo Random
import random

#Generar el número aleatorio entre 1 y 10
numero_secreto = random.randint(1,10)

#Añadimos una variable para indicarle al usuario el nº de intentos que lleva
intento = 0

#bucle infinito
while True:
    #a cada iteracion intento sumará 1
    intento +=1
    #Solicitamos un número al usuario
    numero = int(input(f"Intento nº {intento}: Introduzca un número entre 1 y 10 para adivinar el nº secreto: "))
    #condicional para ver si el nº del usuario es mayor o menor al numero aleatorio generado
    if numero == numero_secreto:
        #Si adivina el número
        print(f"¡Correcto! Has adivinado el número que era: {numero_secreto}")
        print("FIN DEL JUEGO")
        #detener el bucle infinito while
        break
    #si el numero del usuario es menor le damos una pista
    elif numero < numero_secreto:
        print("Te has quedado corto...el número es mayor, prueba otra vez")
    #si el numero del usuario es mayor le damos una pista
    else:
        print("Te has pasado...el número es menor, prueba otra vez")