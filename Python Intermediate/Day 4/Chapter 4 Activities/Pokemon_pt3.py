''' Parte 3 - Protegiendo a nuestros Pokémon
Historia: El Profesor Oak descubrió un problema. Algunos entrenadores están modificando directamente la vida de los Pokémon.

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

Requisitos:

1. Proteger atributos
    Modificar la clase Pokemon.
    Los siguientes atributos deberán estar encapsulados:    vida    nivel
2. Crear métodos de acceso
    Crear un Getter para:
        - vida
        - nivel
3. Crear métodos modificadores
    Crear un Setter para:
        - nivel
        - vida
    Crear un Setter para:
        - nivel
        - Vida
    No debe permitirse:
        vida < 0
    No debe permitirse:
        nivel < 1
Pruebas:
    Utilizar los Getters para consultar:
        vida nivel
            de:
                Pikachu, Charmander, Bulbasaur, Squirtle
    Utilizar los Setters para intentar modificar:
        vida nivel

Reto 1
    Crear un método:
        curarse() ---- que aumente la vida del Pokémon.

Reto 2
    Crear un método:
        subir_nivel() --- que incremente el nivel del Pokémon.
'''


class Pokemon:
    # --------- PARTE 1: CLASES Y MÉTODOS ---------
    def __init__(self, nombre, tipo, nivel, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = vida
    # --------- PARTE 2: MÉTODOS ---------
    def presentarse(self):
        print(f"Hola, soy {self.nombre}. Soy de tipo {self.tipo}.")
    
    def atacar(self):
        print(f"{self.nombre} ha realizado un ataque.")
    
    def descansar(self):
        print(f"{self.nombre} está descansando.")
    
    def es_pokemon(self):
        return isinstance(self, Pokemon)
    # --------- PARTE 3: PROTEGIENDO A NUESTROS POKÉMON ---------
    def get_vida(self):
        return self.vida
    def get_nivel(self):
        return self.nivel

pikachu = Pokemon("Pikachu", "Electric", 25, 100)
charmander = Pokemon("Charmander", "Fire", 15, 80)
bulbasaur = Pokemon("Bulbasaur", "Grass", 20, 90)
squirtle = Pokemon("Squirtle", "Water", 18, 85)
inventado = Pokemon("Culryflame", "Fire", 30, 120)


pikachu.presentarse()
charmander.atacar()
bulbasaur.descansar()
print(f"¿Pikachu es un Pokémon? {pikachu.es_pokemon()}")