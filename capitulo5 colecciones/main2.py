#Tuplas: como una lista pero que no se puede modificar, usar para datos fijos
'''
tuple = ()
'''
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

for i in dias_semana:
    if(i.startswith("M")):
        print(i)


for i in dias_semana:
    if(not i.endswith("es")):
        print(i)