# Calculadora de precio

iva = 0.16
descuento = 0.10

precio = float(input("¿Cuanto cuesta el producto que quieres? "))

print(precio)
precio_con_descuento = precio - precio*descuento
precio_con_iva = precio_con_descuento + precio_con_descuento*iva



print ("El producto cuesta $" , precio , "\nCon IVA: $" , precio_con_iva , "\nPrecio con descuento: $", precio_con_descuento)

#Calculadora de peso (N)

gravedad_terrestre = 9.8#m/s^2
gravedad_lunar = 1.62#m/s^2
gravedad_marciana = 3.71#m/s^2
gravedad_venusina = 8.87#m/s^2


masa = float(input("¿Cuánto pesas (kgs)? "))

peso_terrestre = gravedad_terrestre * masa
peso_lunar = gravedad_lunar * masa
peso_marciano = gravedad_marciana * masa
peso_venusino = gravedad_venusina * masa

print("Ya que la gravedad en la Tierra es" , gravedad_terrestre, "m/s^2. Tu peso es" , peso_terrestre , "N")
print("Ya que la gravedad en la Luna es" , gravedad_lunar, "m/s^2. Tu peso sería" , peso_lunar , "N")
print("Ya que la gravedad en Marte es" , gravedad_marciana, "m/s^2. Tu peso sería" , peso_marciano , "N")
print("Ya que la gravedad en Venus es" , gravedad_venusina, "m/s^2 Tu peso sería" , peso_venusino , "N")