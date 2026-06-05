def definir_matriz(filas, columnas):
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matriz[1][2])  # Imprime el elemento en la fila 1, columna 2 (6)
    print(matriz)
    print(matriz[0])  # Imprime la primera fila de la matriz

    for fila in matriz:
        print(fila) # Imprime cada fila de la matriz

    numeros = [1,2,3,4,5]
    pares = [x for x in numeros if x % 2 == 0]
    print(pares)

    dobles = [x * 2 for x in numeros]
    print(dobles)

    print("Usando un bucle for para crear una lista de dobles:")
    dobles = []
    for x in numeros:
        dobles.append(x * 2)
    print(dobles)

#definir_matriz()

def longitud_matriz():
    palabras = ["hola", "mundo", "python"]
    palabras_largas = [palabra for palabra in palabras if len(palabra) > 4]
    print(palabras_largas)

    words = ["Marisol", "Ana", "Sofía", "Lucía", "Valentina",
            "Isabella", "Camila", "Valeria", "Gabriela", "Daniela",
            "Luz", "Sofía", "María", "Fernanda", "Ximena", "Victoria",
            "Tom", "Santiago", "Matías", "Sebastián", "Diego", "Emiliano",
            "Miguel", "Joaquín", "Andrés", "Alejandro", "Pablo", "Lucas",
            "Diego", "Bruno", "Martina", "Renata"
            ]

    tres_letras = [word for word in words if len(word) == 3]
    print(tres_letras)

#longitud_matriz()