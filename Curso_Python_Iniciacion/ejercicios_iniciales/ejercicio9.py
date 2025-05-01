#EJERCICIO 9: Palíndromo
#Comprobar si una palabra se escribe igual al derecho que al revés

#solicitamos una palabra al usuario:
palabra = input("Introduzca una palabra: ")

#verificar si es un palindromo
if palabra == palabra[::-1]:#slicing, se usa para invertir una cadena
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")

