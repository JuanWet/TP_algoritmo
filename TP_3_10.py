class Pila:
    def __init__(self):
        self.dioses = []

    # Insertar el nombre de Atenea en la posición deseada debajo de la cima
    def insertar_atenea(self, nombre, posicion):
        # Obtener la posición de la cima
        cima = len(self.dioses) - 1
        
        # Desplazar los elementos debajo de la cima hacia abajo
        self.dioses.append(None)  # Agregar un elemento temporal al final de la lista
        for i in range(cima, posicion - 1, -1):
            self.dioses[i + 1] = self.dioses[i]
        
        # Insertar Atenea en la posición deseada
        self.dioses[posicion] = nombre

    # Imprimir la pila de nombres de dioses griegos
    def imprimir_pila(self):
        for nombre in reversed(self.dioses):
            print(nombre)

# Crear una instancia de la pila
pila_dioses = Pila()

# Agregar nombres de dioses griegos a la pila
pila_dioses.dioses.append('Zeus')
pila_dioses.dioses.append('Poseidón')
pila_dioses.dioses.append('Apolo')
pila_dioses.dioses.append('Afrodita')

# Insertar Atenea en la posición deseada (por ejemplo, i=2)
pila_dioses.insertar_atenea('Atenea', 2)

# Imprimir la pila de nombres de dioses griegos
pila_dioses.imprimir_pila()