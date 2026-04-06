class Nodo:
    def __init__(self, nombre, genero, duracion, artista):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.artista = artista
        self.anterior = None
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None
        self.actual = None

    def AgregarCancionAlFinal(self, nombre, genero, duracion, artista):
        nodo = Nodo(nombre, genero, duracion, artista)

        if self.cabeza == None:
            self.cabeza = nodo
            nodo.siguiente = nodo
            nodo.anterior = nodo
            self.actual = nodo
        else:
            ultimo = self.cabeza.anterior
            ultimo.siguiente = nodo
            nodo.anterior = ultimo
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo

        print("Cancion agregada exitosamente.")

    def MostrarLista(self):
        if self.cabeza == None:
            print("Lista vacia")
            return

        actual = self.cabeza
        while True:
            print(actual.nombre, end="==>")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("Fin.")

    def Reproducir(self):
        if self.cabeza == None:
            print("No hay canciones")
            return
        if self.actual == None:
            self.actual = self.cabeza
        self.MostrarActual()

    def MostrarActual(self):
        if self.actual:
            print("Reproduciendo:")
            print("Nombre:", self.actual.nombre)
            print("Artista:", self.actual.artista)
            print("Genero:", self.actual.genero)
            print("Duracion:", self.actual.duracion)

    def Siguiente(self):
        if self.actual:
            self.actual = self.actual.siguiente
            self.MostrarActual()

    def Anterior(self):
        if self.actual:
            self.actual = self.actual.anterior
            self.MostrarActual()

    def BuscarPorNombre(self, nombre):
        if self.cabeza == None:
            print("Lista vacia")
            return

        actual = self.cabeza
        encontrados = []

        while True:
            if actual.nombre == nombre:
                encontrados.append(actual)
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        if len(encontrados) == 0:
            print("No se encontraron resultados para nombre:", nombre)
            return

        print("Encontrado(s):", len(encontrados))
        for c in encontrados:
            print("-", c.nombre, "|", c.artista, "|", c.genero, "|", c.duracion)

    def BuscarPorArtista(self, artista):
        if self.cabeza == None:
            print("Lista vacia")
            return

        actual = self.cabeza
        encontrados = []

        while True:
            if actual.artista == artista:
                encontrados.append(actual)
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        if len(encontrados) == 0:
            print("No se encontraron resultados para artista:", artista)
            return

        print("Canciones del artista:", artista)
        print("Encontrado(s):", len(encontrados))
        for c in encontrados:
            print("-", c.nombre, "|", c.artista, "|", c.genero, "|", c.duracion)

    def BuscarPorGenero(self, genero):
        if self.cabeza == None:
            print("Lista vacia")
            return

        actual = self.cabeza
        encontrados = []

        while True:
            if actual.genero == genero:
                encontrados.append(actual)
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        if len(encontrados) == 0:
            print("No se encontraron resultados para genero:", genero)
            return

        print("Canciones", genero + ":")
        print("Encontrado(s):", len(encontrados))
        for c in encontrados:
            print("-", c.nombre, "|", c.artista, "|", c.genero, "|", c.duracion)

    def MostrarPorGeneros(self):
        if self.cabeza == None:
            print("Lista vacia")
            return

        generos = {}

        actual = self.cabeza
        while True:
            if actual.genero not in generos:
                generos[actual.genero] = []
            generos[actual.genero].append(actual)
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        for g in generos:
            print("\nCanciones", g + ":")
            print("Encontrado(s):", len(generos[g]))
            for c in generos[g]:
                print("-", c.nombre, "|", c.artista, "|", c.genero, "|", c.duracion)

    def EliminarCancion(self, nombre):
        if self.cabeza == None:
            print("Lista vacia")
            return

        actual = self.cabeza

        while True:
            if actual.nombre == nombre:
                if actual.siguiente == actual:
                    self.cabeza = None
                    self.actual = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior

                    if actual == self.cabeza:
                        self.cabeza = actual.siguiente

                    if actual == self.actual:
                        self.actual = actual.siguiente

                print("Cancion eliminada:", nombre)
                return

            actual = actual.siguiente
            if actual == self.cabeza:
                break

        print("Cancion no encontrada:", nombre)


lista = ListaCircular()
lista.AgregarCancionAlFinal("Shape of You", "Pop", "4:20", "Ed Sheeran")
lista.AgregarCancionAlFinal("Believer", "Rock", "3:30", "Imagine Dragons")
lista.AgregarCancionAlFinal("Perfect", "Pop", "4:40", "Ed Sheeran")
lista.AgregarCancionAlFinal("Gasolina", "Reggaeton", "3:15", "Daddy Yankee")
lista.AgregarCancionAlFinal("Danza Kuduro", "Reggaeton", "3:18", "Don Omar")

lista.MostrarLista()
lista.Reproducir()
lista.Siguiente()

lista.BuscarPorGenero("Pop")
lista.BuscarPorArtista("Ed Sheeran")
lista.BuscarPorNombre("Believer")

lista.MostrarPorGeneros()

lista.EliminarCancion("Perfect")
lista.MostrarLista()
