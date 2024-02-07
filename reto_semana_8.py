diccionario_colores_arcoiris = {
    "rojo": "🔴",
    "naranja": "🟠",
    "amarillo": "🟡",
    "verde": "🟢",
    "azul": "🔵",
    "índigo": "🟣",
    "violeta": "🟪",
}

rainbow_colors_dictionary = {
    "red": "🔴",
    "orange": "🟠",
    "yellow": "🟡",
    "green": "🟢",
    "blue": "🔵",
    "indigo": "🟣",
    "violet": "🟪",
}

opcion = False

while opcion == False:

    idioma = input("Presiona 1 para Español, Press 2 for English: ")

    if idioma == "1":
        frase = input("Escribe una frase que hable de uno o mas colores: ")
        frase =  frase.lower()
        palabras = frase.split()
        
        respuesta = ''
        
        for palabra in palabras:
            if palabra in diccionario_colores_arcoiris:
                respuesta = respuesta + " " + diccionario_colores_arcoiris[palabra] + " "
            else:
                respuesta = respuesta + " " + palabra + " " 
        
        print(respuesta)
        break
          
    elif idioma == "2":
        phrase = input("Write a phrase that mentions one or more colors: ")
        phrase = phrase.lower()
        words = phrase.split()

        answer = ''
        
        for word in words:
            if word in rainbow_colors_dictionary:
                answer = answer + " " + rainbow_colors_dictionary[word] + " "
            else:
                answer = answer + " " + word  + " " 

        print(answer)
        break
    
    else:
        print("Opcion no valida: ")





















# emoji_diccionario = { "hola": "👋",
#     "bienvenido": "🤝",
#     "gracias": "🙏",
#     "amor": "❤️",
#     "feliz": "😄",
#     "triste": "😢",
#     "comida": "🍕",
#     "sol": "☀️",
#     "lluvia": "🌧️"}

# frase = input("Escribe una frase: ")
# frase = frase.lower()
# palabras = frase.split()

# respuesta = ''

# for palabra in palabras:
#     if palabra in emoji_diccionario:
#         respuesta = respuesta + " " + emoji_diccionario[palabra] + " "
#     else:
#         respuesta = respuesta + " " + palabra + " "    

# print(respuesta)        