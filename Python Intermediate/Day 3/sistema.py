#Registro de empleados

def despedida():
    print("Gracias por usar el sistema de registro de empleados. ¡Hasta luego!")

def validar_edad(edad):
    if edad >= 18:
        print("Edad válida. Puede continuar con el registro.")
    else:
        print("Edad no válida. Debe ser mayor de 18 años para registrarse.")
        despedida()

def solicitar_datos():
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    validar_edad(edad)
    #print(f"Empleado registrado: {nombre}, Edad: {edad}")
    return nombre, edad

def bienvenida():
    print("Bienvenido al sistema de registro de empleados.")
    print("-----Sistema de Registro de Empleados-----")

def main():
    bienvenida()
    nombre, edad = solicitar_datos()
    print(f"-------Empleado Registrado------\nEmpleado: {nombre}\nEdad: {edad}")
    despedida()
if __name__ == "__main__":
    main()