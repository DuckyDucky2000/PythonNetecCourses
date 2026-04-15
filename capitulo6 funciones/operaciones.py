#Para reutilizar código en partes de un proyecto

#Si no retorna valor
'''
def nombre_funcion(argumentos):
    código
'''


def calcular_factorial():
    respuesta = "si"
    while respuesta != "no":
        numero= int(input("Numero: "))
        factorial= int(input("Factorial: "))
        while numero > 0:
            factorial = factorial * numero
            numero = numero - 1 
        print(factorial)
        respuesta = input("¿Quieres probar otra combinación? si/no ")

def calcular_suma():
    a = int(input("Valor 1: "))
    b = int(input("Valor 2: "))
    suma = a + b
    print(suma)