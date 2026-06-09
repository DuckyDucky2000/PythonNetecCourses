''' Práctica Integradora POO
**Parte 1 - El Laboratorio Pokémon (Opción 1) **
Contexto

El Profesor Oak necesita un sistema para registrar los Pokémon descubiertos en la región.
Tu misión será crear la primera versión de este sistema utilizando Programación Orientada a Objetos.

Requisitos:

Crear una clase
Debes crear una clase llamada: ** Pokemon**
Crear un constructor
Todos los Pokémon deben nacer con la siguiente información:

nombre  tipo    nivel   vida

Crear objetos
Registra los siguientes Pokémon:

Pikachu, Charmander, Bulbasaur, Squirtle
Mostrar información
Utiliza print() para mostrar los datos de cada Pokémon.

Verificar atributos
Utiliza la función: hasattr()

para comprobar si existen algunos atributos.

Reto 1
Crear un Pokémon inventado.
Debe tener:
nombre  tipo    nivel   vida
Reto 2
¿Qué ocurre si intentas consultar un atributo que no existe?
Investígalo.
'''

class Pokemon:
    def __init__(self, nombre, tipo, nivel, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = vida

pikachu = Pokemon("Pikachu", "Electric", 25, 100)
charmander = Pokemon("Charmander", "Fire", 15, 80)
bulbasaur = Pokemon("Bulbasaur", "Grass", 20, 90)
squirtle = Pokemon("Squirtle", "Water", 18, 85)
inventado = Pokemon("Culryflame", "Fire", 30, 120)

def mostrar_pokemon():
    for pokemon in [pikachu, charmander, bulbasaur, squirtle, inventado]:
        print(f"{pokemon.nombre}\t\t{pokemon.tipo}\t{pokemon.nivel}\t\t{pokemon.vida}")

mostrar_pokemon()

print(f"\n¿Pikachu tiene el atributo 'nivel'? {hasattr(pikachu, 'nivel')}")
print(f"¿Pikachu tiene el atributo 'ataque'? {hasattr(pikachu, 'ataque')}") #No tiene