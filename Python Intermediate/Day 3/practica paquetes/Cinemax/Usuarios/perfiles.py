'''
perfiles.py
Crear una función llamada:

mostrar_usuario()
La función deberá mostrar el nombre de un usuario.
'''
usuarios = [{"Nombre": "Angel",
             "Favs": ["Comedy", "Action"]},
            {"Nombre": "Maria",
             "Favs": ["Drama", "Thriller"]}]

generos = {1: "Comedy", 2: "Action", 3: "Drama", 4: "Thriller", 5: "Sci-Fi", 6: "Fantasy", 7: "Animation"}

def mostrar_usuarios(nombre_usuario):
    for usuario in usuarios:
        if usuario["Nombre"] == nombre_usuario:
            print(f"Usuario: {usuario['Nombre']}")
            print(f"Géneros favoritos: {', '.join(usuario['Favs'])}")
            return usuario
    print("Usuario no encontrado.")
    return None

def agregar_usuario(nombre, favs):
    usuarios.append({"Nombre": nombre, "Favs": [favs]})
    