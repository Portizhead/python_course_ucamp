import matplotlib.pyplot as plt

#pedir al usuario las ventas de un rango de determinados años
year_inicio = int(input("dame el año inicial: "))
year_final = int(input("dame el año final: "))
years_rango = range(year_inicio, year_final + 1)
years_rango = list(years_rango)
# print(years_rango)
print(years_rango)
#pedir las ventas de cada año dentro del rango
ventas = []
for year in years_rango:
    venta = int(input(f"dame las ventas del {year}: "))
    ventas.append(venta)
#mostrar mediante una grafica de lineas las ventas de cada año


print(ventas)

plt.plot(years_rango, ventas)
plt.xticks(list(years_rango))
plt.yticks(list(ventas))
plt.xlabel('Año')
plt.ylabel('Ventas')
plt.title('Ventas por Año')
plt.show()


# plt.plot(list(years_rango), ventas, marker='o')  # Usar list(years_rango) para obtener la lista de años
# plt.xlabel('Año')
# plt.ylabel('Ventas')
# plt.title('Ventas por Año')
# plt.grid(True)

# # Personalizar el eje x para mostrar los años
# plt.xticks(list(years_rango))

# plt.show()