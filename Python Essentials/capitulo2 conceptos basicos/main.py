# comentario 1

'''
comentario multilinea 1
comentario multilinea 2
comentario multilinea 3
'''


nombre = "Paty"
edad = 25
altura =1.62
vivo = True
'''
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(vivo))

print("Nombre: " + nombre)
print("Edad: ", edad, " años")
print("Altura: ", altura, "mts")
print("Status, ¿vivo?: ", vivo)
'''

#almacenar info de consola
nombre2 = input("Escribe tu nombre: ")
print("Nombre:", nombre2)
#print(type(nombre2))
edad2 = int(input("Coloca tu edad: "))
#print("En 2027 tendrá:", edad2+2, "años")
#print(type(edad2))
altura2 = float(input("Coloca tu altura: "))
#print("Altura:", altura2, "mts")
#print(type(altura2))
vivo2 = bool(input("¿Tas vivo, carnal? (True/False) con mayuscula al principio: "))
#print("¿Vivo?:", vivo2)
#print(type(vivo2))

'''
Cadena donde se muestra la información general del cliente
Variables
    nombre2(str): Entrada de consola, nombre cliente
    edad2(int): Entrada de consola, edad cliente'''
print("Hola", nombre2, "tienes", edad2, "años, mides", altura2, "mts y que estes vivo es", vivo2)

peso = float(input("Peso /kgs)"))
imc = peso/(altura2*altura2)

print("IMC:",imc)