''' Ejercicio: Credenciales de empleados
La empresa TechNova está generando nuevas credenciales para sus empleados.
Tienes la siguiente información:'''

nombre1 = "Ana García"
id1 = 25

nombre2 = "Carlos López"
id2 = 348

nombre3 = "María Torres"
id3 = 7

titulo = "CREDENCIAL"
for nombre, id in [(nombre1, id1), (nombre2, id2), (nombre3, id3)]:
    print(f"{titulo:=^20}")
    print(f"Empleado: {nombre}")
    print(f"ID: EMP-{id:06d}\n")

''' Genera la siguiente salida:

===== CREDENCIAL =====
Empleado: Ana García
ID: EMP-000025

===== CREDENCIAL =====
Empleado: Carlos López
ID: EMP-000348

===== CREDENCIAL =====
Empleado: María Torres
ID: EMP-000007

Requisitos:

Todos los IDs deben tener exactamente 6 dígitos.
Si faltan dígitos, deben completarse con ceros a la izquierda.
El prefijo "EMP-" debe aparecer antes del número.
Utiliza f-strings para construir la salida.
'''



print("\n" + "="*30 + "\n")

''' Ejercicio: Nómina de empleados
El departamento de Recursos Humanos necesita imprimir los salarios de sus empleados de manera profesional.

Tienes la siguiente información:'''

empleado1 = "Ana García"
salario1 = 12500.5

empleado2 = "Carlos López"
salario2 = 98765.4321

empleado3 = "María Torres"
salario3 = 8500

titulo = "NÓMINA"
for nombre, salario in [(empleado1, salario1), (empleado2, salario2), (empleado3, salario3)]:
    print(f"{titulo:=^20}")
    print(f"Empleado: {nombre}")
    print(f"Salario: ${salario:,.2f}\n")

''' Genera la siguiente salida:

===== NÓMINA =====
Empleado: Ana García
Salario: $12,500.50

Empleado: Carlos López
Salario: $98,765.43

Empleado: María Torres
Salario: $8,500.00
Requisitos:

Mostrar separador de miles.
Mostrar exactamente dos decimales.
Utilizar f-strings.
'''