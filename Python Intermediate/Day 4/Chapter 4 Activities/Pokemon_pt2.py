''' El Laboratorio Pokémon- Parte 2: Los Pokémon ahora pueden actuar

Historia:
El Profesor Oak ya registró a todos los Pokémon. Ahora necesita que los Pokémon puedan realizar acciones.

Objetivo:
Agregar métodos a la clase Pokemon.

Requisitos:
    Agregar los siguientes métodos:
        presentarse() ----- Debe mostrar información del Pokémon.
            Ejemplo:  Hola, soy Pikachu. Soy de tipo Eléctrico.
        atacar() ----- Debe mostrar un mensaje de ataque.
            Ejemplo:    Pikachu ha realizado un ataque.
        descansar() ----- Debe mostrar un mensaje de descanso.
            Ejemplo:    Pikachu está descansando.
            Debe mostrar:   Pikachu está descansando.

Reto: Inventa otro método
Reto Extra: Utiliza isinstance() para verificar si los objetos creados pertenecen a la clase Pokemon

Pruebas:
Ejecutar los métodos con:  pikachu charmander bulbasaur squirtle
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

pikachu = Pokemon("Pikachu", "Electric", 25, 100)
charmander = Pokemon("Charmander", "Fire", 15, 80)
bulbasaur = Pokemon("Bulbasaur", "Grass", 20, 90)
squirtle = Pokemon("Squirtle", "Water", 18, 85)
inventado = Pokemon("Culryflame", "Fire", 30, 120)


pikachu.presentarse()
charmander.atacar()
bulbasaur.descansar()
print(f"¿Pikachu es un Pokémon? {pikachu.es_pokemon()}")