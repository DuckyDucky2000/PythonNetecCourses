#Captura de datos de paciente
print("---- Registro básico de Pacientes ----")
nombre = input("Nombre: ")
edad = int(input("Edad: "))
altura = float(input("Altura (mts): "))
peso = float(input("Peso (kgs): "))
temperatura = float(input("Temperatura (°C): "))
imc = peso/(altura**2)

print("Nombre:", nombre)
print("Edad:", edad, "años")
print("Altura:", altura, "mts")
rounded_imc = round(imc,2)
#print("IMC:",rounded_imc)

if rounded_imc < 18.5:
    print("IMC:", rounded_imc, "- peso bajo")
elif rounded_imc > 18.5 and rounded_imc < 24.9:
    print("IMC:", rounded_imc, "- normal")
elif rounded_imc > 25.0 and rounded_imc < 29.9:
    print("IMC:", rounded_imc, "- sobrepeso")
elif rounded_imc > 30.0 and rounded_imc < 34.9:
    print("IMC:", rounded_imc, "- obesidad I")
elif rounded_imc > 35.0 and rounded_imc < 39.9:
    print("IMC:", rounded_imc, "- obesidad II")
else:
    print("IMC:", rounded_imc, "- obesidad III")

if temperatura < 36.0:
    print("Temperatura:", temperatura, "°C, muy baja")
elif temperatura >= 36.0 and temperatura <= 38.5:
    print("Temperatura:", temperatura, "°C, normal")
else:
    print("Temperatura:", temperatura, "°C, muy alta")