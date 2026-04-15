#Calculadora de dosis de medicamento
respuesta="si"
while respuesta != "no":
    nombre_paciente = input("Nombre: ")
    peso  = float(input("Peso: ")) #kgs
    dosis =  float(input("Dosis (mg/kg): ")) #mg/kg
    concentracion = float(input("Concentración (mg/ml): "))  #mg/ml

    dosis_total = peso * dosis
    volumen = dosis_total / concentracion
    print("Volumen:", volumen)
    if dosis_total < 50:
        print("Dosis total:", dosis_total, " -- Dosis Baja")
    elif dosis_total >= 50 and dosis_total <= 500:
        print("Dosis total:", dosis_total, " -- Dosis Normal")
    elif dosis_total > 500:
        print("Dosis total:", dosis_total, " -- Dosis Alta")
    else:
        print("ERROR! Datos inválidos")
    
    respuesta = input("¿Faltan pacientes? ")