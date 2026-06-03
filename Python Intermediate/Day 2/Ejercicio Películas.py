'''
*Objetivo 🎯 **
Realizar un programa que realice la recomendación de películas considerando la edad del usuario,
si es mayor o igual de 18 años le recomendará un título y si es menor de 18 le recomendará
otro tipo de película.

Nota: Utiliza condicionales como los son if, elif, else y la anidación de estas condicionales.
Para limpiar las entradas del usuario te puedes apoyar de los métodos strip y lower.
Los generos a considerar son : Acción, Comedia, Drama, Terror.
Los títulos de las películas quedan a tu consideración.

'''
import random

terror = ["El Conjuro", "It", "El Exorcista", "La Noche del Demonio"]
terror_menores = ["Coraline", "Monster House", "Goosebumps", "The Nightmare Before Christmas"]
accion = ["Avengers: Endgame", "Mad Max: Fury Road", "John Wick", "Gladiator"]
accion_menores = ["Spider-Man: Into the Spider-Verse", "The Incredibles", "Big Hero 6", "How to Train Your Dragon"]
comedia = ["Superbad", "The Hangover", "Step Brothers", "Anchorman"]
comedia_menores = ["Despicable Me", "Shrek", "The Lego Movie", "Finding Nemo"]
drama = ["The Shawshank Redemption", "Forrest Gump", "The Godfather", "Fight Club"]
drama_menores = ["The Lion King", "Up", "Inside Out", "Coco"]


edad = int(input("¿Cuantos años tienes? "))
genero = input("¿Qué tipo de película te gusta? (Acción, Comedia, Drama, Terror) ").strip().lower()

if edad >= 18:
    if genero == "acción":
        print(f"Te recomendamos la película: {random.choice(accion)}")
    elif genero == "comedia":
        print(f"Te recomendamos la película: {random.choice(comedia)}")
    elif genero == "drama":
        print(f"Te recomendamos la película: {random.choice(drama)}")
    elif genero == "terror":
        print(f"Te recomendamos la película: {random.choice(terror)}")
    else:
        print("Género no reconocido. Por favor elige entre Acción, Comedia, Drama o Terror.")
else:
    if genero == "acción" or genero == "accion":
        print(f"Te recomendamos la película: {random.choice(accion_menores)}")
    elif genero == "comedia":
        print(f"Te recomendamos la película: {random.choice(comedia_menores)}")
    elif genero == "drama":
        print(f"Te recomendamos la película: {random.choice(drama_menores)}")
    elif genero == "terror":
        print(f"Te recomendamos la película: {random.choice(terror_menores)}")
    else:
        print("Género no reconocido. Por favor elige entre Acción, Comedia, Drama o Terror.")