import random

caracteres_permitidos = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]

def generar_password():
    '''
    Debe contener:
    * una función llamada generar_password()
    * una lista o cadena de caracteres permitidos
    * lógica para generar una contraseña aleatoria de 8 caracteres (usa ciclos) 

    ⚙️ Requisitos
    ✅ Usar: import random
    ✅ Crear una función
    ✅ Usar módulos propios
    ✅ Utilizar: random.choice()
    '''
    global caracteres_permitidos
    password = ""
    for i in range(8):
        password += random.choice(caracteres_permitidos)
    return password