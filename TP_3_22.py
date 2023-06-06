from collections import deque

class Personaje:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

# Crear una cola de personajes
cola_personajes = deque()

# Agregar personajes a la cola
cola_personajes.append(Personaje("Tony Stark", "Iron Man", "M"))
cola_personajes.append(Personaje("Steve Rogers", "Capitán América", "M"))
cola_personajes.append(Personaje("Natasha Romanoff", "Black Widow", "F"))
cola_personajes.append(Personaje("Carol Danvers", "Capitana Marvel", "F"))
cola_personajes.append(Personaje("Scott Lang", "Ant-Man", "M"))
cola_personajes.append(Personaje("Stephen Strange", "Doctor Strange", "M"))
cola_personajes.append(Personaje("Wanda Maximoff", "Scarlet Witch", "F"))

# Actividad a: determinar el nombre del personaje de la superhéroe Capitana Marvel
nombre_personaje_capitana_marvel = ""
for personaje in cola_personajes:
    if personaje.nombre_superheroe == "Capitana Marvel":
        nombre_personaje_capitana_marvel = personaje.nombre_personaje
        break

print("a. El nombre del personaje de la superhéroe Capitana Marvel es:", nombre_personaje_capitana_marvel)

# Actividad b: mostrar los nombre de los superhéroes femeninos
print("b. Los nombres de los superhéroes femeninos son:")
for personaje in cola_personajes:
    if personaje.genero == "F":
        print(personaje.nombre_superheroe)

# Actividad c: mostrar los nombres de los personajes masculinos
print("c. Los nombres de los personajes masculinos son:")
for personaje in cola_personajes:
    if personaje.genero == "M":
        print(personaje.nombre_personaje)

# Actividad d: determinar el nombre del superhéroe del personaje Scott Lang
nombre_superheroe_scott_lang = ""
for personaje in cola_personajes:
    if personaje.nombre_personaje == "Scott Lang":
        nombre_superheroe_scott_lang = personaje.nombre_superheroe
        break

print("d. El nombre del superhéroe del personaje Scott Lang es:", nombre_superheroe_scott_lang)

# Actividad e: mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
print("e. Los superhéroes o personajes cuyos nombres comienzan con la letra S son:")
for personaje in cola_personajes:
    if personaje.nombre_personaje.startswith("S"):
        print("Nombre del personaje:", personaje.nombre_personaje)
        print("Nombre del superhéroe:", personaje.nombre_superheroe)
        print("Género:", personaje.genero)
        print()

# Actividad f: determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
carol_danvers_presente = False
nombre_superheroe_carol_danvers = ""
for personaje in cola_personajes:
    if personaje.nombre_personaje == "Carol Danvers":
        carol_danvers_presente = True
        nombre_superheroe_carol_danvers = personaje.nombre_superheroe
        break

if carol_danvers_presente:
    print("f. El personaje Carol Danvers se encuentra en la cola.")
    print("   Nombre de su superhéroe:", nombre_superheroe_carol_danvers)
else:
    print("f. El personaje Carol Danvers no se encuentra en la cola.")
