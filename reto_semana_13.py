# 
# 
# edad = int(input("Introduce tu edad: "))
# correo = input("Introduce tu correo: ")
# telefono = input("Introduce tu telefono: ")
# calificaciones = input("Introduce la cal")



nombre_default= "pepito"
calif_default = 5
alumnos = {}

def es_float(calif):
    try:
        float_numero = float(calif)
        return True
    except ValueError:
        return False

def promedio(calificaciones):
    lista_floats = []
    for numero in calificaciones:
        lista_floats.append(float(numero))
           
    suma_calificaciones = sum(lista_floats)
    promedio = suma_calificaciones / len(calificaciones)
    return promedio
        
        
while True:
    print("Presiona 1 para agregar un nuevo alumno.")
    print("Presiona 2 para ver los alumnos y las calificaciones.")
    print("Presiona S para salir.")
    eleccion = input()
    
    if eleccion == "1":
        while True:            
            nombre = input("Introduce su nombre y su apellido: ")
            if nombre == "":
                print("Tu nombre no puede ir en blanco.")
            elif nombre.isdigit() == True:
                print("El nombre no debe ser numerico.")
            else:
                break
        
        num_calif = int(input("Cuantas calificaciones quieres agregar?: "))
        calificaciones = []
        for i in range(num_calif):
            while True:          
                calif = input("Introduce su calificacion: ")
                # calif = float(calif)
                if calif == "":
                    print("Tu calif no puede ir en blanco.")
                elif es_float(calif) != True:
                    print("Tu calif debe ser numerica.")
                else:
                    break                
                
            
            calificaciones.append(calif)
        
        prom = promedio(calificaciones)       
                          
        alumnos[f'{nombre}'] = prom
########################################################################################################            
    elif eleccion == "2":
        print(alumnos)
        print(prom)
        
    elif eleccion == "s" or eleccion == "S":
        respuesta = input("Esta seguro que quiere cerrar el programa? presione s para si y n para no ")
        if respuesta == "S" or respuesta == "s":
            break
        elif respuesta == "N" or respuesta == "n":
            continue
        else:
            print("Tu eleccion no fue s ni n, escoge una de las opciones.")
    else:
        print("Tu eleccion no fue 1 ni 2 ni S, escoge una de las opciones.")
        
        
        
        
# while True:
#     try:
#         edad = int(input("Introduce tu edad: "))    
#         break
#     except ValueError:
#         print("Debes introducir un numero")        
        

# while True:
#     nombre = input("Introduce tu nombre: ")
#     apellido = input("Introduce tu apellido: ")
#     if nombre == "":
#         print("No has introducido tu nombre")
#     elif apellido == "":
#         print("No has introducido tu apellido")
#     else:
#         break        