# -------------------- Operaciones con cadenas -------------------- #
'''
Los str son inmutables/ineditables
'''
cadena = "Edgar Velasco"
ciudad = "CDMX"
condicion = ciudad.lower()=="cdmx"
#cadena = cadena.upper()
print("Mayúsculas:", cadena.upper())
print("Original:", cadena)
print("Minúsculas:",cadena.lower())
print("Capitalizar:", cadena.capitalize())
print("Titulo:", cadena.title())
print("¿Eres de CDMX?", condicion)

#nombre = input("Nombre: ")
#nombre = nombre.title()
#nombre = 123
#print("Nombre: ", nombre)

print("Cadena comienza con A?", cadena.startswith("A"))
print("Cadena termina con o?", cadena.endswith("o"))
numero = 129734891763
cadena_test = str(numero)
print("Cadena termina con 3?", cadena_test.endswith("3"))
print("Reemplaza s por z:", cadena.replace("s", "z"))
print("Longitud:", len(cadena))