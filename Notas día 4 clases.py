class Perro: #Nota: nombre de la clase en mayuscula
    def __init__(self, nombre, raza, edad): #Metodo constructor
        print("Ha nacido un nuevo perro", self) #self.__class__.__name__ devuelve el nombre de la clase a la que pertenece el objeto
        self.nombre = nombre #Atributo de instancia, cada instancia tiene su propio valor
        self.raza = raza
        self.edad = edad 

firulais = Perro("Firulais", "Labradror", 2) #instancia de la clase perro
rocky = Perro("Rocky", "Pastor alemán", 3) #instancia de la clase perro
luna = Perro("Luna", "Husky", 1) #instancia de la clase perro

'''Instancia: es un objeto creado a partir de una clase. Es una representación concreta de la clase, con sus propios atributos y comportamientos. Cada instancia puede tener valores diferentes para sus atributos, lo que permite crear múltiples objetos con características únicas a partir de la misma clase.'''

class Auto:
    pass

ferrari = Auto() #instancia de la clase auto
tesla = Auto() #instancia de la clase auto
mustang = Auto() #instancia de la clase auto

class Videojuego:
    pass

mario_bros = Videojuego() #instancia de la clase videojuego
zelda = Videojuego() #instancia de la clase videojuego
pokemon = Videojuego() #instancia de la clase videojuego

class Superheroe:
    pass

spiderman = Superheroe() #instancia de la clase superheroe
spiderman.nombre = "Peter Parker"
spiderman.poder_caracteristico = "Sentido arácnido"
spiderman.vida = 70
spiderman.ciudad = "Nueva York"

nightwing = Superheroe() #instancia de la clase superheroe
nightwing.nombre = "Dick Grayson"
nightwing.poder_caracteristico = "Estar bien guapo"
nightwing.vida = 30
nightwing.ciudad = "Blüdhaven"

loki = Superheroe() #instancia de la clase superheroe
loki.nombre = "Loki"
loki.poder_caracteristico = "Magia Asgardiana"
loki.vida = 100
loki.ciudad = "Asgard"

class Pelicula:
    duracion = 0
    director = ""
    genero = ""
    pass

the_amazing_digital_circus_the_last_act = Pelicula() 
the_amazing_digital_circus_the_last_act.duracion = 90
the_amazing_digital_circus_the_last_act.director = "Travis Knight"
the_amazing_digital_circus_the_last_act.genero = "Animación"

shrek = Pelicula()
shrek.duracion = 90
shrek.director = "Andrew Adamson y Vicky Jenson"
shrek.genero = "Animación"


avatar = Pelicula()
avatar.duracion = 162
avatar.director = "James Cameron"
avatar.genero = "Ciencia Ficción"

avengers = Pelicula() 
avengers.duracion = 143
avengers.director = "Anthony y Joe Russo"
avengers.genero = "Acción"

son_of_batman = Pelicula() 
son_of_batman.duracion = 80
son_of_batman.director = "Sandy Collora"
son_of_batman.genero = "Animación" 