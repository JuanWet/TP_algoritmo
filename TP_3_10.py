class Pila:
    def __init__(self):
        self.dioses = []
        
    def insertar_atenea(self, nombre, posicion):
        cima = len(self.dioses) - 1
        
        self.dioses.append(None)  # Agregar un elemento temporal al final de la lista
        for i in range(cima, posicion - 1, -1):
            self.dioses[i + 1] = self.dioses[i]
        
        self.dioses[posicion] = nombre

    def imprimir_pila(self):
        for nombre in reversed(self.dioses):
            print(nombre)

pila_dioses = Pila()

pila_dioses.dioses.append('Zeus')
pila_dioses.dioses.append('Poseidón')
pila_dioses.dioses.append('Apolo')
pila_dioses.dioses.append('Afrodita')

pila_dioses.insertar_atenea('Atenea', 2)

pila_dioses.imprimir_pila()
