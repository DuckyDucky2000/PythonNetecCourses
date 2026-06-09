'''
Ejercicio: Auditoría de ventas 💰
Una tienda recibió el siguiente reporte:'''

reporte = '''Venta #1254 por $850
Venta #1255 por $1200
Venta #1256 por $950
Venta #1257 por $1500'''

'''
El gerente quiere obtener todos los números de venta.
Utiliza findall() para extraer todos los IDs de venta.

Salida esperada:    ['#1254', '#1255', '#1256', '#1257']
'''

import re
def auditoria_ventas():
    ventas = re.findall(r"#\d+", reporte) #Busca todas las ocurrencias que coincidan con el patrón # seguido de uno o más dígitos, devuelve una lista de los IDs de venta encontrados.
    print(ventas)

auditoria_ventas()