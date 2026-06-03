'''
1. Importa la biblioteca random para seleccionar destinos de manera aleatoria.
2. Solicita al usuario que elija un tipo de viaje: aventura, playa o ciudad.
3. Utiliza condicionales (if/elif/else) para evaluar la elección del usuario.
4. Selecciona un destino aleatorio de una lista específica según el tipo de viaje.
5. Muestra el resultado con un mensaje amigable
6. Finaliza el programa con un mensaje motivador.
'''

import random
print("¡Bienvenido a tu planificador de viajes personalizado!")
print("¿Qué tipo de viaje te gustaría hacer? (1. aventura, 2. playa, 3. ciudad)")

tipo_viaje = input("Ingresa el número correspondiente a tu elección: ")
if tipo_viaje == "1":
    destinos_aventura = ["Machu Picchu, Perú", "Parque Nacional Torres del Paine, Chile", "Islas Galápagos, Ecuador"]
    destino_elegido = random.choice(destinos_aventura)
    print(f"¡Genial! Para una aventura inolvidable, te recomendamos visitar {destino_elegido}.")

elif tipo_viaje == "2":
    destinos_playa = ["Cancún, México", "Punta Cana, República Dominicana", "Maldivas"]
    destino_elegido = random.choice(destinos_playa)
    print(f"¡Perfecto! Para relajarte en la playa, te sugerimos visitar {destino_elegido}.")

elif tipo_viaje == "3":
    destinos_ciudad = ["París, Francia", "Tokio, Japón", "Nueva York, Estados Unidos"]
    destino_elegido = random.choice(destinos_ciudad)
    print(f"¡Excelente! Para explorar una ciudad vibrante, te recomendamos visitar {destino_elegido}.")
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")