class NodoArbol:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izquierda = None
        self.derecha = None

def insertar(raiz, nombre, es_heroe):
    if raiz is None:
        return NodoArbol(nombre, es_heroe)
    if nombre < raiz.nombre:
        raiz.izquierda = insertar(raiz.izquierda, nombre, es_heroe)
    elif nombre > raiz.nombre:
        raiz.derecha = insertar(raiz.derecha, nombre, es_heroe)
    return raiz

def encontrar_villanos_ordenados(raiz):
    if raiz is None:
        return []
    villanos = []
    villanos += encontrar_villanos_ordenados(raiz.izquierda)
    if not raiz.es_heroe:
        villanos.append(raiz.nombre)
    villanos += encontrar_villanos_ordenados(raiz.derecha)
    return sorted(villanos)

def encontrar_heroes_con_c(raiz):
    if raiz is None:
        return []
    heroes_c = []
    heroes_c += encontrar_heroes_con_c(raiz.izquierda)
    if raiz.es_heroe and raiz.nombre.startswith("C"):
        heroes_c.append(raiz.nombre)
    heroes_c += encontrar_heroes_con_c(raiz.derecha)
    return heroes_c

def contar_superheroes(raiz):
    if raiz is None:
        return 0
    cuenta = 0
    if raiz.es_heroe:
        cuenta += 1
    cuenta += contar_superheroes(raiz.izquierda)
    cuenta += contar_superheroes(raiz.derecha)
    return cuenta

def encontrar_y_renombrar_doctor_strange(raiz, nombre_objetivo):
    def encontrar_y_renombrar(nodo):
        if nodo:
            if nodo.nombre == nombre_objetivo:
                nodo.nombre = "Doctor Strange"
            encontrar_y_renombrar(nodo.izquierda)
            encontrar_y_renombrar(nodo.derecha)
    
    encontrar_y_renombrar(raiz)

def crear_bosque(raiz):
    arbol_heroes = None
    arbol_villanos = None

    def construir_bosque(nodo):
        nonlocal arbol_heroes, arbol_villanos
        if nodo:
            if nodo.es_heroe:
                arbol_heroes = insertar(arbol_heroes, nodo.nombre, True)
            else:
                arbol_villanos = insertar(arbol_villanos, nodo.nombre, False)
            construir_bosque(nodo.izquierda)
            construir_bosque(nodo.derecha)
    
    construir_bosque(raiz)
    return arbol_heroes, arbol_villanos

def contar_nodos_en_arbol(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos_en_arbol(raiz.izquierda) + contar_nodos_en_arbol(raiz.derecha)

def recorrido_en_orden_alfabetico(raiz):
    if raiz is None:
        return []
    resultado = recorrido_en_orden_alfabetico(raiz.izquierda)
    resultado.append(raiz.nombre)
    resultado += recorrido_en_orden_alfabetico(raiz.derecha)
    return resultado


raiz = None


# a. 
raiz = insertar(raiz, "Iron Man", True)
raiz = insertar(raiz, "Thor", True)
raiz = insertar(raiz, "Loki", False)
raiz = insertar(raiz, "Capitan America", True)
raiz = insertar(raiz, "Viuda Negra", True)
raiz = insertar(raiz, "Doctor Strange", True)
raiz = insertar(raiz, "Hulk", True)
raiz = insertar(raiz, "Thanos", False)

# b. 
villanos_ordenados = encontrar_villanos_ordenados(raiz)
print("Villanos ordenados alfabeticamente:", villanos_ordenados)

# c. 
heroes_con_c = encontrar_heroes_con_c(raiz)
print("Superheroes que empiezan con C:", heroes_con_c)

# d. 
num_superheroes = contar_superheroes(raiz)
print("Numero de superheroes en el arbol:", num_superheroes)

# e. 
encontrar_y_renombrar_doctor_strange(raiz, "Doctor Strange")

# f. 
heroes_en_orden_descendente = recorrido_en_orden_alfabetico(raiz)[::-1]
print("Superheroes en orden descendente:", heroes_en_orden_descendente)

# g. 
arbol_heroes, arbol_villanos = crear_bosque(raiz)

# h.1.
num_nodos_arbol_heroes = contar_nodos_en_arbol(arbol_heroes)
num_nodos_arbol_villanos = contar_nodos_en_arbol(arbol_villanos)
print("Numero de nodos en el arbol de heroes:", num_nodos_arbol_heroes)
print("Numero de nodos en el arbol de villanos:", num_nodos_arbol_villanos)

# h.2.
heroes_en_orden_alfabetico = recorrido_en_orden_alfabetico(arbol_heroes)
villanos_en_orden_alfabetico = recorrido_en_orden_alfabetico(arbol_villanos)

print("Barrido ordenado alfabeticamente en el arbol de heroes:", heroes_en_orden_alfabetico)
print("Barrido ordenado alfabeticamente en el arbol de villanos:", villanos_en_orden_alfabetico)