''' **Práctica Integradora POO- Parte 4 - Evolución del Laboratorio Pokémon **
Historia:
El Profesor Oak ha descubierto un problema. Hasta ahora todos los Pokémon utilizan exactamente la misma clase: Pokemon Sin embargo, los Pokémon son muy diferentes entre sí.

Por ejemplo:
    Charmander → Tipo Fuego
    Squirtle → Tipo Agua
    Bulbasaur → Tipo Planta
    Pikachu → Tipo Eléctrico

Todos comparten características básicas, pero cada tipo posee habilidades especiales.
El Profesor Oak necesita reorganizar el sistema utilizando Herencia.

Objetivo:
    Aplicar:
        ✅ Herencia
        ✅ Clase Padre
        ✅ Clases Hijas
        ✅ Reutilización de código

Requisitos:
    Utilizar la clase Pokemon como Clase Padre
    La clase padre deberá conservar:
        - nombre
        - tipo
        - nivel
        - vida
    También deberá conservar:
        presentarse()
        atacar()
        descansar()
        curarse()
        subir_nivel()

    Crear Clases Hijas
    Crear las siguientes clases:
        - PokemonFuego
        - PokemonAgua
        - PokemonPlanta
        - PokemonElectrico

    Todas deberán heredar de:
        - Pokemon

    Crear habilidades especiales
    Cada tipo deberá tener un método exclusivo.
        - PokemonFuego :        Agregar:    lanzar_llamas()
        - PokemonAgua :         Agregar:    hidrobomba()
        - PokemonPlanta :       Agregar:    latigo_cepa()
        - PokemonElectrico :    Agregar:    impactrueno()

    Crear Objetos:
        - Charmander
        - Squirtle
        - Bulbasaur
        - Pikachu
    utilizando las nuevas clases hijas.

    Probar Herencia:
        Comprobar que TODOS pueden utilizar:
            - presentarse()
            - atacar()
            - descansar()
            - curarse()
            - subir_nivel()

            Probar habilidades especiales
            Comprobar que:          Charmander puede usar: lanzar_llamas()
            Comprobar que:          Squirtle puede usar: hidrobomba()
            Comprobar que:          Bulbasaur puede usar: latigo_cepa()
            Comprobar que:          Pikachu puede usar: impactrueno()
Investigación:
    Intenta ejecutar:
        pikachu.lanzar_llamas()
    Pregunta: ¿Qué ocurrió?
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