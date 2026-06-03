#print("Hola Mundo")

def calcular_area(base, altura):
    '''
    Calcular área de un réctangulo a partir de base y altura
    
    Parámetros:
    base (float o int): base del rectangulo
    altura (float o int): altura de rectangulo

    Retorna:
    Área calculada
    '''

    area = base * altura
    return area

#print(calcular_area(8,5))
#print(calcular_area.__doc__) #imprime el doc-string: comentario multilinea

x = 10
#print("x is a an" , type(x), "value")

#Asignación simultanea
tranquilo, lindo, divertido, inteligente, sentimental = "Haru", "Makoto", "Nagisa", "Rei", "Rin"
#Equivalente a un linea por linea tranquilo = "Haru", etc.

#Tipo de datos
#Boolean
'''
print(True + 1) # True = 1
print(False + 1) # False = 0
print(True * 3.5)
'''

#DELETE
#del x
#print(x)
'''
a = 10
b = a
print("a = ", a)
print("b = ", b)
del a #no puede eliminarlo del todo, porque b depende de a
print("a =", a) #aunque a ya no funciona sola
del b
print("b =", b)
'''

lista = ["Hola", 2j, 3, True, 5]
lista_copia = lista
del lista[2]
print(lista)
#print(lista_copia)
del lista[0]
print(lista)

def mi_funcion():
    print("Prueba de Identación automática")
    print("Identación manual, 4 espacios")
    print("Identación manual, tab -->")
    x = int(input("Prueba escribiendo 1 o 2 (numeros o se rompe): "))
    if x == 1:
        print("Identación if ruta 1")
    elif x == 2: 
        print("Identación if ruta 2")
    else:
        print("No seas tramposo, dije 1 o 2")

#
# mi_funcion()

#help('<<')