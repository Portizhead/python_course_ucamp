#eliminar elementos de una lista que esten tambien en las listas posteriores

lista_A = ["a","b","c","d"]
lista_B = ["c","d","e","f"]
lista_C = ["a","e","g","h"]
lista_D = ["h","i","j","k"]


# #leer las listas
main_lista = [["a","b","c","d"], ["c","d","e","f"]]


# def verificar_interseccion(main_lista):
#     num_de_listas = len(main_lista)
#     repetidos = []
    
#     for i in range(num_de_listas):
#         lista_actual = main_lista[i]
#         repetidos_actual = []
        
#         for j in range(num_de_listas):
#             if i != j:
#                 otra_lista = main_lista[j]
#                 for elemento in lista_actual:
#                     if elemento in otra_lista:
#                         repetidos_actual.append(elemento)
                
#         repetidos.append(repetidos_actual)
    
#     return(repetidos)
            

# print(verificar_interseccion(main_lista)) #expected output: [a,c,d,e]


def eliminar_repetidos(main_lista):
    num_de_listas = len(main_lista)
    main_lista_nueva = []
    for i in range(num_de_listas):
        sig = i + 1
        if sig < num_de_listas:
            lista_nueva = []
            lista_actual = main_lista[i]
            lista_siguiente = main_lista[sig]
            for elemento in lista_actual:
                if elemento not in lista_siguiente:
                    lista_nueva.append(elemento)

            main_lista_nueva.append(lista_nueva)
        else:
            break
    
    return(main_lista_nueva)

print(f"Listas despues de eliminar los repetidos en listas siguientes: {eliminar_repetidos(main_lista)}")