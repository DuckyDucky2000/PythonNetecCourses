peliculas = [{"Nombre": "White Chicks", "Genero": "Comedy"},
             {"Nombre": "Your Name", "Genero": "Animation"},
             {"Nombre": "Pacific Rim", "Genero": "Sci-Fi"},
             {"Nombre": "The Dark Knight", "Genero": "Action"},
             {"Nombre": "Pulp Fiction", "Genero": "Action"},
             {"Nombre": "The Lord of the Rings: The Fellowship of the Ring", "Genero": "Fantasy"},
             {"Nombre": "Inception", "Genero": "Sci-Fi"},
             {"Nombre": "The Matrix", "Genero": "Sci-Fi"},
             {"Nombre": "The Godfather", "Genero": "Drama"},
             {"Nombre": "The Lion King", "Genero": "Animation"},
             {"Nombre": "The Avengers", "Genero": "Action"},
             {"Nombre": "The Silence of the Lambs", "Genero": "Thriller"},
             {"Nombre": "The Social Network", "Genero": "Drama"},
             {"Nombre": "The Dark Knight Rises", "Genero": "Action"}]

def mostrar_peliculas():
    print("Catálogo de películas:")
    for pelicula in peliculas:
        print(f"{pelicula['Nombre']} - Género: {pelicula['Genero']}")

if __name__ == "__main__":
    mostrar_peliculas()