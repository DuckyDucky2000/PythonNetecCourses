'''
**Práctica Integradora POO- Parte 4 - Evolución del Laboratorio Pokémon **
Historia

El Profesor Oak ha descubierto un problema.

Hasta ahora todos los Pokémon utilizan exactamente la misma clase: Pokemon

Sin embargo, los Pokémon son muy diferentes entre sí.

Por ejemplo:

Charmander → Tipo Fuego

Squirtle → Tipo Agua

Bulbasaur → Tipo Planta

Pikachu → Tipo Eléctrico

Todos comparten características básicas, pero cada tipo posee habilidades especiales.

El Profesor Oak necesita reorganizar el sistema utilizando Herencia.

Objetivo

Aplicar:

✅ Herencia

✅ Clase Padre

✅ Clases Hijas

✅ Reutilización de código

Requisitos

Utilizar la clase Pokemon como Clase Padre
La clase padre deberá conservar:

nombre
tipo
nivel
vida
También deberá conservar:

presentarse()

atacar()

descansar()

curarse()

subir_nivel()

Crear Clases Hijas
Crear las siguientes clases:

PokemonFuego
PokemonAgua
PokemonPlanta
PokemonElectrico
Todas deberán heredar de:

Pokemon

Crear habilidades especiales
Cada tipo deberá tener un método exclusivo.

PokemonFuego

Agregar:

lanzar_llamas()

PokemonAgua

Agregar:

hidrobomba()

PokemonPlanta

Agregar:

latigo_cepa()

PokemonElectrico

Agregar:

impactrueno()

Crear Objetos
Crear:

Charmander
Squirtle
Bulbasaur
Pikachu
utilizando las nuevas clases hijas.

Probar Herencia
Comprobar que TODOS pueden utilizar:

presentarse()

atacar()

descansar()

curarse()

subir_nivel()

Probar habilidades especiales
Comprobar que:

Charmander puede usar: lanzar_llamas()
Comprobar que:

Squirtle puede usar: hidrobomba()
Comprobar que:

Bulbasaur puede usar: latigo_cepa()
Comprobar que:

Pikachu puede usar: impactrueno()
Investigación

Intenta ejecutar:

pikachu.lanzar_llamas()

Pregunta:

¿Qué ocurrió?
'''