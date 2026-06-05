'''
sugerencias.py
Crear una función llamada:

recomendar()
La función deberá mostrar una recomendación de película.

'''
import Peliculas.catalogo as catalogo
import Usuarios.perfiles as perfiles
import random

def recomendar():
    if not perfiles.usuarios:
        print("No hay usuarios registrados.\nPor favor, agrega un usuario para obtener recomendaciones.")
        return

    usuario = random.choice(perfiles.usuarios)
    favs = usuario["Favs"]
    recomendacion = None

    for pelicula in catalogo.peliculas:
        if pelicula["Genero"] in favs:
            recomendacion = pelicula
            break

    if recomendacion:
        print(f"Recomendación para {usuario['Nombre']}: {recomendacion['Nombre']} - Género: {recomendacion['Genero']}")
    else:
        print(f"No se encontraron recomendaciones para {usuario['Nombre']}.")
    
if __name__ == "__main__":
    recomendar()