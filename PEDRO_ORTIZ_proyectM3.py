import random
import matplotlib.pyplot as plt

#metodo para la representacion de la caida de las bolas
def drop_ball(numero_filas):
    posicion = 0
    for i in range(numero_filas):
        #para saber si se iba a la derecha o a la izquierda
        direccion = random.choice([-1, 1])  # -1: izquierda, 1: derecha
        #ver donde caera
        posicion += direccion
    return posicion

def correr_simulacion(numero_filas, num_bolitas):
    resultado = [0] * (2 * numero_filas + 1)

    for i in range(num_bolitas):
        posicion_final = drop_ball(numero_filas)
        index_final = min(max(0, posicion_final + numero_filas), len(resultado) - 1)
        resultado[index_final] += 1

    return resultado

def plot_resultado(resultado):
    #para la grafica usamos la de barras para representar la acumulacion de las bolitas
    plt.bar(range(len(resultado)), resultado)
    plt.xlabel('Posición en las bolitas')
    plt.ylabel('Frecuencia acumulada de bolitas')
    plt.title('Simulación de la máquina de Galton')
    plt.show()

# Ejemplo de uso
numero_filas = 12
num_bolitas = 3000

resultado = correr_simulacion(numero_filas, num_bolitas)
plot_resultado(resultado)
