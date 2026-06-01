#Operadores relacionales

''' ==: igual que (int, float, str, bool)
Descripción: compara 2 valores '''
#Scenario: nombre de pacientes es igual al de otro?
nombre1 = "Paty"
nombre2 = "paty"
resultado_igual = nombre1==nombre2
print("Same name (1&2)?", resultado_igual)


''' != Diferente que
Descripción: valida si 2 variables son diferentes '''
#Scenario: peso de pacientes es diferente al de otro?
peso1 = 35.8
peso2 = 40.2
resultado_dif = peso1!=peso2
print("Different weight?", resultado_dif)

''' < o > Mayour que / Menor que
Descripción que un valor sea sólo mayor a otro '''

edad = 18
resultado_mayor = edad > 17
print("Mayor de edad?", resultado_mayor)

'''
<= o >= Mayor que / igual que
Descripción combina el = y el <(o>), compara valor mayor/menor o igual a x '''
#Scenario: un paciente es 3ra edad

edad_miq = 61
resultado_miq = edad_miq>= 60
print("¿Es 3a edad?", resultado_miq)

#Probar minq
#Vida máxima, record mundial presuntamente 122
edad_minq = 104
resultado_minq = edad_minq<=122
print("Vivo?",edad_minq, resultado_minq)

# ------------------ Operadores Lógicos ---------------------------#

''' and: requiere varias condiciones para considerarse cierto '''
#Paciente es adulto

paciente_and = 19
ciudad="Toluca"
condicion_and = (paciente_and>=18 and paciente_and<=60) and (ciudad == "Toluca")
print("Paciente adulto joven en Toluca?", condicion_and)

''' or: al menos una condición se cumple '''
ciudad_or = "Guadalajara"
condicion_or = ciudad_or=="Zapopan" or ciudad_or=="Guadalajara"
print("Esta en GDL O ZPN?", condicion_or)


'''not: niega, o invierte valores, si es falso, da verdadero y viceversa'''
#Scenario: ¿No eres adulto mayor?
edad_not = 45
condicion_not = not edad_not>=60
print("NO eres un adulto mayor (3ra edad)?",condicion_not)