#EJERCICIO 5:Lista de la compra->
#Crear un programa que permita al usuario agregar elementos a una lista de compras y luego
#mostrar la lista completa:

#Inicializar una lista
lista_compra = []

#Esto seria un bucle infinito
while True:
    item = input("Ingresa un articulo a tu lista de la compra, o escriba fin para terminar: ")
    #con esto evitamos que sea un bucle infinito
    if(item.lower() == "fin"):
        break
    #agregamos cada articulo que el usuario ingrese a la lista 
    lista_compra.append(item)

#Mostrar la lista de compras
#con el bucle for recorremos la lista completa
print("\nTu lista de la compra es: ")
for item in lista_compra:
    print(f"- {item}")