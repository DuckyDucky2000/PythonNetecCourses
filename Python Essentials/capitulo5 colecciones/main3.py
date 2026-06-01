#Diccionarios
paciente1 = {
    "nombre": "Paty",
    "edad": 25,
    "altura": 1.61,
    "tipo_sangre": "B+",
    "direccion": {
        "calle": "montecitos",
        "numero": 38,
        "colonia": "napoles"
    }
}

paciente2 = {
    "nombre": "Cris",
    "edad": 26,
    "altura": 1.70,
    "tipo_sangre": "A-",
    "direccion": {
        "calle": "cañitas",
        "numero": 10,
        "colonia": "spoooky"
    }
}

print(paciente1["edad"])
print(paciente2["direccion"])

pacientes = []
pacientes.append({"nombre": "Edgardo", "edad": 33})
pacientes.append({"nombre": "Cesar", "edad": 27})
pacientes.append({"nombre": "Nazmin", "edad": 24})
pacientes.append({"nombre": "Leonel", "edad": 6})
print(pacientes)

for i in pacientes:
    if i["nombre"].startswith("C"):
        print(i)
    '''if i["edad"]<18:
        print("El paciente", i["nombre"], "tiene solo", i["edad"], "años de edad")
    '''