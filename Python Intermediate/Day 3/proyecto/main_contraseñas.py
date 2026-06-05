from seguridad import generar_password #import *

def main():
    '''
    Debe:
    * importar el módulo seguridad
    * llamar la función generar_password()
    * mostrar la contraseña en pantalla
    '''
    password = generar_password()
    print("Tu contraseña es:", password)
    #print("¿Quieres generar otra contraseña? (s/n)")
    if input("¿Quieres generar otra contraseña? (s/n) ").lower() == "s":
        main()
    else:
        print("De acuerdo, ¡hasta luego!")

print(" ------ Generador de contraseñas ------")
main()