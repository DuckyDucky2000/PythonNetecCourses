''' Parte 3 - Protegiendo a nuestros Pokémon
Historia: El Profesor Oak descubrió un problema. Algunos entrenadores están modificando directamente la vida de los Pokémon.
Por ejemplo:
    pikachu.vida = -500
    o
    pikachu.vida = 999999
Esto provoca errores en el sistema.
Para evitarlo, se decidió proteger la información más importante de los Pokémon.

Objetivo:
    Aplicar:
    ✅ Encapsulamiento
    ✅ Getters
    ✅ Setters

Requisitos:
1. Proteger atributos
    Modificar la clase Pokemon.
    Los siguientes atributos deberán estar encapsulados:
        - vida
        - nivel
2. Crear métodos de acceso (Getters)
    - vida
    - nivel
3. Crear métodos modificadores (Setters)
    - nivel
    - vida
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
        self.__nombre = nombre
        self.__tipo = tipo
        self.__nivel = nivel
        self.__vida = vida  #hacer privado, evita que usuarios externos puedan acceder directamente a este atributo, solo se puede acceder a través de métodos específicos dentro de la clase.
    # --------- PARTE 2: MÉTODOS ---------
    def presentarse(self):
        print(f"Hola, soy {self.nombre}. Soy de tipo {self.tipo}.")
    
    def atacar(self):
        print(f"{self.nombre} ha realizado un ataque.")
    
    def descansar(self):
        print(f"{self.nombre} está descansando.")
    
    def es_pokemon(self):
        return isinstance(self, Pokemon)
    # --------- PARTE 3: PROTEGER ATRIBUTOS, SETTERS, GETTERS ---------
    def get_vida(self):
        return self.vida
    def get_nivel(self):
        return self.nivel
    def set_vida(self, nueva_vida):
        if nueva_vida < 0 or nueva_vida > 714:
            print("Puntos de Salud Inválidos. No seas tramposo.")
        else:
            self.__vida = nueva_vida
    def set_nivel(self, nuevo_nivel):
        if nuevo_nivel < 1 or nuevo_nivel > 100:
            print("El nivel no puede ser menor a 1 o mayor a 100. No seas tramposo.")
        else:
            self.__nivel = nuevo_nivel
    def curarse(self, puntos):
        self.set_vida(self.get_vida() + puntos)
    def subir_nivel(self):
        self.set_nivel(self.get_nivel() + 1)

pikachu = Pokemon("Pikachu", "Electric", 25, 100)
charmander = Pokemon("Charmander", "Fire", 15, 80)
bulbasaur = Pokemon("Bulbasaur", "Grass", 20, 90)
squirtle = Pokemon("Squirtle", "Water", 18, 85)