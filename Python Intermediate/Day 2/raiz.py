import Modulos.mensajes as mensajes
#from Modulos.operaciones import * #sumar, restar
import Modulos.operaciones as op
nombre = input("Ingrese su nombre: ")
mensajes.display(nombre)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

print("El resultado de la suma de", a, "+", b, "es:", op.sumar(a, b))

#resultado_resta = op.restar(a, b)
print("El resultado de la resta de", a, "-", b, "es:", op.restar(a, b))

print("El resultado de la multiplicación de", a, "*", b, "es:", op.multiplicar(a, b))

print("El resultado de la división de", a, "/", b, "es:", op.dividir(a, b))

print(dir(op))

