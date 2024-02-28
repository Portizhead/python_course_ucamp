#en este archivo se van a crear las listas
#el usuario puede crear varias listas
#puede especificar la longitud de cada lista





def crear_listas(listas):
    main_lista = []

    for i in range(listas):    
        tamanio = int(input(f"De que tamaño sera la lista # {i+1}?: "))
        lista = []
        
        for j in range(tamanio):
            valor = input(f"Dame el valor # {j+1} de tu lista # {i+1}: ")
            lista.append(valor)

        # print(lista)
        main_lista.append(lista)
    
    return(main_lista)        
    
# print(crear_listas(listas))    
    