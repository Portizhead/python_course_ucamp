# El programa que desarrollarás debe tener las siguientes características: 
# 1. Que en un bucle infinito solicite al usuario una letra (debes especificar al usuario la condición 
# para terminar el programa. Por ejemplo, para salir, escriba alto, presione 0 o cualquier otra que 
# se te ocurra).
# 2. Harás una función que imprima en la pantalla la letra siguiente en el alfabeto y la letra anterior 
# a la ingresada.
# 3. El programa debe continuar en el bucle hasta que el usuario decida salir del programa.


# Alfabeto en mayúsculas
alfabeto_mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Alfabeto en minúsculas
alfabeto_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alto = 1


def impresion_de_letras(letra):
    if letra.isalpha():
        if letra in alfabeto_mayusculas:
            indice_leta = alfabeto_mayusculas.index(letra)
            letra_anterior = alfabeto_mayusculas[indice_leta - 1]
            letra_siguiente = alfabeto_mayusculas[indice_leta + 1]
            print(f"La letra del usuario es {letra}, la anterior es: {letra_anterior} y la siguiente es: {letra_siguiente}")
        elif letra in alfabeto_minusculas:
            indice_leta = alfabeto_minusculas.index(letra)
            letra_anterior = alfabeto_minusculas[indice_leta - 1]
            letra_siguiente = alfabeto_minusculas[indice_leta + 1]
            print(f"La letra del usuario es {letra}, la anterior es: {letra_anterior} y la siguiente es: {letra_siguiente}")
            
    else:
        print("escribe una letra del alfabeto por favor.")

while alto != 0:
    letra = input("escribe una letra: ")
    
    if letra == '0':
        alto = 0
    elif letra.isalpha():
            impresion_de_letras(letra)
            print("para salir del programa presiona 0")
            
    else:
        print("escribe una letra del alfabeto por favor o para salir del programa presiona 0")   
    

    
    
