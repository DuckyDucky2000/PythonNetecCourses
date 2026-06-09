'''Ejercicio: Folio de transferencia bancaria
El banco genera un folio único para cada transferencia.
Tienes la siguiente información:'''
folio = 348
'''Genera exactamente la siguiente salida:      TRX-000348
Condiciones:
Debe comenzar con TRX-. El número debe ocupar 6 dígitos. Si faltan dígitos, deben completarse con ceros. Utiliza una sola f-string.
'''
def generar_folio(folio):
    folio_formateado = f"TRX-{folio:06d}"
    print(folio_formateado)

generar_folio(folio)