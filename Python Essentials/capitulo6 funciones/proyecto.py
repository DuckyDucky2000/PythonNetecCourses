pacientes = []

pacientes.append({#paciente1
    "nombre": "Paty",
    "edad": 25,
    "altura": 1.61,
    "peso": 70,
    "tipo_sangre": "B+",
})

pacientes.append({#paciente2
    "nombre": "Cris",
    "edad": 26,
    "altura": 1.72,
    "peso": 85,
    "tipo_sangre": "O-",  
})

pacientes.append({#paciente3
    "nombre": "Gus",
    "edad": 25,
    "altura": 1.65,
    "peso": 75,
    "tipo_sangre": "A-",
})

pacientes.append({#paciente 4
    "nombre": "Aura",
    "edad": 24,
    "altura": 1.71,
    "peso": 90,
    "tipo_sangre": "AB",  
})

def menu():
    print("1. Mostrar Pacientes (todos)")
    print("2. Buscar Paciente")
    print("3. Calcular IMC")
    print("4. Insertar paciente")


def mostrar_pacientes():
    for i in pacientes:
        print(i)

def buscar_paciente():
    nombre = input("¿A quién buscas? ")
    for i in pacientes:
        if i["nombre"].upper()== nombre.upper():
            print(i)
            return i

def calcular_imc():
    #INVOCAR BUSCAR PARA SABER DE QUIEN ES EL IMC
    paciente_a_calcular = buscar_paciente()

    imc = paciente_a_calcular["peso"]/(paciente_a_calcular["altura"]**2)
    rounded_imc = round(imc,2)
    #print("IMC:",rounded_imc)

    if rounded_imc < 18.5:
        print("IMC:", rounded_imc, "- peso bajo")
    elif rounded_imc > 18.5 and rounded_imc < 24.9:
        print("IMC:", rounded_imc, "- normal")
    elif rounded_imc > 25.0 and rounded_imc < 29.9:
        print("IMC:", rounded_imc, "- sobrepeso")
    elif rounded_imc > 30.0 and rounded_imc < 34.9:
        print("IMC:", rounded_imc, "- obesidad I")
    elif rounded_imc > 35.0 and rounded_imc < 39.9:
        print("IMC:", rounded_imc, "- obesidad II")
    else:
        print("IMC:", rounded_imc, "- obesidad III")

def insertar_paciente():
    pacientes.append({"nombre": input("Nombre: "), "edad": int(input("Edad: ")), "altura": float(input("Altura: ")), "peso": float(input("Peso")), "tipo_sangre": input("Tipo de Sangre")})

respuesta = "si"
while respuesta != "no":
    menu()
    opcion = int(input(" --------- Escoge una opción: --------- "))
    if opcion == 1:
        print ("Mostrar todos")
        mostrar_pacientes()
    elif opcion == 2:
        print("Buscar paciente (por nombre)")
        buscar_paciente()
    elif opcion == 3:
        print("Calculo IMC")
        calcular_imc()
    elif opcion == 4:
        print("Insertar paciente")
        insertar_paciente()
    else:
        print("Error!")
    respuesta = input("¿Falta algo por hacer? ")