import Modulos.mensajes as mensajes
#from Modulos.operaciones import * #sumar, restar
import Modulos.operaciones as op
nombre = input("Ingrese su nombre: ")
mensajes.display(nombre)

a = int(input("1er número: "))
b = int(input("2do número: "))

print("El resultado de la suma de", a, "+", b, "es:", op.sumar(a, b))
#resultado_resta = op.restar(a, b)
print("El resultado de la resta de", a, "-", b, "es:", op.restar(a, b))
print("El resultado de la multiplicación de", a, "*", b, "es:", op.multiplicar(a, b))
print("El resultado de la división de", a, "/", b, "es:", op.dividir(a, b))
print("El resultado de la potencia de", a, "**", b, "es:", op.potencia(a, b))
print("El resultado de la división entera de", a, "//", b, "es:", op.division_entera(a, b))
print("El resultado de la potencia de", a, "%", b, "es:", op.petencia(a, b))

print(dir(op))

print(op.__doc__)

print(__name__)