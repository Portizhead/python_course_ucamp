print("***   Calculadora de Indice de Masa Corporal   ***")

fields_filled = False

while fields_filled == False: 

    name = input("Por favor ingresa tu nombre: ")

    last_name_1 = input("Por favor ingresa tu apellido paterno: ")

    last_name_2 = input("Por favor ingresa tu apellido materno: ")

    age = input("Por favor ingresa tu edad: ")

    weight = input("Por favor ingresa tu peso: ")

    height = input("Por favor ingresa tu estatura: ")

    if (name == "" or last_name_1 == "" or last_name_2 == "" or age == "" or weight == "" or height == ""):
        print ("one of your data is empty please fill all the data")
    else:
        fields_filled = True


weight = float(weight)
height = float(height)

idmc = weight / (pow(height, 2))
