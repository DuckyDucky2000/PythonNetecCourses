#Estructuras de control
''' if-else: Permite elegir 2 caminos '''

#Scenario: ¿Medico normal o geriatra?
edad_paciente = int(input("Edad: "))
if edad_paciente>=60:
    print("Ir a geriatria")
else:
    print("Ir a medico general")

#Edad par o impar

edad = int(input("Edad:"))
operacion = edad % 2
if operacion == 0:
    print("Par")
else:
    print("Impar")

# if encadenado
#Crear una app que me diga la cantidad de un año que tiene un año
mes = input("Mes: ")
mes = mes.lower()

if mes=="enero" or mes=="marzo" or mes=="mayo" or mes=="julio" or mes=="agosto" or mes=="octubre" or mes=="diciembre":
    print("El mes de", mes.capitalize(), "tiene 31 días")
elif mes=="abril" or mes=="junio" or mes=="septiembre" or mes=="noviembre":
    print("El mes de", mes.capitalize(), "tiene 30 días")
elif mes=="febrero":
    print("El mes de", mes.capitalize(), "tiene 28 días, o 29 en año bisiesto")
else:
    print("Creo que lo escribiste mal, o quizás lo abreviaste, intenta otra vez")


# --------------------------- CICLOS ---------------------------

respuesta="si"
while respuesta != "no":
    numero = int(input("Escribe número: "))
    resultado = numero % 2
    if resultado == 0:
        print(numero, "es par")
    else:
        print(numero, "es impar")
    respuesta = input("¿Quieres continuar? ")

# --------------------------- for ---------------------------

for x in range(2):
    print("---- Contador:", x+1, "----")
    numero = int(input("Escribe número: "))
    resultado = numero % 2
    if resultado == 0:
        print(numero, "es par")
    else:
        print(numero, "es impar")