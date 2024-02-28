import m_eliminar 
import m_listas 

listas = int(input("Cuantas listas quieres crear?: "))

main_lista = m_listas.crear_listas(listas)
print(main_lista)

print(f"Listas despues de eliminar los repetidos en listas siguientes: {m_eliminar.eliminar_repetidos(main_lista)}")