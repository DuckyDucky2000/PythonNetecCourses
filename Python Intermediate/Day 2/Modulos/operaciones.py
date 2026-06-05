def sumar (a, b):
    return a + b

def restar (a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."
    
def potencia (a, b):
    return a ** b

def division_entera (a, b):
    if b != 0:
        return a // b
    else:
        return "Error: No se puede dividir por cero."

def petencia (a, b):
    if b != 0:
        return a % b
    else:
        return "Error: No se puede dividir por cero."
    

def main():
    print(sumar(5, 3))
    print(sumar(2, 1))
    print(sumar(3, 3))
    print(sumar(2, 3))


print(__name__)

if __name__ == "__main__":
    main()