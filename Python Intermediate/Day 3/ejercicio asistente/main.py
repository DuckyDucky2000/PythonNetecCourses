'''
2️⃣ Crear un archivo llamado:
main.py
En este archivo deberán:

#✅ Importar el módulo: 
import asistente
#✅ Mostrar el contenido del módulo usando dir()
print(dir(asistente))
#✅ Mostrar la documentación de una función usando help()
help(asistente.saludar)
#✅ Mostrar el docstring usando __doc__
print(asistente.saludar.__doc__)
#✅ Ejecutar las funciones
print(asistente.saludar("Carlos"))

🔥 BONUS: Agregar documentación al módulo completo.
Ejemplo:

Módulo de asistente virtual.
Contiene funciones para generar mensajes automáticos.

📌 Resultado esperado
El programa debe:
✅ importar correctamente el módulo
✅ mostrar los nombres del módulo con dir()
✅ mostrar documentación con help()
✅ ejecutar las funciones correctamente
'''

#✅ Importar el módulo: 
import asistente
#✅ Mostrar el contenido del módulo usando dir()
print(dir(asistente))
#✅ Mostrar la documentación de una función usando help()
help(asistente.saludar)
#✅ Mostrar el docstring usando __doc__
print(asistente.saludar.__doc__)
#✅ Ejecutar las funciones
#print(asistente.saludar("Carlos"))

def main():
    nombre = input("Buenos días, ¿cómo te llamas? ")
    print(asistente.preguntar_edad())
    print(asistente.saludar(nombre))
    estado = input("¿Cómo te sientes hoy? Bien/Mal: ")
    #asistente.estado(estado)
    print(asistente.estado(estado))

main()