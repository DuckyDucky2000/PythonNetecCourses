'''Ejercicio: Banner de bienvenida
Tienes la siguiente información:'''

mensaje = "BIENVENIDO"
'''
Genera exactamente la siguiente salida:
"----BIENVENIDO-----"

Condiciones:
El texto debe quedar centrado. El ancho total debe ser de 20 caracteres. Los espacios sobrantes deben rellenarse con asteriscos (-). Utiliza una sola f-string.
'''

print(f"{mensaje:-^20}")