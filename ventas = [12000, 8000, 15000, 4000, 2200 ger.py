ventas = [12000, 8000, 15000, 4000, 22000, 7000, 10000]

ventas_bajas = 0
ventas_medias = 0
ventas_altas = 0

for i in range(len(ventas)):
    venta = ventas[i]

    print("Venta", i+1, ":", venta)

    if venta < 7000:
        print("Venta baja")
        ventas_bajas += 1

    elif 7000 <= venta <= 15000:
        print("Venta media")
        ventas_medias += 1

    else:
        print("Venta alta")
        ventas_altas += 1

print("Ventas bajas:", ventas_bajas)
print("Ventas medias:", ventas_medias)
print("Ventas altas:", ventas_altas)