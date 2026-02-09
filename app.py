#listas doblemente ligadas

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self,dato):
        nuevo=Nodo(dato)

        if self.esta_vacia():
            self.cabeza= nuevo
            self.cola= nuevo
        else:
            nuevo.siguiente= self.cabeza
            self.cabeza.anterior= nuevo
            self.cabeza= nuevo 

    def insertar_final(self,dato):
        nuevo=Nodo(dato)

        if self.esta_vacia():
            self.cabeza= nuevo
            self.cola= nuevo

        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
        self.cola = nuevo

    def eliminar_inicio(self, dato):
        if self.esta_vacia():
            return None

        if self.cabeza.dato==self.cola.dato:
            self.cabeza= None
            self.cola= None

        else :
            self.cabeza= self.cabeza.siguiente
            self.cabeza.anterior=None

    def eliminar_final(self, dato):
        if self.esta_vacia():
            return None

        if self.cabeza.dato==self.cola.dato:
            self.cabeza= None
            self.cola= None
        else:
            self.cola= self.cola.anterior
            self.cola.siguiente=None
    
    def recorrer_adelante(self,dato):
        if self.esta_vacia():
            print("lista vacía")
            return

        print("recorriendo inicio---->fin")
        actual=self.cabeza
        while actual:
            print(actual.dato, end="->")
            actaual=actual.siguiente
        print("fin")

    def recorrer_atras(self,dato):
        if self.esta_vacia():
            print("lista vacía")
            return

        print("recorriendo fin---->inicio")
        actual=self.cola
        while actual:
            print(actual.dato, end="->")
            actaual=actual.anterior
        print("inicio")       
 
    def buscar(self,dato):
        actaul =self.cabeza
        while actual:
            if actual.dato==dato:
                return True
            actaual= actual.siguiente

        return False

    def __len__(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += contador
            actual=actual.siguiente
            return contador

    def __rtr__(self):
        if self.esta_vacía():
            return "Lista Vacía"

        elementos =[]
        actual =self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return"<=>".join(elementos)

lista=ListaDoble()
lista.insertar_final(10)
lista.insertar_final(20)
lista.insertar_final(30)

lista.insertar_inicio(40)
print(lista)

lista.recorrer_adelante()
lista.recorrer_atras()

print(f"Tamaño de la lista:{len(lista)}")

print(lista.buscar(40))