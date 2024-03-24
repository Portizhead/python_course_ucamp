#Consultor de clima
import requests

while True:
    print("""Elije con que opcion quieres buscar el clima de tu ciudad:
        Opciones:
        1.-Con la latitud y la longitud
        2.-Con el nombre de la ciudad""")
        
    try:
        option = int(input("Opcion: "))
        
        if option == 1:
            lat = int(input("Ingresa la latitud: "))
            lon = int(input("Ingresa la longitud: "))
            break
        elif option == 2:
            nombre_ciudad = input("Ingresa el nombre de la ciudad con el siguiente formato: CIUDAD,SIGLAS_DEL_PAIS: ")    
            break
    except ValueError:
        print("Opcion no valida intenta de nuevo\n**********************************************************")    


# api_key = input("Ingresa tu API Key de OpenWeather: ")


url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"

respuesta = requests.get(url)

if respuesta.status_code != 200:
    print("Ha ocurrido un error. Intenta nuevamente")
    exit()
    
    

# api_key = input("Introduce tu API key de OpenWeather")#



