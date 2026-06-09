def analisis_cadenas():
    print("Bienvenido a la práctica del día 4: Indexación y Slicing".capitalize())
    print("SIN DUDA NO HAY PROGRESO".lower())
    print("QuE lA FuERzA tE aCoMpaÑe".swapcase())
    print("un pequeño paso para un programador, un gran salto para la humanidad".title())
    print("   Espacio al inicio y al final   ".strip())
    print("xxxooooxxx".strip("x"))
    print("xxxooooxxx".lstrip("x"))
    print("xxxooooxxx".rstrip("x"))
    print("¡Bienvenido".isalnum())
    print("Si se puede imaginar, se puede programar".startswith("Si"))
    print("Si se puede imaginar, se puede programar".startswith("Hola"))
    print("Si se puede imaginar, se puede programar".endswith("programar"))
    print("55".isdecimal())

    nombre = "Alice"
    print(nombre.isalpha()) #True, porque solo contiene letras
    nombre2 = "Alice123"
    print(nombre2.isalpha()) #False, porque contiene números

    texto = "hola mundo"
    print("*".join(texto)) #h*o*l*a* *m*u*n*d*o
    print("Python".center(20, "-")) #-------Python--------

    palabras = ["Python", "es", "genial"]
    print(" ".join(palabras)) #Python es genial

#analisis_cadenas()

def ejercicio_correos():
    correos = [ "gabriel@example.com", "alice@example.com", "bob@example.com", "aeoigroij.com", "juan@yahoo.com.mx", "maria@gmail.ekj"]

    for correo in correos:
        if correo.find("@") != -1 and correo.find(".com") != -1:
            print(f"{correo} es un correo válido.")
        else:
            print(f"* ERROR: {correo} NO es un correo válido.")

#ejercicio_correos()

def busqueda():
    mensaje = "Hola Mundo"
    print(mensaje.find("o",3)) #Busca la letra "o" a partir del índice 3, devuelve el índice de la siguiente "o" después del índice 3, que es 7.
    print(mensaje.find("o", 3, 9)) #Busca la letra "o" en el mensaje entre los índices 3 y 9, devuelve el índice de la siguiente "o" dentro de ese rango, que es 7.
    pos = mensaje.find("o")
    while pos != -1:
        print(f"Letra \"o\" en índice: {pos}")
        pos = mensaje.find("o", pos + 1) #Busca la siguiente "o" a partir del índice después de la última encontrada.

#busqueda()

def formato_cadenas():
    nombre = "Alice"
    edad = 30
    print(f"Mi nombre es {nombre} y tengo {edad} años.")

    texto = "Hola"

    print(f"{texto:*^10} ") #***Hola***

#formato_cadenas()

def formato_numeros():
    numero = 25
    print(f"El número es: {numero:+5}") #El número es: 00025
    print(f"El número es: {numero:+5d}") #El número es: +0025
    print(f"El número es: {numero:+5.2f}") #El número es: +25.00
    print(f"El número es: {numero:#b}") #El número es: 0b11001
    print(f"El número es: {numero:#x}") #El número es: 0x19

    millones = 1234567890
    print(f"El número es: {millones:,}") #El número es: 1,234,567,890

    numero_formatado = 123456.7890
    print(f"El número es: {numero_formatado:,.2f}") #El número es: 123,456.79

#formato_numeros()

import re

def expresiones_regulares():
    texto = "Aprendiendo Python"
    resultado = re.search("Python", texto) #Busca la palabra "Python" en el texto, devuelve un objeto de coincidencia si se encuentra, o None si no se encuentra.
    print(resultado.group()) #group() devuelve la parte del texto que coincide con la búsqueda, en este caso "Python".

    #Metacaracteres
    texto2a = "Mi número de teléfono es 1234567890."
    texto2b = "Mi número de teléfono es 123-456-7890."
    resultado2a = re.search(r"\d+", texto2a) #Busca una secuencia de dígitos en el texto, devuelve un objeto de coincidencia si se encuentra, o None si no se encuentra.
    resultado2b = re.search(r"\d{3}-\d{3}-\d{4}", texto2b) # (r"") indica que es una cadena raw, donde los caracteres de escape se tratan literalmente. \d representa un dígito, {3} indica que debe haber exactamente 3 dígitos, y el guion "-" se incluye literalmente.
    print(resultado2a.group()) #1234567890
    print(resultado2b.group()) #123-456-7890

    usuarios = ["@admin_2025", "@user123", "@python_master", "@JuanitoPerez", "@maria_garcia"]
    for usuario in usuarios:
        resultado3 = re.search(r"\w+", usuario) #Busca una secuencia de caracteres alfanuméricos (letras, dígitos o guiones bajos) en el texto, devuelve un objeto de coincidencia si se encuentra, o None si no se encuentra.
        if resultado3:
            print(resultado3.group()) #admin_2025, user123, python_master, JuanitoPerez, maria_garcia

    texto4 = "Hola mundo"
    resultado4 = re.search(r"\s", texto4) #Busca un espacio en el texto, devuelve un objeto de coincidencia si se encuentra, o None si no se encuentra.
    print(f"Hay un espacio >{resultado4.group()}< aquí") #Devuelve un espacio, porque \s representa un espacio en blanco.

#expresiones_regulares()

def ejercicio_validacion_nombres():
    nombres = [
        "Ana García", "Carlos Pérez", "María López", "JuanMartínez", "Laura Sánchez"]

    for nombre in nombres:
        if re.search(r"\s", nombre):
            print(f"Correcto: {nombre}")
        else:
            print(f"**Error: {nombre}")

#ejercicio_validacion_nombres()

def valores_opcionales():
    texto = "My favorite color"
    resultado = re.search(r"colou?r", texto)
    print(texto, "uses", resultado.group()) #color, porque la "u" es opcional debido a "u?".
#valores_opcionales()

telefono ="+521234567890"
resultado_telefono = re.search(r"\+?52\d{10}", telefono)
print(telefono)

telefono2 = input("Ingrese su número de teléfono: ")
patron = r"\+?52\d{10}$"
resultado_telefono2 = re.fullmatch(patron, telefono2)
if resultado_telefono2:
    print(f"El número {telefono2} es válido.")
else:
    print(f"El número {telefono2} no es válido. ¿Te falto tu lada, +52, tal vez números?")