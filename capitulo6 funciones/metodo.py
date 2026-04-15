
def multiplicar(a, b):
    resultado = a * b
    #print(resultado)
    return resultado

multiplicar(10,5)
valor_retornado = multiplicar(5,3)
#print(valor_retornado+10)

def division(a, b):
    div = a / b
    return div

respuesta = division(15,3)
#print(respuesta)

'''
Aplicación insertar_paciente, existe_paciente (True, False), buscar_paciente
'''

pacientes = []
def insertar_paciente(nombre):
        pacientes.append(nombre)
        print("Paciente insertado")
'''
respuesta = "si"
while respuesta != "no":
    dato_de_entrada = input("Escribe nombre paciente: ")
    insertar_paciente(dato_de_entrada)
    respuesta = input("¿Falta algun paciente? ")'''

print(pacientes)

def existe_paciente(nombre):
    for i in pacientes:
        if i.upper()== nombre.upper():
            return True

print(valor_retornado)
insertar_paciente("Luis")
insertar_paciente("Ana")
insertar_paciente("Juan")
insertar_paciente("Lola")
valor_retornado = existe_paciente("Juan")
print(valor_retornado)