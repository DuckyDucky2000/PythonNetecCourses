'''
Contexto
La NASA perdió comunicación con la nave Artemis X mientras realizaba una misión de exploración en una región desconocida del espacio.
Tras recuperar parte de la memoria de la computadora principal, los ingenieros descubrieron que la tripulación dejó un mensaje oculto dentro de varios registros dañados.
Tu misión será descifrar la última transmisión enviada por la nave utilizando indexación y slicing.

Instrucciones
'''

#Registros Recuperados

registro1 = ["A7UZT9O2"]
registro2 = ["xD7E4S9TMR8U3C1C5I6O0N"]
registro3 = ["A1D2A3V4I5T6C7A8"]

''' Fragmento 1
La primera palabra está oculta en el registro 1.
Recupera una letra cada 2 posiciones comenzando desde el índice 0.

Guarda el resultado en:             fragmento1
'''

fragmento1 = registro1[0][0:len(registro1[0]):2]
#print(fragmento1)

''' Fragmento 2
La segunda palabra está oculta en el registro 2.

Deberás utilizar indexación para recuperar cada letra de manera individual y posteriormente unirlas. La palabra se conforma por el indice : 1, 3,5,7,9,11,13,15,17,19,21

Guarda el resultado en:             fragmento2
'''

fragmento2 = registro2[0][1] + registro2[0][3] + registro2[0][5] + registro2[0][7] + registro2[0][9] + registro2[0][11] + registro2[0][13] + registro2[0][15] + registro2[0][17] + registro2[0][19] + registro2[0][21]
#print(fragmento2)

''' Fragmento 3

La última palabra se encuentra oculta en el registro 3.
Primero recupera únicamente las letras utilizando slicing con 2 saltos.
Posteriormente invierte el resultado utilizando slicing inverso.
Guarda el resultado en:             fragmento3
'''

fragmento3 = registro3[0][0:len(registro3[0]):2][::-1]
#print(fragmento3)


''' Mensaje Final
Una vez obtenidos todos los fragmentos, crea la variable:           mensaje_secreto
uniendo todas las partes recuperadas.

Finalmente muestra en pantalla:
'''

mensaje_secreto = fragmento1 + " " + fragmento2 + " " + fragmento3

print("\nTRANSMISIÓN RECUPERADA:")
print(mensaje_secreto, "💥")
print("\nEste mensaje fue patrocinado por Doofenshmirtz Malvados y Asociados.")

''' Restricciones
✅ Debes utilizar indexación.
✅ Debes utilizar slicing.
✅ Debes utilizar slicing con saltos.
❌ No está permitido escribir manualmente ninguna palabra.
❌ Todas las palabras deben recuperarse a partir de los registros proporcionados.
'''