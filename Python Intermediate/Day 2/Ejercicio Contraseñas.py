'''
Práctica: Sistema de Verificación de Contraseña
**Objetivo General: **
Desarrollar un programa en Python que verifique la contraseña ingresada por el usuario,
permitiendo hasta tres intentos antes de denegar el acceso.

**Conceptos Clave: **
Variables y asignación de valores. Bucles y control de flujo (uso de while, else y condicionales).
Entrada y salida estándar.

Desafíos:
Inicialización: Define las variables necesarias para almacenar la contraseña correcta,
el número máximo de intentos, y un contador de intentos.

Bucle de Intentos: Implementa un bucle que repita la solicitud de ingreso de la contraseña hasta
que se alcance el número máximo de intentos o se ingrese la contraseña correcta.

Verificación: Dentro del bucle, compara la contraseña ingresada con la contraseña correcta. Si
coinciden, muestra un mensaje de éxito y termina el bucle.

Límite de Intentos: Si se supera el número de intentos permitidos sin acertar la contraseña,
informa al usuario que el acceso ha sido denegado.
'''
import time


def ingresar():
    contraseña_correcta = "Netec123"
    intentos_maximos = 5
    intentos = 0
    while intentos < intentos_maximos:
        contraseña_ingresada = input(f"Tienes {intentos_maximos} intentos.\nIngresa la contraseña: ")
        if contraseña_ingresada == contraseña_correcta:
            print("¡Contraseña correcta! Acceso concedido.")
            break
        else:
            intentos += 1
            print(f"Contraseña incorrecta. Te quedan {intentos_maximos - intentos} intentos.")
    else:
        print("Has superado el número máximo de intentos. Acceso denegado.")
        time.sleep(2)
        print("\nPuedes intentarlo otra vez")
        print("Te quedan 5 intentos.")
        ingresar()

ingresar()

