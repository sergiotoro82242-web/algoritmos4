class Nodo:
    def __init__(self, nombre, cedula, prioridad):
        self.nombre = nombre
        self.cedula = cedula
        self.prioridad = prioridad
        self.siguiente = None


class Lista:
    def __init__(self):
        self.cabeza = None

    def AgregarNodoAlFinal(self, nombre, cedula, prioridad):
        nodo = Nodo(nombre, cedula, prioridad)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo
        print("Nodo agregado exitosamente.")

    def MostraNodo(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.nombre} (Prioridad: {actual.prioridad}) ==> ", end="")
            actual = actual.siguiente
        print("Fin.")

    def AgregarConPrioridad(self, nombre, cedula, prioridad):
        nodo = Nodo(nombre, cedula, prioridad)

        if self.cabeza is None:
            self.cabeza = nodo
        elif self.cabeza.prioridad > prioridad:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nodo.siguiente = actual.siguiente
            actual.siguiente = nodo


# Prueba
lista = Lista()
lista.AgregarNodoAlFinal("Juan", 111, 2)
lista.AgregarNodoAlFinal("Camila", 112, 3)
lista.AgregarNodoAlFinal("Pedro", 113, 1)
lista.MostraNodo()