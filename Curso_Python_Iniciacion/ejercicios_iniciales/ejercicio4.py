#EJERCICIO 4:
#Función para calcular el área de un círculo

#importar libreria MATH
import math

#definir la función
def areaCirculo(radio):
    return math.pi * radio ** 2

#Solicitar el radio del circulo al usuario
radio = float(input("Introduce el radio del círculo: "))

#calcular y mostrar el resultado
print(f"El área del círculo con radio {radio}cm, es de {areaCirculo(radio):.2f}cm")