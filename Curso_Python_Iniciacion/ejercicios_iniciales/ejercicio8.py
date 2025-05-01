#EJERCICIO 8: Tabla de multiplicar
#Pedir un número al usuario y mostrar la tabla de multiplicar de dicho número.
#Solicitamos numero al usuario
numero = int(input("Introduzca un número: "))

#imprimir en consola la tabla mediante bucle for
print(f"La tabla de multiplicar de {numero} es: ")
#en cada iteracion i aumenta en 1 su valor entre los valores 1 y 11
for i in range(1,11):
    #mostramos en pantalla el resultado a cada iteracion del bucle.
    print(f"{numero} x {i} = {numero * i}")