'''
Parte 3 - Protegiendo a nuestros Pokémon
Historia

El Profesor Oak descubrió un problema.

Algunos entrenadores están modificando directamente la vida de los Pokémon.

Por ejemplo:

pikachu.vida = -500

o

pikachu.vida = 999999

Esto provoca errores en el sistema.

Para evitarlo, se decidió proteger la información más importante de los Pokémon.

Objetivo

Aplicar:

✅ Encapsulamiento

✅ Getters

✅ Setters

Requisitos

1. Proteger atributos

Modificar la clase Pokemon.

Los siguientes atributos deberán estar encapsulados:

vida
nivel
2. Crear métodos de acceso

Crear un Getter para:

vida
Crear un Getter para:

nivel
3. Crear métodos modificadores

Crear un Setter para:

vida
Crear un Setter para:

-nivel -Vida

No debe permitirse:

vida < 0
No debe permitirse:

nivel < 1
Pruebas

Utilizar los Getters para consultar:

vida nivel

de:

Pikachu
Charmander
Bulbasaur
Squirtle
Utilizar los Setters para intentar modificar:

vida nivel

Reto 1

Crear un método:

curarse()
que aumente la vida del Pokémon.

Reto 2

Crear un método:

subir_nivel()
que incremente el nivel del Pokémon.
'''