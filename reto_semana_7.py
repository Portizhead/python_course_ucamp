lista = []
        
alumnos = 1


cantidad_de_alumnos = int(input("Cuantos alumnos quieres agregar a tu lista?: "))
print("Recuerda que debes agregar al menos una calificacion por alumno")

while alumnos <= cantidad_de_alumnos:
    opcion = input("Agregar alumno (1) o terminar (2): ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ").capitalize()
        
        es_numerica = False
        while not es_numerica:
            try:
                calificacion1 = float(input(f'Ingrese la primera calificación de {nombre}: '))
                es_numerica = True            
            except ValueError:
                print("Las calificaciones deben ser numericas.") 
        
        es_numerica = False
        while not es_numerica:
            try:
                calificacion2 = float(input(f'Ingrese la segunda calificación de {nombre}: '))
                es_numerica = True            
            except ValueError:
                print("Las calificaciones deben ser numericas.") 
                    
                    
        es_numerica = False
        while not es_numerica:
            try:
                calificacion3 = float(input(f'Ingrese la tercera calificación de {nombre}: '))
                es_numerica = True            
            except ValueError:
                print("Las calificaciones deben ser numericas.") 
                
                                                        
        alumno = [nombre, calificacion1, calificacion2, calificacion3]
        lista.append(alumno)
       
    
    elif opcion == "2":
        if  calificacion1 or calificacion2 or calificacion3:
            print(f"El programa ha terminado con {alumnos} alumnos. ")
            break
        else:
            print("Recuerda que debes agregar al menos una calificacion por alumno")
            continue
            
    else:
        print("Se ha ingresado una opcion invalida.")
        continue
    
    alumnos +=1

for alumno in lista:
        
    print(f"El promedio de {alumno[0]} es de {round(sum(alumno[1:])/len(alumno[1:]), 2)}")
    
        
