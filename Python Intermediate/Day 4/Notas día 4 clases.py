class Perro: #Nota: nombre de la clase en mayuscula
    def __init__(self, nombre, sexo, raza, edad): #Metodo constructor
        #print("Ha nacido un nuevo perro", self)
        self.nombre = nombre #Atributo de instancia, cada instancia tiene su propio valor
        self.sexo = sexo
        self.raza = raza
        self.edad = edad 
    def ladrar(self):
        print("¡Guau guau!")
    def comer(self):
        print("¡Ñam ñam!")
    def dormir(self):
        print("Zzzzz...")

firulais = Perro("Firulais", "Macho", "Labradror", 2) #instancia de la clase perro
rocky = Perro("Rocky", "Macho", "Pastor alemán", 3) #instancia de la clase perro
luna = Perro("Luna", "Hembra", "Husky", 2) #instancia de la clase perro
bella = Perro("Bella", "Hembra", "Cocker Spaniel", 4) #instancia de la clase perro
jolie = Perro("Jolie", "Hembra", "Cocker Spaniel", 0) #instancia de la clase perro

for perro in [firulais, rocky, luna, bella, jolie]:
    if perro.sexo == "Macho":
        print(f"El nombre de mi perro es {perro.nombre}, su raza es {perro.raza} y tiene {perro.edad} años.")
    else:
        print(f"El nombre de mi perra es {perro.nombre}, su raza es {perro.raza} y tiene {perro.edad} años.")


'''Instancia: es un objeto creado a partir de una clase. Es una representación concreta de la clase, con sus propios atributos y comportamientos. Cada instancia puede tener valores diferentes para sus atributos, lo que permite crear múltiples objetos con características únicas a partir de la misma clase.'''

class Auto:
    pass

ferrari = Auto()
tesla = Auto()
mustang = Auto()

class Videojuego:
    def __init__(self, nombre, genero, plataforma):
        self.nombre = nombre
        self.genero = genero
        self.plataforma = plataforma

mario_bros = Videojuego("Mario Bros", "Plataforma", "Nintendo")
zelda = Videojuego("Zelda", "Aventura", "Nintendo")
pokemon = Videojuego("Pokemon", "RPG", "Nintendo")

class Superheroe:
    def __init__(self, nombre, poder_caracteristico, vida, ciudad):
        self.nombre = nombre
        self.poder_caracteristico = poder_caracteristico
        self.vida = vida
        self.ciudad = ciudad

spiderman = Superheroe("Peter Parker", "Sentido arácnido", 70, "Nueva York")
nightwing = Superheroe("Dick Grayson", "Estar bien guapo", 30, "Blüdhaven")
loki = Superheroe("Loki", "Magia Asgardiana", 100, "Asgard")

class Pelicula:
    def __init__(self, duracion, director, genero):
        self.duracion = duracion
        self.director = director
        self.genero = genero

the_amazing_digital_circus_the_last_act = Pelicula(90, "Travis Knight", "Animación") 
shrek = Pelicula(90, "Andrew Adamson y Vicky Jenson", "Animación")
avatar = Pelicula(162, "James Cameron", "Ciencia Ficción")
avengers = Pelicula(143, "Anthony y Joe Russo", "Acción")
son_of_batman = Pelicula(80, "Sandy Collora", "Animación") 
crepusculo = Pelicula(120, "Catherine Hardwicke", "Romance")

if hasattr(crepusculo, 'duracion'):
    print(f"La película tiene un atributo 'duracion'.")
else:
    print(f"No tiene ese atributo")