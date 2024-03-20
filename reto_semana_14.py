
with open("agenda.txt", "r") as archivo:    
    registros = []
    # print(archivo)
    for linea in archivo:
        registro = {}
        # print(linea)
        # print(linea.strip())
        # print(linea.split(", "))
        campos = linea.strip().split(", ")        
        for campo in campos:
            # print(campo.split(": "))
            key = campo.split(": ")[0]
            value = campo.split(": ")[1]
            # clave, valor = campo.split(": ") esta es otra sintaxis pero me saco un poco dudas
            # print(value)
            registro[key] = value
            
        registros.append(registro)   
    while True:
        try:    
            print("estos son los registros en la agenda: ")
            for i,registro in enumerate(registros, start=1):        
                print(f"{i}.- Nombre: {registro['Nombre']}, Edad: {registro['Edad']}, Correo: {registro['Correo']}, Telefono: {registro['Telefono']}")
            
            seleccion = int(input("Escribe el numero del registro que quieres editar: "))
            # print(len(registros)) = 3
            if seleccion > 0 and seleccion <= len(registros):
                print("Que campo quieres editar: ")
                # print(registros[seleccion - 1])
                campos2 = ", ".join(registros[seleccion - 1].keys())
                campos2_lista = campos2.split(", ")        
                campos2_lista.remove("Edad")
                # print(campos2_lista)        
                for i,opcion in enumerate(campos2_lista, start= 1):
                    print(f"{i}.- {opcion}")
                
                while True:
                    try:
                        opcion = int(input("Teclea el numero con de la opcion a editar: "))

                        if opcion == 1:
                            print(registros[seleccion - 1]['Nombre'])
                            nuevo_nombre = input("Que nuevo nombre le quieres asignar?: ")
                            registros[seleccion - 1]['Nombre'] = nuevo_nombre
                            print(registros[seleccion - 1]['Nombre'])
                            # registro['Nombre'] aqui tengo una duda, si ponia esta sintaxis me salia siempre el ultimo registro por que?
                        elif opcion == 2:
                            print(registros[seleccion - 1]['Correo'])
                            nuevo_correo = input("Que nuevo correo le quieres asignar?: ")
                            registros[seleccion - 1]['Correo'] = nuevo_correo
                            print(registros[seleccion - 1]['Correo'])
                        elif opcion == 3:
                            print(registros[seleccion - 1]['Telefono'])
                            nuevo_telefono = input("Que nuevo telefono le quieres asignar?: ")
                            registros[seleccion - 1]['Telefono'] = nuevo_telefono
                            print(registros[seleccion - 1]['Telefono'])
                        # print(f"{registros[seleccion - 1]}")
                        # campo_a_editar = input
                        break
                    except ValueError:
                        print("debe ingresarse un numero")
                break
        except ValueError:
            print("debe ingresarse un numero")

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



