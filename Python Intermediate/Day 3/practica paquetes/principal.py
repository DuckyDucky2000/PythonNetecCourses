''' Práctica: Creación de Paquetes y Módulos en Python
Objetivo: Crear una estructura de paquetes y subpaquetes para una plataforma de streaming llamada CineMax, implementando módulos, funciones e importaciones.

Instrucciones:
1. Crear la siguiente estructura de carpetas y archivos: [Estructura de carpetas y archivos]
2. Crear las siguientes funciones: [Cada función debe estar en el módulo correspondiente según su temática]
'''

#3. Crear las siguientes importaciones
#Importación de una función
import Peliculas.catalogo as catalogo
#Importación de un módulo
import Usuarios.perfiles as perfiles
#Importación de una ruta completa
import Recomendaciones.sugerencias as sugerencias

#4. Ejecutar las funciones
#Desde principal.py ejecutar las tres funciones utilizando la sintaxis correspondiente para cada tipo de importación.

#5. Crear una función principal. Crear una función llamada:

def main():
    print("Bienvenido a CineMax. Escoge una opción:")
    opt = int(input("1. Mostrar películas\n2. Mostrar usuarios\n3. Mostrar recomendaciones\n"))
    if opt == 1:
        catalogo.mostrar_peliculas
    elif opt == 2:
        perfiles.mostrar_usuarios()
    elif opt == 3:
        sugerencias.recomendar()
    elif opt == 4: #Nuevo usuario
        nombre = input("Ingrese el nombre del nuevo usuario: ")
        for i in range(1, 8):
            fav_gen = input(f"¿Te gusta el género {perfiles.generos[i]}? (s/n): ")
            if fav_gen.lower() == 's':
                perfiles.agregar_usuario(nombre, perfiles.generos[i])
            elif fav_gen.lower() == 'n':
                continue

    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()

''' La función deberá ejecutar las tres funcionalidades del sistema en el siguiente orden:
    a. Mostrar películas.
    b. Mostrar usuario.
    c. Mostrar recomendación.

6. Proteger la ejecución principal
Utilizar la variable especial:

__name__
para ejecutar la función principal únicamente cuando el archivo sea ejecutado directamente.
'''

if __name__ == "__main__":
    main()

