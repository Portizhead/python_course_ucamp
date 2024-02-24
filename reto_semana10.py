# realiza un programa que emplee funciones y que tenga las siguientes características:
# ● Que permita crear dos listas de distintas longitudes.
# ● Que la longitud y los elementos de cada lista sean especificados por el usuario.
# ● Que imprima las listas indicando que son las listas originales.
# ● Que elimine de la primera lista los nombres de la segunda.
# ● Que imprima la primera lista indicando que se han eliminado los elementos que estaban también en la segunda.

print("Vamos a crear dos listas, pueden ser de distintas longitudes.")


# lista1_len = int(input("De que tamaño sera la primer lista?: "))
# lista1 = []
# #ingresar los elementos de la lista1
# for i in range(lista1_len):
#     elemento = input((f"Por favor ingresa el elemento {i+1} de tu lista: "))
#     lista1.append(elemento)


# lista2_len = int(input("De que tamaño sera la segunda lista?: "))
# lista2 = []
# #ingresar elementos de la lista2
# for i in range(lista2_len):
#     elemento = input((f"Por favor ingresa el elemento {i+1} de tu lista: "))
#     lista2.append(elemento)

# #mostrar elementos de las listas    
# print(lista1)
# print(lista2)

# for elemento in lista1:
#     if elemento in lista2:
#         lista1.remove(elemento)

# print(lista1)    




def crear_lista():
    lista = []
    list_size = int(input("De que tamaño sera la lista? "))
    
    for i in range(list_size):
        element = input((f"Por favor ingresa el elemento {i+1} de tu lista: "))
        lista.append(element)
    return lista    

def comparar_listas(lista1, lista2):
    
    for elemento in lista1:
        if elemento in lista2:
            lista1.remove(elemento)
    
    return lista1            
    
lista1 = crear_lista()
lista2 = crear_lista()
print(f"las listas son: {lista1} y {lista2} ")
print(f"la lista 1 despues de remover los elementos que estaban tambine en la segunda: {comparar_listas(lista1, lista2)}")