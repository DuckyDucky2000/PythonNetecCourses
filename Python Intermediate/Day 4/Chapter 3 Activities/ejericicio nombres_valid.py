''' Ejercicio: Validando nombres completos
Una empresa recibió una lista de empleados, pero algunos escribieron su nombre y apellido correctamente y otros olvidaron dejar un espacio entre ellos.

Lista recibida:
'''
nombres = [
    "Ana García",
    "CarlosLópez",
    "María Torres",
    "PedroRamírez",
    "Laura Sánchez"
]
'''
Necesitamos identificar qué registros contienen al menos un espacio para considerar que tienen nombre y apellido separados correctamente.
'''

import re
def validar_nombres(nombres):
    for nombre in nombres:
        if re.search(r"\s", nombre): #Busca un espacio en el nombre, devuelve un objeto de coincidencia si se encuentra, o None si no se encuentra.
            print(f"Correcto: {nombre}")
        else:
            print(f"**Error: {nombre}")