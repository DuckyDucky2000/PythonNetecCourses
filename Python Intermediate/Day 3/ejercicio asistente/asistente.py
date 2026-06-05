'''
🟢 Práctica — Creación de un Módulo en Python
🎯 Objetivo
    Aprender a:
    * crear módulos en Python,
    * importar módulos,
    * usar la función dir(),
    * documentar funciones con docstrings,
    * utilizar help() y __doc__.

📌 Instrucciones
    1️⃣ Crear un archivo llamado:
        asistente.py
    Dentro de este archivo deberán crear las siguientes funciones:

    saludar(nombre)
    despedirse(nombre)
    motivar()
    estado()
    preguntar_edad()


📌 Requisitos importantes
    ✅ Todas las funciones deben tener documentación (docstring).
    ✅ El docstring debe explicar:
        qué hace la función, parámetros, qué retorna.
    ✅ Todas las funciones deben retornar mensajes.

📌 Ejemplo de estructura
    def ejemplo():
        #Explicación de la función.
        #funcion
        return "Hola"
'''

def saludar(nombre):
    """
    Función para saludar a una persona.
    Parámetros:
        nombre (str): El nombre de la persona a saludar.
    Retorna:
        str: Mensaje de saludo.
    """
    return f"Hola, {nombre}! Bienvenido al asistente virtual."

def despedirse(nombre):
    """
    Función para despedirse de una persona.
    Parámetros:
        nombre (str): El nombre de la persona a despedirse.
    Retorna:
        str: Mensaje de despedida.
    """
    return f"Adiós, {nombre}! Que tengas un buen día."


def motivar():
    """
    Función para generar un mensaje de motivación.
    Parámetros:
        Ninguno.
    Retorna:
        str: Mensaje de motivación.
    """
    import random
    mensajes_motivadores = [
        "¡Sigue adelante! ¡Tú puedes lograrlo!",
        "¡No te rindas! Cada paso cuenta.",
        "¡Cree en ti mismo!\nEres capaz de lograr grandes cosas.",
        "¡El éxito está a tu alcance!\nSolo tienes que seguir intentándolo."
        "¡Cada día es una nueva oportunidad para crecer y mejorar!"
    ]
    mensaje = random.choice(mensajes_motivadores)

    return mensaje


def estado(animo):
    """
    Función para generar un mensaje basado en el estado de ánimo.
    Parámetros:
        animo (str): El estado de ánimo de la persona (feliz, triste, cansado).
    Retorna:
        str: Mensaje basado en el estado de ánimo.
    """
    if animo.lower() == "bien":
        return "¡Me alegra saber que estás bien! ¡Sigue disfrutando tu día!"
    elif animo.lower() == "mal":
        return "Lamento oír eso.\n" + motivar() + "\nRecuerda que después de la tormenta siempre llega la calma."
    else:
        return "No reconozco ese estado de ánimo. ¡Espero que estés bien!"

def preguntar_edad():
    """
    Función para preguntar la edad de una persona.
    Parámetros:
        Ninguno.
    Retorna:
        str: Mensaje preguntando la edad.
    """
    edad = int(input("¿Cuántos años tienes? "))
    return f"¡Gracias por compartir tu edad!\nTienes {edad} años, una edad maravillosa para aprender y crecer."
