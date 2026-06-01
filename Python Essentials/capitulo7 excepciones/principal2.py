def obtener_numero_entero(mensaje):
    numero = 0
    try:
        numero = int(input(mensaje))
        return numero
    except:
        print("------- Error! Formato incorrecto -------\n Intentalo de nuevo. Ej: 25")
        numero = obtener_numero_entero(mensaje)
        return numero


def obtener_numero_flotante(mensaje):
    numero = 0

    try:
        numero = float(input(mensaje))
        return numero
    except: 
        print("------- Error! Formato incorrecto. ------- \n Intentalo de nuevo. Ej: 1.62")
        numero = obtener_numero_flotante(mensaje)
        return numero

pacientes = []

paciente = {
    "nombre": input("Nombre: "),
    "edad": obtener_numero_entero("Edad: "), # esto se vuelve el mensaje de: funcion(mensaje)
    "altura": obtener_numero_flotante("Altura (mts): ") #funcion(mensaje)
}
'''
if paciente["edad"] <= 0:
    obtener_numero_entero("La edad actual no es valida, intentalo otra vez: ")

if paciente["altura"] <= 0:
    obtener_numero_flotante("La altura actual no es valida, intentalo otra vez: ")
'''

print(paciente)
