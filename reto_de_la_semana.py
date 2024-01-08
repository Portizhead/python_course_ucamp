# 1. Que solicite al usuario el año actual y un año cualquiera. 
# 2. Que despliegue en la pantalla cuántos años han pasado desde el año ingresado hasta el actual o cuántos años faltan para llegar a ese año. Ten en cuenta que si solo falta o ha pasado un año, debe mostrar un mensaje adecuado. 
# 3. Que notifique si se ha ingresado dos veces el mismo año. 
# 4. La salida de tu programa debe parecerse a la siguiente

año_actual = int(input("Introduce el año actual: "))
otro_año = int(input("Introduce otro año para calcular: "))

if año_actual > otro_año:
    if año_actual - otro_año == 1:
        print(f"Desde el año {otro_año} ha pasado 1 año")
    else:    
        print(f"Han pasado {año_actual - otro_año} años desde el año que has introducido ")

elif año_actual < otro_año:
    if otro_año - año_actual == 1:
        print(f"Para llegar a {otro_año} hace falta 1 año")
    else:    
        print(f"Faltan {otro_año - año_actual } años para llegar al año que has introducido ")

elif año_actual == otro_año:
    print("Has introducido el mismo año que el actual")
