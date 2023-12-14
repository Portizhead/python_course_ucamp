print("***   Calculadora de Indice de Masa Corporal   ***")

fields_filled = False

while fields_filled == False: 

    name = input("Por favor ingresa tu nombre: ")

    last_name_1 = input("Por favor ingresa tu apellido paterno: ")

    last_name_2 = input("Por favor ingresa tu apellido materno: ")

    age = input("Por favor ingresa tu edad usando números no letras: ")

    weight = input("Por favor ingresa tu peso usando números no letras: ")

    height = input("Por favor ingresa tu estatura usando números no letras: ")

    if (name == "" or last_name_1 == "" or last_name_2 == "" or age == "" or weight == "" or height == ""):
        print ("Una o mas piezas de información esta vacía o esta escrita erroneamente por favor intenta de nuevo.")

    else:
        fields_filled = True

age = int(age)
weight = float(weight)
height = float(height)

idmc = weight / (pow(height, 2))

print(f"Hola {name} {last_name_1} {last_name_2}, mides {height}m, pesas {weight}kg y tu índice de masa corporal es de {idmc}")
