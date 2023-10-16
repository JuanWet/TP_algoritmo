class Jedi:
    def __init__(self, nombre, especie, nacimiento, color_sable, ranking, maestros):
        self.nombre = nombre
        self.especie = especie
        self.nacimiento = nacimiento
        self.color_sable = color_sable
        self.ranking = ranking
        self.maestros = maestros
        self.izquierda = None
        self.derecha = None

def insertar_jedi_por_nombre(raiz, jedi):
    if raiz is None:
        return Jedi(nombre=jedi['nombre'], especie=jedi['especie'], nacimiento=jedi['nacimiento'],
                    color_sable=jedi['color_sable'], ranking=jedi['ranking'], maestros=jedi['maestros'])
    if jedi['nombre'] < raiz.nombre:
        raiz.izquierda = insertar_jedi_por_nombre(raiz.izquierda, jedi)
    else:
        raiz.derecha = insertar_jedi_por_nombre(raiz.derecha, jedi)
    return raiz

def insertar_jedi_por_ranking(raiz, jedi):
    if raiz is None:
        return Jedi(nombre=jedi['nombre'], especie=jedi['especie'], nacimiento=jedi['nacimiento'],
                    color_sable=jedi['color_sable'], ranking=jedi['ranking'], maestros=jedi['maestros'])
    if jedi['ranking'] < raiz.ranking:
        raiz.izquierda = insertar_jedi_por_ranking(raiz.izquierda, jedi)
    else:
        raiz.derecha = insertar_jedi_por_ranking(raiz.derecha, jedi)
    return raiz

def insertar_jedi_por_especie(raiz, jedi):
    if raiz is None:
        return Jedi(nombre=jedi['nombre'], especie=jedi['especie'], nacimiento=jedi['nacimiento'],
                    color_sable=jedi['color_sable'], ranking=jedi['ranking'], maestros=jedi['maestros'])
    if jedi['especie'] < raiz.especie:
        raiz.izquierda = insertar_jedi_por_especie(raiz.izquierda, jedi)
    else:
        raiz.derecha = insertar_jedi_por_especie(raiz.derecha, jedi)
    return raiz

def inorden(raiz):
    if raiz:
        inorden(raiz.izquierda)
        print(f"Nombre: {raiz.nombre}, Ranking: {raiz.ranking}")
        inorden(raiz.derecha)

def barrido_por_nivel(raiz):
    if raiz:
        cola = [raiz]
        while cola:
            nodo = cola.pop(0)
            print(f"Nombre: {nodo.nombre}, Ranking: {nodo.ranking}")
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)

def buscar_jedi_por_nombre(raiz, nombre_objetivo):
    if raiz is None:
        return None
    if nombre_objetivo < raiz.nombre:
        return buscar_jedi_por_nombre(raiz.izquierda, nombre_objetivo)
    elif nombre_objetivo > raiz.nombre:
        return buscar_jedi_por_nombre(raiz.derecha, nombre_objetivo)
    else:
        return raiz

def mostrar_informacion_jedi(nombre_arbol, nombre_objetivo):
    jedi = buscar_jedi_por_nombre(nombre_arbol, nombre_objetivo)
    if jedi:
        print(f"Informacion de {nombre_objetivo}:")
        print(f"Nombre: {jedi.nombre}")
        print(f"Especie: {jedi.especie}")
        print(f"Nacimiento: {jedi.nacimiento}")
        print(f"Color del sable de luz: {jedi.color_sable}")
        print(f"Ranking: {jedi.ranking}")
        print(f"Maestros: {', '.join(jedi.maestros)}")
    else:
        print(f"{nombre_objetivo} no encontrado.")

def listar_jedi_por_ranking(raiz, ranking_objetivo, result=None):
    if result is None:
        result = []

    if raiz:
        if raiz.ranking == ranking_objetivo:
            result.append(raiz)
        if ranking_objetivo < raiz.ranking:
            listar_jedi_por_ranking(raiz.izquierda, ranking_objetivo, result)
        if ranking_objetivo > raiz.ranking:
            listar_jedi_por_ranking(raiz.derecha, ranking_objetivo, result)

    return result

