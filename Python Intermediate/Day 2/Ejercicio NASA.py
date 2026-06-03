'''
Ejercicio: Contador regresivo para la NASA.
Objetivo 🎯 Realiza un programa para la NASA que sea su contador regresivo para que su cohete pueda despegar.
Nota: Haz uso del ciclo while y además que la NASA pueda escoger a partir del número que deseen iniciar en su cuenta regresiva.
'''

import time

def contador_regresivo():
    numero_inicial = int(input("¿Dónde empieza el conteo regresivo? "))
    while numero_inicial >= 0:
        print(numero_inicial)
        time.sleep(1)
        numero_inicial -= 1
    print("¡Despegue! 🚀")

#contador_regresivo()

# Otra forma de hacerlo con un ciclo for
#for i in 1,2,3,4,5:
#    print(i)

#range(valor_inicial, valor_final, tamaño_del_saltos)
#for i in range(2, 20): # inicia en 2, termina en 19 y va de 1 en 1
#    print(i)

#for i in range(10, 0, -1): # inicia en 10, termina en 1 y va de -1 en -1
#    print(i)
#    time.sleep(1)
#print("¡Despegue! 🚀")



#Ejercicio tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(int(input("¿De qué número quieres la tabla de multiplicar? ")))
