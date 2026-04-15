# Listas, tuplas, colecciones

'''Listas => list = []
'''

#Lista para almacenar nombres de pacientes

pacientes = ["Paloma", "Ana", "Cece", "Alan", "Paco"]

pacientes.append("Alejandra")

'''
print(pacientes)
respuesta = "si"
while respuesta != "no":
    formulario = input("Nombre del paciente: ")
    pacientes.append(formulario)
    respuesta = input("¿Faltan pacientes? ")
print(pacientes)
'''

# modificando
pacientes[2] = "Luis"
print(pacientes)

#poscion de x valor
print("Alejandra es el paciente #", pacientes.index("Alejandra"))

#eliminar elemento de lista
pacientes.remove("Paloma")
print("Eliminando a Paloma...", pacientes)


#Procesar datos de lista
print()
datos=["Cesar", "Luis", "Carla", "Cynthia"]
#Procesando for
'''for i in datos:
    datos =i.upper()

print(datos)
'''

print(datos)

lista_resultado = [i.upper() for i in datos if i.endswith("a")]
print(lista_resultado)
print(datos)