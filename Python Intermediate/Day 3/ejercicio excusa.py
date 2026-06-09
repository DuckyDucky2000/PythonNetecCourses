import random

def generar_excusa():
    perpetrador = ["Mi perro", "Mi gato", "Mi vecino", "Mi jefe", "Mi amigo", "Mi hermana"]
    crimen = ["se comió", "rompió", "perdió", "olvidó", "manchó", "destruyó"]
    victima = ["mi tarea", "mi proyecto", "mi presentación", "mi informe", "mi trabajo", "mi computadora"]

    excusa = f"{perpetrador[random.randint(0, len(perpetrador)-1)]} {crimen[random.randint(0, len(crimen)-1)]} {victima[random.randint(0, len(victima)-1)]}."
    return excusa


#print("Generador de excusas:")
#print(generar_excusa())
'''
import platform
print("Versión de sistema operativo:", platform.version())
print("Información de plataforma:", platform.platform())
print("Procesador:", platform.processor())
print("Máquina:", platform.machine())

print("Versión de Python:", platform.python_version())
print("Versión de Python completa:", platform.python_version_tuple())
'''
'''

'''
def formato():
    correo = "example@test.com"
    usuario, dominio = correo.split("@")
    print("Usuario:", usuario)
    print("Dominio:", dominio)

    print("Wiston Churchill dijo: \"Manten la calma y continua.\"")
    print("El símbolo de porcentaje se representa entre comillas diferentes. Ej 50'%'")

    print("Nombre\tEdad\tCiudad")
    print("Alicia\t30\tNew York")
    print("Bob\t25\tLos Angeles\nCharlie\t35\tChicago")
    print("Lista de compras:\n- Leche\n- Pan\n- Huevos")
    print("Lista de compras:\n* Leche\n* Pan\n* Huevos")

    print("Linea 1\vLinea 2\vLinea 3")

    print("C:\\Users\\Usuario\\Documentos")