# <<m_promedio_alumnos.py>>

"""
Este modulo contiene la funcion captura que solicita la informacion de los
aolumnos y la funcion promedio que calculara el promedio
"""

def promedio(nombre, calificacion1, calificacion2):
    promedio = (calificacion1 + calificacion2) / 2
    print(f"El promedio de {nombre} es {promedio}")
    
def captura(numero = 3):
    lista = []
    
    for i in range(numero):
        nombre = input("Ingrese el nombre del alumno: ").capitalize()
        calif1 = int(input("ingrese la primera calificacion: "))
        calif2 = int(input("ingrese la segunda calificacion: "))
        lista.append([nombre,calif1,calif2])
        promedio(nombre,calif1,calif2)    
    print(lista)
    
    