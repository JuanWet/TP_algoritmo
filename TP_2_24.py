class PersonajeMCU:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas
        
class PilaMCU:
    def __init__(self):
        self.pila = []

    def esta_vacia(self):
        return len(self.pila) == 0

    def apilar(self, personaje):
        self.pila.append(personaje)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.pila.pop()

    def obtener_posicion(self, personaje):
        if personaje in self.pila:
            posicion = len(self.pila) - self.pila.index(personaje)
            return posicion, personaje.nombre
        else:
            return None, None

    def personajes_mas_de_cinco_peliculas(self):
        personajes = []
        for personaje in self.pila:
            if personaje.cantidad_peliculas > 5:
                personajes.append(personaje)
        return personajes

    def cantidad_peliculas_viuda_negra(self):
        for personaje in self.pila:
            if personaje.nombre == "Viuda Negra":
                return personaje.cantidad_peliculas
        return 0

    def personajes_con_iniciales(self, iniciales):
        personajes = []
        for personaje in self.pila:
            if personaje.nombre.startswith(iniciales):
                personajes.append(personaje)
        return personajes

pila_mcu = PilaMCU()
pila_mcu.apilar(PersonajeMCU("Iron Man", 3))
pila_mcu.apilar(PersonajeMCU("Capitán América", 6))
pila_mcu.apilar(PersonajeMCU("Hulk", 4))
pila_mcu.apilar(PersonajeMCU("Thor", 5))
pila_mcu.apilar(PersonajeMCU("Viuda Negra", 7))
pila_mcu.apilar(PersonajeMCU("Rocket Raccoon", 3))
pila_mcu.apilar(PersonajeMCU("Groot", 4))
pila_mcu.apilar(PersonajeMCU("Doctor Strange", 2))
pila_mcu.apilar(PersonajeMCU("Black Panther", 3))
pila_mcu.apilar(PersonajeMCU("Spider-Man", 4))

posicion_rocket = None
nombre_rocket = "Rocket Raccoon"
for i, personaje in enumerate(pila_mcu.pila[::-1], 1):
    if personaje.nombre == nombre_rocket:
        posicion_rocket = i
        break

if posicion_rocket is not None:
    print(nombre_rocket, "se encuentra en la posición", posicion_rocket)
else:
    print("Rocket Raccoon no se encuentra en la pila.")

posicion_groot = None
nombre_groot = "Groot"
for i, personaje in enumerate(pila_mcu.pila[::-1], 1):
    if personaje.nombre == nombre_groot:
        posicion_groot = i
        break

if posicion_groot is not None:
    print(nombre_groot, "se encuentra en la posición", posicion_groot)
else:
    print("Groot no se encuentra en la pila.")

personajes_mas_de_cinco = pila_mcu.personajes_mas_de_cinco_peliculas()
for personaje in personajes_mas_de_cinco:
    print(personaje.nombre, "aparece en", personaje.cantidad_peliculas, "películas")

cantidad_peliculas_viuda_negra = pila_mcu.cantidad_peliculas_viuda_negra()
print("La Viuda Negra participó en", cantidad_peliculas_viuda_negra, "películas")

personajes_iniciales_cdg = pila_mcu.personajes_con_iniciales("C") + pila_mcu.personajes_con_iniciales("D") + pila_mcu.personajes_con_iniciales("G")
for personaje in personajes_iniciales_cdg:
    print(personaje.nombre)