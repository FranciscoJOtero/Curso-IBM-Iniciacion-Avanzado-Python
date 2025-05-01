#EJERCICIO 7: Contador de Vocales
#Pedir al usuario que introduzca una frase o una palabra y contar las vocales

palabra = input("Introduzca una frase o una palabra: ")

contador_vocales = 0

for letra in palabra:
    if letra.lower() in "aeiou":
        contador_vocales +=1

print(f"La palabra o frase {palabra} tiene {contador_vocales} vocales.")