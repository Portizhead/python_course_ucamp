#Pokedex

import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json
import os


if __name__ == "__main__":

    poke_name = input("Escribe el nombre de un pokemon: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Pokemon no encontrado")
        exit()

    poke_info = response.json()

    def iterate_poke_ability (poke_abilities):
        abilities = []
        for i in range(len(poke_abilities)):
            abilities.append(poke_abilities[i]["ability"]["name"])

        return abilities

    def iterate_poke_moves(poke_moves):
        moves = []
        for i in range(5):
            moves.append(poke_moves[i]["move"]["name"])
        
        return moves

    def iterate_poke_types(poke_types):
        types = []
        for i in range(len(poke_types)):
            types.append(poke_types[i]["type"]["name"])
        
        return types
            
    # print(iterate_poke_ability (poke_info["abilities"]))

    try:
        sprite_url = poke_info["sprites"]["front_shiny"]
        sprite_open = Image.open(urlopen(sprite_url))
        plt.imshow(sprite_open)
        
        poke_weight = poke_info["weight"]
        
        poke_height = poke_info["height"]
        
        poke_moves = iterate_poke_moves(poke_info["moves"])
        poke_moves = ", ".join(poke_moves)
        
        poke_abilities = iterate_poke_ability(poke_info["abilities"])
        poke_abilities = ",".join(poke_abilities)
        
        poke_types = iterate_poke_types(poke_info["types"])
        poke_types = ",".join(poke_types)
        
        plt.title(f"{poke_name}")
        plt.xlabel(f"Peso: {poke_weight}Lbs\n"\
                f"Tamaño: {poke_height}\n"\
                f"Movimientos: {poke_moves}\n"\
                f"Habilidades: {poke_abilities}\n"\
                f"Tipos: {poke_types}")
        # info_text = f"Peso: {poke_weight}\n"\
        #             f"Habilidades: {poke_abilities}"
        
        # plt.text(10, -30, info_text, fontsize=10, color='white')
        
        poke_data = {
            "Nombre": poke_name,
            "Peso": poke_weight,
            "Tamaño": poke_height,
            "Movimientos": poke_abilities,
            "Tipos": poke_types,
            "Sprite Frontal": sprite_url
        }
        
        with open(os.path.join("fundamentos de python\Modulo 4\pokedex",f"{poke_name}_info.json"), "w") as file:
            json.dump(poke_data, file, indent=4)
        
        plt.show()
        
    except Exception as e:
        print("El pokemon no tiene imagen", e)    
        exit()


    
  
