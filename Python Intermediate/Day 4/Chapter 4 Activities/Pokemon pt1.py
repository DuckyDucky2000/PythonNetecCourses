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

nombre
tipo
nivel
vida
Crear objetos
Registra los siguientes Pokémon:

Pikachu
Charmander
Bulbasaur
Squirtle
Mostrar información
Utiliza print() para mostrar los datos de cada Pokémon.

Verificar atributos
Utiliza la función: hasattr()

para comprobar si existen algunos atributos.

Reto 1
Crear un Pokémon inventado.
Debe tener:

nombre
tipo
nivel
vida
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

pikachu = Pokemon("Pikachu", "Eléctrico", 25, 100)
charmander = Pokemon("Charmander", "Fuego", 15, 80)
bulbasaur = Pokemon("Bulbasaur", "Planta", 20, 90)
squirtle = Pokemon("Squirtle", "Agua", 18, 85)

print(f"Nombre: {pikachu.nombre}, \tTipo: {pikachu.tipo}, \tNivel: {pikachu.nivel}, \tVida: {pikachu.vida}")
print(f"Nombre: {charmander.nombre}, \tTipo: {charmander.tipo}, \tNivel: {charmander.nivel}, \tVida: {charmander.vida}")
print(f"Nombre: {bulbasaur.nombre}, \tTipo: {bulbasaur.tipo}, \tNivel: {bulbasaur.nivel}, \tVida: {bulbasaur.vida}") 
print(f"Nombre: {squirtle.nombre}, \tTipo: {squirtle.tipo}, \tNivel: {squirtle.nivel}, \tVida: {squirtle.vida}")