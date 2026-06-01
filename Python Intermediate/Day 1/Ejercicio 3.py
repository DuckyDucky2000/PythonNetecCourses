#Concatenación - 

import random

adjetivos = ["Veloces", "Ruidosos", "Peligrosos", "Mentirosos", "Audaces", "Imaginarios", ""]
sustantivos = ["Leones", "Fantasmas", "Dragones", "Sistema", "Pánico", "Héroes", "Villanos", "Demonios"]
tematicas = ["del espacio", "en la Disco", "del Silencio", "Primaverales", ""]

for i in range(5):
    adjetivo = random.choice(adjetivos)
    sustantivo = random.choice(sustantivos)
    tematica = random.choice(tematicas)

    nombre_banda = sustantivo + " " + adjetivo + " " + tematica
    #print(nombre_banda)

'''
nombre = input("¿Cómo te llamas? ")
n = input("Número entero: ")

print((nombre + "\n") * int(n))
'''

#Operadores relacionales
x = 5
y = 10

def comparar(x, y):
    print("Comparando x =", x, "y y =", y)
    print("¿Iguales? x == y:", x == y) #False
    print("¿Diferentes? x != y:", x != y) #True
    print("¿Mayor? x > y:", x > y) #False
    print("¿Menor? x < y:", x < y) #True
    print("¿Mayor o igual? x >= y:", x >= y) #False
    print("¿Menor o igual? x <= y:", x <= y) #True

#comparar(x, y)

def operaciones_aritmeticas(x, y):
    print("Operaciones aritméticas con x =", x, "y y =", y)
    print("¿Suma? x + y:", x + y)
    print("¿Resta? x - y:", x - y)
    print("¿Multiplicación? x * y:", x * y)
    print("¿División? x / y:", x / y)
    print("¿División entera? x // y:", x // y) #División entera
    print("¿Módulo? x % y:", x % y) #Módulo o residuo
    print("¿Potencia? x ** y:", x ** y) #Potencia

#operaciones_aritmeticas(x, y)

def operaciones_logicas(x, y):
    print("Operaciones lógicas con x =", x, "y y =", y)
    print("¿AND? x > 0 and y > 0:", x > 0 and y > 0) #True
    print("¿OR? x < 0 or y > 0:", x < 0 or y > 0) #True
    print("¿NOT? not (x > 0):", not (x > 0)) #False

#operaciones_logicas(x, y)
a = b = 100
def operadores_de_identidad(a, b):
    print("Operadores de identidad con a =", a, "y b =", b, "\n")
    
    print("¿a es b? a is b:", a is b) #True
    print(id(a), id(b)) #Mismo id, porque a y b apuntan al mismo objeto en memoria
    print("¿a no es b? a is not b:", a is not b) #False
    b = 200
    print("\nDespués de cambiar el valor de b a 200:")
    print("¿a es b? a is b:", a is b) #False, ahora a y b son objetos diferentes
    print(id(a), id(b)) #Diferente id, porque a y b ahora apuntan a objetos diferentes
    print("¿a no es b? a is not b:", a is not b)


#Operadores de membresía
def operadores_de_membresia():
    print("Operadores de membresía\n")
    frutas = ["manzana", "banana", "naranja", "cereza", "uva"]
    print("Lista de frutas:", frutas)
    print("¿Está 'manzana' en la lista de frutas?", "manzana" in frutas) #True
    print("¿Está 'fresa' en la lista de frutas?", "fresa" in frutas) #False
    print("¿Está 'pera' en la lista de frutas?", "pera" not in frutas) #True

#operadores_de_membresia()

#Operadores de pertenencia
def operadores_de_pertenencia():   

    texto = "hola mundo"
    #print("¿Está 'hola' en el texto?", "hola" in texto) #True 
    
    print("Operadores de pertenencia\n")
    edades = {"Ana": 25, "Luis": 30, "Carlos": 34}
    print("Diccionario de edades:", edades)
    print("¿Está 'Luis' en el diccionario de edades?", "Luis" in edades) #True
    print("¿Está 'fresa' en el diccionario de edades?", "fresa" in edades) #False
    print("¿Hay alguien de 30 años en el diccionario de edades?", 30 in edades.values()) #True


#operadores_de_pertenencia()

print("Este", "es", "un", "mensaje")
print('Separador - sep="[valor]"')
print("Este", "es", "un", "mensaje", sep="-", end=".") #sep es el separador entre los argumentos, por defecto es un espacio