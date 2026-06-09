''' Ejercicio: Protección de correos electrónicos
Una empresa compartirá un reporte con terceros.
Por motivos de privacidad, necesita ocultar el nombre de usuario de cada correo electrónico, pero conservar el dominio para fines estadísticos.
'''
texto = [
    "juan@gmail.com",
    "ana@hotmail.com",
    "pedro@yahoo.com",
    "marcos@outlook.com",
    "daniel@live.com"
    ]

'''
Reemplaza únicamente el nombre de usuario por: [USUARIO OCULTO]

Salida esperada:
[USUARIO OCULTO]@gmail.com
[USUARIO OCULTO]@hotmail.com
[USUARIO OCULTO]@yahoo.com
[USUARIO OCULTO]@outlook.com
[USUARIO OCULTO]@live.com
'''

import re
for correo in texto:
    correo_oculto = re.sub(r"^[^@]+", "[USUARIO OCULTO]", correo) #Reemplaza el nombre de usuario (cualquier cosa antes del @) por [USUARIO OCULTO], dejando el dominio intacto.
    print(correo_oculto)