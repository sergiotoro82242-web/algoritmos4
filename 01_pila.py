"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 1: IMPLEMENTACIÓN DE PILA (STACK)
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════

La Pila es una estructura de datos LIFO (Last In, First Out).
El último elemento en entrar es el primero en salir.

Analogía: Una pila de platos - solo puedes poner o quitar del tope.
"""


class Nodo:
    """Nodo para la lista enlazada"""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    """
    Implementación de Pila usando lista enlazada.
    Todas las operaciones son O(1).
    """
    
    def __init__(self):
        self.tope = None
        self.tamanio = 0
    
    def esta_vacia(self):
        """Retorna True si la pila está vacía"""
        return self.tope is None
    
    def push(self, dato):
        """Agrega un elemento al tope de la pila - O(1)"""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamanio += 1
    
    def pop(self):
        """Quita y retorna el elemento del tope - O(1)"""
        if self.esta_vacia():
            raise Exception("Error: La pila está vacía")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return dato
    
    def peek(self):
        """Retorna el elemento del tope sin quitarlo - O(1)"""
        if self.esta_vacia():
            raise Exception("Error: La pila está vacía")
        return self.tope.dato
    
    def __len__(self):
        """Retorna el tamaño de la pila"""
        return self.tamanio
    
    def __str__(self):
        """Representación visual de la pila"""
        if self.esta_vacia():
            return "Pila vacía"
        
        elementos = []
        actual = self.tope
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        return "Tope → " + " → ".join(elementos) + " → None"


# ═══════════════════════════════════════════════════════════════════════════════
# DEMOSTRACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("       DEMOSTRACIÓN DE PILA (STACK)")
    print("=" * 50)
    
    pila = Pila()
    
    print("\n📥 Agregando elementos (push):")
    for valor in [10, 20, 30, 40]:
        pila.push(valor)
        print(f"   push({valor}) → {pila}")
    
    print(f"\n📊 Tamaño de la pila: {len(pila)}")
    print(f"👀 Elemento en el tope (peek): {pila.peek()}")
    
    print("\n📤 Quitando elementos (pop):")
    while not pila.esta_vacia():
        valor = pila.pop()
        print(f"   pop() = {valor} → {pila}")
    
    print("\n" + "=" * 50)
    print("💡 Observa: Los elementos salen en orden inverso")
    print("   al que entraron (LIFO)")
    print("=" * 50)
