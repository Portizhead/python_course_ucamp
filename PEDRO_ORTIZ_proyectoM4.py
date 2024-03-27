#Pokedex

import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json
import os

poke_nombre = input("Escribe el nombre de un pokemon: ")
url = f"https://pokeapi.co/api/v2/pokemon/{poke_nombre}"
respuesta = requests.get(url)

if respuesta.status_code != 200:
    print("Pokemon no encontrado")
    exit()

poke_info = respuesta.json()

def iterar_poke_abilities(poke_abilities):
    abilities = []
    for i in range(len(poke_abilities)):
        abilities.append(poke_abilities[i]["ability"]["name"])

    return abilities

def iterar_poke_moves(poke_moves):
    moves = []
    for i in range(5):
        moves.append(poke_moves[i]["move"]["name"])
    
    return moves

def iterar_poke_types(poke_types):
    types = []
    for i in range(len(poke_types)):
        types.append(poke_types[i]["type"]["name"])
    
    return types
        
# print(iterar_poke_abilities(poke_info["abilities"]))

try:
    sprite_url = poke_info["sprites"]["front_shiny"]
    sprite_open = Image.open(urlopen(sprite_url))
    plt.imshow(sprite_open)
    
    poke_peso = poke_info["weight"]
    
    poke_height = poke_info["height"]
    
    poke_movimientos = iterar_poke_moves(poke_info["moves"])
    poke_movimientos = ", ".join(poke_movimientos)
    
    poke_habilidades = iterar_poke_abilities(poke_info["abilities"])
    poke_habilidades = ",".join(poke_habilidades)
    
    poke_tipos = iterar_poke_types(poke_info["types"])
    poke_tipos = ",".join(poke_tipos)
    
    plt.title(f"{poke_nombre}")
    plt.xlabel(f"Peso: {poke_peso}Lbs\n"\
               f"Tamaño: {poke_height}\n"\
               f"Movimientos: {poke_movimientos}\n"\
               f"Habilidades: {poke_habilidades}\n"\
               f"Tipos: {poke_tipos}")
    # info_text = f"Peso: {poke_peso}\n"\
    #             f"Habilidades: {poke_habilidades}"
    
    # plt.text(10, -30, info_text, fontsize=10, color='white')
    
    poke_data = {
        "Nombre": poke_nombre,
        "Peso": poke_peso,
        "Tamaño": poke_height,
        "Movimientos": poke_habilidades,
        "Tipos": poke_tipos,
        "Sprite Frontal": sprite_url
    }
    
    with open(os.path.join("fundamentos de python\Modulo 4\pokedex",f"{poke_nombre}_info.json"), "w") as file:
        json.dump(poke_data, file, indent=4)
    
    plt.show()
    
except Exception as e:
    print("El pokemon no tiene imagen", e)    
    exit()

# with open("pokeInfo.txt", "w") as archivo:
    
        
"""

with open("agenda.txt", "w") as archivo:
    for registro in registros:
        # print(registro)
        linea_items = []
        for key, value in registro.items():
            linea_items.append(f"{key}: {value}")
            
        # print(linea_items)
        linea = ', '.join(linea_items)
        # print(linea)
        archivo.write(linea + "\n")

print("Los cambios han sido guardados en el archivo.")   



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




  info_text = f"Nombre: {poke_info['name'].capitalize()}\n" \
                f"ID: {poke_info['id']}\n" \
                f"Tipo(s): {', '.join([tipo['type']['name'] for tipo in poke_info['types']])}\n" \
                f"Altura: {poke_info['height'] / 10} m\n" \
                f"Peso: {poke_info['weight'] / 10} kg\n" \
                f"Habilidades:\n" \
                f"{', '.join([habilidad['ability']['name'] for habilidad in poke_info['abilities']])}\n" \
                # f"Movimientos:\n" 
                f"{', '.join([movimiento['move']['name'] for movimiento in poke_info['moves'][:5]])}"

    plt.text(1, -30, info_text, fontsize=10, color='white')  # Ajusta la posición del texto según sea necesario


datos = respuesta.json()
nombre = datos["name"]
item = datos["held_items"][0]["item"]["name"]
moves = datos["moves"]#[0]["move"]["name"]

print(nombre)
print(item)
# print(moves)

print(f"Movimientos de {nombre}")

for i in range(len(moves)):
    movimiento =  moves[i]["move"]["name"]
    print(movimiento)
"""



























