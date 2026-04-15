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

# ---------------------------- Validar datos ----------------------------------- #

def obtener_entero(mensaje):
    numero = 0
    try:
        numero = int(input(mensaje))
        return numero
    except:
        print("------- Error! Formato incorrecto -------\n Intentalo de nuevo. Ej: 25")
        obtener_entero(mensaje)
    

def obtener_flotante(mensaje):
    numero = 0

    try:
        numero = float(input(mensaje))
        return numero
    except: 
        print("------- Error! Formato incorrecto. ------- \n Intentalo de nuevo. Ej: 1.62")
        obtener_flotante(mensaje)

def edad_valida(mensaje):
    edad = obtener_entero(mensaje)
    if edad > 0 and edad < 122:
            return edad
    else: 
        print("------- Edad no valida ------- \n Es IMPOSIBLE que tu edad sea -x, 0 o >122")
        edad_valida(mensaje)

def peso_valido(mensaje):
    peso = obtener_flotante(mensaje)
    if peso > 0 and peso < 635:
            return peso
    else: 
        print("------- Peso no valido ------- \n Es IMPOSIBLE que tu peso sea -x, 0 o >635")
        peso_valido(mensaje)

def altura_valida(mensaje):
    altura = obtener_flotante(mensaje)
    if altura > 0 and altura < 2.72:
        return altura
    else: 
        print("------- Altura no valida ------- \n Es IMPOSIBLE que tu altura sea -x, 0 o >2.72")
        altura_valida(mensaje)
        
# -------------------------- Funciones principales ------------------------ #
def menu():
    print("----------- Bienvenido al registro de pacientes----------- \n ¿Qué deseas hacer hory")
    print("1. Mostrar Pacientes (todos) \n 2. Buscar Paciente\n3. Calcular IMC\n4. Insertar paciente")

    opcion = obtener_entero("Escoge una opción: ")
    if opcion == 1:
        print("----------- Mostrar todos los pacientes -----------")
        mostrar_pacientes()
    elif opcion == 2:
        print("----------- Buscar paciente (por nombre) -----------")
        buscar_paciente()
    elif opcion == 3:
        print("----------- Calculo IMC -----------")
        calcular_imc()
    elif opcion == 4:
        print("----------- Insertar paciente -----------")
        insertar_paciente()
    else:
        print("Error!")

def mostrar_pacientes():
    for i in pacientes:
        print(i)

def buscar_paciente():
    nombre = input("¿A quién buscas? ")
    existente = None
    for i in pacientes:
        if i["nombre"].upper()== nombre.upper():
            print(i)
            existente = i
            return i
    if existente == None:
        print("Usuario no encontrado \n ---- ¿Qué quieres hacer ahora? ----")
        intento = obtener_entero("1. Intentarlo otra vez \n2. Volver al menu ")
        if intento == 1:
            buscar_paciente()
        elif intento == 2:
            menu()
        else:
            print("Opcion no valida")

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
    pacientes.append({
        "nombre": input("Nombre: "),
        "edad": edad_valida("Edad: "),
        "altura": altura_valida("Altura (mts): "),
        "peso": peso_valido("Peso (kgs): "),
        "tipo_sangre": input("Tipo de Sangre: ")
    })

respuesta = "si"
while respuesta != "no":
    menu()
    '''
    opcion = obtener_entero("Escoge una opción: ")
    if opcion == 1:
        print("Mostrar todos")
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
    '''
    respuesta = input("¿Falta algo por hacer? ")