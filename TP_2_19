pila_peliculas = [
    ("Guardianes de la galaxia", 2014),
    ("Capitan America", 2014),
    ("Black Panther", 2018),
    ("Ant-Man y la Avispa", 2018),
    ("Captain America: Civil War", 2016),
    ("Doctor Strange", 2016),
]

peliculas_2014 = []
peliculas_2018 = []
peliculas_2016 = []


def pelicula_año(pila, año, peliculas):
    pila_aux = []
    while len(pila) > 0:
        pelicula = pila.pop()
        if pelicula[1] == año:
            peliculas.append(pelicula[0])
        pila_aux.append(pelicula)
    while len(pila_aux) > 0:
        pila.append(pila_aux.pop())
    return peliculas


peliculas_2014 = pelicula_año(pila_peliculas, 2014, peliculas_2014)
peliculas_2016 = pelicula_año(pila_peliculas, 2016, peliculas_2016)
peliculas_2018 = pelicula_año(pila_peliculas, 2018, peliculas_2018)

print("peliculas estrenada en el 2014", peliculas_2014)
print("peliculas estrenadas en el 2016", peliculas_2016)
print("peliculas estrenada en el año 2018", peliculas_2018)
