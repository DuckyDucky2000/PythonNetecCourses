def saludo (nombre):
    '''
    Recibe nombre y le saluda

    Parámetros:
    nombre (str): Nombre del usuario

    Retorna:
    El saludo completo
    '''

    texto = ("Hola " + nombre)

    return texto

print(saludo("Paty"))
#print(saludo.__doc__)

help(saludo)