# Longitud de una frase

# Pseudo Codigo
# 1- primero pedimos la frase al usuario
# 2- verificamos el tamaño de la frase
# 3- crear una condicion que verifique que la frase tiene entre cuatro y ocho letras
# 4- vamos a crear 3 escenarios dependiendo del resultado de la verificacion del paso 3:
#     si esta en rango imprimimos un mensaje que diga que la palabra es correcta
#     si tiene menos de 4 letras imprimir un mensaje que diga hacen falta letras, solo tiene N letras
#     si tiene mas de 8 letras imprmir un mensaje que diga sobran letras, tiene N letras
    
programa = True

while programa == True:
    frase = input("Escribe una palabra que tenga entre 4 y 8 letras: ")
    longitud_frase = len(frase)
    
    if frase.isdigit():
        print("Lo siento, eso no es una palabra, son números. Intenta otra vez")
    else:
        if longitud_frase <= 3:
            print(f"Hacen falta letras. Solo tiene {longitud_frase} letras. Intenta otra vez")            
        elif longitud_frase >= 9:
            print(f"Sobran letras. Tiene {longitud_frase} letras. Intenta otra vez")            
        else:
            print(f"La palabra es correcta.")    
            break
        
        
# Encuentra el cuadrante

# Pseudo Codigo 
# 1- pedir los numeros de entrada o sea las coordenadas
# 2- definir la combinacion de los numeros que se encuentran en cada cuadrante 
# es decir la combinacion positivo-positivo que cuadrante es
# 3- si el usuario ingresa el valor de 0 poner que no puede ser 0 ya que ese 
# valor no se encuentra en ningun cuadranta 


def determinar_cuadrante(x, y):
    if x > 0 and y > 0:
        return "I"
    elif x < 0 and y > 0:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    elif x > 0 and y < 0:
        return "IV"
    else:
        return "El punto se encuentra en un eje o en el origen."

def resultado():
    x = float(input("Ingrese X: "))
    y = float(input("Ingrese Y: "))

    if x != 0 and y != 0:
        cuadrante = determinar_cuadrante(x, y)
        print(f"El punto se encuentra en el cuadrante {cuadrante}.")
    else:
        print("Las coordenadas no pueden ser cero.")


resultado()























































