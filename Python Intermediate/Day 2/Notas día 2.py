#IF-ELSE
def promedio_estudiante():
    estudiante  = input("Nombre: ")
    matematicas = float(input("Calificación de matemáticas: "))
    quimica     = float(input("Calificación de química: "))
    biologia    = float(input("Calificación de biología: "))

    promedio = (matematicas + quimica + biologia) / 3

    if promedio >= 6:
        print(f"Felicidades {estudiante}, has aprobado con un promedio de {promedio:.2f}.")
    else:
        print(f"Lo siento {estudiante}, has reprobado con un promedio de {promedio:.2f}.")

#promedio_estudiante()

#saber si un numero es par o impar

def es_par(numero):
    numero = int(input("Ingresa un numero entero"))
    if (numero % 2) == 0:
        print(f"El numero: {numero} es par")
    else:
        print(f"El numero: {numero} es impar")

#es_par()

#Calculadora de descuentos (elegir el monto minimo para descuento)
def calculadora_descuentos():
    print("El valor minimo para descuento es de 350 pesos")
    precio = float(input("Ingresa el costo de tu prenda: "))

    if precio >= 350:
        print(f"Tu descuento es de: {precio*.10}.")
        precio = precio*.90
        print(f"Tu precio final es de: {precio}.")
    else:
        print("Agrega mas productos para tener un descuento.")

#calculadora_descuentos()



#iF-ELIF-ELSE
def votar_o_beber_USA():
    edad = int(input("¿Cuántos años tienes? "))
    if input("¿Eres ciudadano americano? (si/no) ").strip().lower() == "si":
        gringo = True
    else:
        gringo = False

    print("\n")

    if edad >= 21 and gringo:
        print("Eres mayor de edad y ciudadano americano, puedes votar y beber alcohol.\n")
    elif edad >= 21:
        print("Eres mayor de edad pero no eres ciudadano americano, no puedes votar.\n")
    elif edad >= 18 and gringo:
        print("Eres ciudadano americano mayor de edad, puedes votar, pero no puedes beber alcohol.\n")
        print(f"Te faltan {21 - edad} años para poder beber alcohol en Estados Unidos.\n")
    elif edad >= 18:
        print("Eres mayor de edad pero no eres ciudadano americano, no puedes votar.\nNo puedes beber alcohol en Estados Unidos, aunque en tu país legalmente podrías hacerlo.\n")
        print(f"Te faltan {21 - edad} años para poder beber alcohol en Estados Unidos.\n")
    else:
        print("No eres ciudadano americano ni eres mayor de edad, no puedes votar (en USA).\n")
        print(f"Te faltan {21 - edad} años para poder beber alcohol en Estados Unidos.\n")

#votar_o_beber_USA()

# ----------------- Rutas cross if-else ------------------

def ruta_cross_if_else():
    x = 5
    y = -5

    if x > 0:
        print("x es positivo")
        if y > 0:
            print("y también es positivo")
        else:
            print("y es negativo")
    else:
        print("x es negativo")
        if y > 0:
            print("y es positivo")
        else:
            print("y también es negativo")

#ruta_cross_if_else()

# ------------------------ Contador ---------------------------
numero = 0
while numero <= 5:
    print(numero)
    numero += 1

print("¡Contador terminado!")