def listar_jedi_por_especie(jedi_data, especies_objetivo):
    result = []
    for jedi in jedi_data:
        if jedi['especie'] in especies_objetivo:
            result.append(jedi)
    return result

# Datos de Jedi
datos_jedi = [
    {
        'nombre': 'Yoda',
        'especie': 'Unknown',
        'nacimiento': 896,
        'color_sable': 'Verde',
        'ranking': 'Jedi Master',
        'maestros': ['N/A'],
    },
    {
        'nombre': 'Luke Skywalker',
        'especie': 'Human',
        'nacimiento': 19,
        'color_sable': 'Azul',
        'ranking': 'Jedi Knight',
        'maestros': ['Obi-Wan Kenobi', 'Yoda'],
    },
    {
        'nombre': 'Obi-Wan Kenobi',
        'especie': 'Human',
        'nacimiento': 57,
        'color_sable': 'Azul',
        'ranking': 'Jedi Master',
        'maestros': ['Qui-Gon Jinn'],
    },
    {
        'nombre': 'Ahsoka Tano',
        'especie': 'Togruta',
        'nacimiento': 36,
        'color_sable': 'Verde',
        'ranking': 'Jedi Knight',
        'maestros': ['Anakin Skywalker'],
    }
]

# Crear los árboles de acceso a los dato
arbol_nombre = None
arbol_ranking = None
arbol_especie = None

for jedi in datos_jedi:
    arbol_nombre = insertar_jedi_por_nombre(arbol_nombre, jedi)
    arbol_ranking = insertar_jedi_por_ranking(arbol_ranking, jedi)
    arbol_especie = insertar_jedi_por_especie(arbol_especie, jedi)

# b. 
print("Barrido en orden por Nombre:")
inorden(arbol_nombre)

print("\nBarrido en orden por Ranking:")
inorden(arbol_ranking)

# c. 
print("\nBarrido por Nivel del Arbol por Ranking:")
barrido_por_nivel(arbol_ranking)

print("\nBarrido por Nivel del Arbol por Especie:")
barrido_por_nivel(arbol_especie)

# d. 
mostrar_informacion_jedi(arbol_nombre, "Yoda")
mostrar_informacion_jedi(arbol_nombre, "Luke Skywalker")

# e. 
jedi_masters = listar_jedi_por_ranking(arbol_ranking, "Jedi Master")
print("\nJedi con ranking Jedi Master:")
for jedi in jedi_masters:
    print(jedi.nombre)

# f. 
def listar_jedi_por_color_sable(jedi_data, color_sable_objetivo):
    result = []
    for jedi in jedi_data:
        if jedi['color_sable'] == color_sable_objetivo:
            result.append(jedi['nombre'])
    return result

jedi_verde_sable = listar_jedi_por_color_sable(datos_jedi, "Verde")
print("\nJedi con sable de luz color verde:")
for jedi in jedi_verde_sable:
    print(jedi)

# g. 
def listar_jedi_con_maestros(jedi_data):
    result = []
    for jedi in jedi_data:
        for maestro in jedi['maestros']:
            if maestro in [j['nombre'] for j in jedi_data]:
                result.append(jedi['nombre'])
                break
    return result

jedi_con_maestros = listar_jedi_con_maestros(datos_jedi)
print("\nJedi con maestros:")
for jedi in jedi_con_maestros:
    print(jedi)

# h. 
especies_objetivo = ["Togruta", "Cerean"]
jedi_especies = listar_jedi_por_especie(datos_jedi, especies_objetivo)
print("\nJedi de especie Togruta o Cerean:")
for jedi in jedi_especies:
    print(jedi['nombre'])

# i. 
def listar_jedi_con_nombre_especial(jedi_data):
    result = []
    for jedi in jedi_data:
        if jedi['nombre'].startswith("A") or "-" in jedi['nombre']:
            result.append(jedi['nombre'])
    return result

jedi_especiales = listar_jedi_con_nombre_especial(datos_jedi)
print("\nJedi cuyos nombres comienzan con A o contienen un guion (-):")
for jedi in jedi_especiales:
    print(jedi)
