"""
MATERIAL DE RECURSIVIDAD (estilo profe Juan Esteban)
Incluye:
1) Potencia recursiva (normal) y potencia optimizada (divide y vencerás)
2) Búsqueda binaria recursiva
3) Adaptación a LISTAS LIGADAS (simple y circular) con recursividad, manteniendo el mismo estilo:
   - Caso base: condición para parar
   - Caso recursivo: llamada con un problema más pequeño

Nota:
- La búsqueda binaria requiere acceso por índice, por eso es ideal en arreglos/listas normales.
- En listas ligadas NO conviene binaria (no hay acceso directo), pero igual se puede:
  a) hacer búsqueda lineal recursiva (lo correcto)
  b) o convertir a lista normal y aplicar binaria (también se muestra)
"""

# ============================================================
# 1) EJERCICIO: POTENCIA RECURSIVA
# ============================================================

def potencia(base, exponente):
    """
    Calcula base^exponente recursivamente.

    Caso base:
    - exponente == 0 -> retorna 1

    Caso recursivo:
    - base * potencia(base, exponente - 1)
    """
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


def potencia_optimizada(base, exponente):
    """
    Versión optimizada (O(log n)) usando:
    - Si exponente es par: base^n = (base^(n/2))^2
    - Si exponente es impar: base^n = base * base^(n-1)

    Caso base:
    - exponente == 0 -> 1

    Caso recursivo:
    - par: llamar con exponente//2
    - impar: llamar con exponente-1
    """
    if exponente == 0:
        return 1

    if exponente % 2 == 0:
        mitad = potencia_optimizada(base, exponente // 2)
        return mitad * mitad
    else:
        return base * potencia_optimizada(base, exponente - 1)


# ============================================================
# 2) EJERCICIO: BUSQUEDA BINARIA RECURSIVA
# ============================================================

def busqueda_binaria(lista, objetivo, inicio=0, fin=None):
    """
    Búsqueda binaria recursiva en lista ORDENADA.

    Caso base:
    - inicio > fin -> no encontrado (-1)

    Paso recursivo:
    - calcular medio
    - si objetivo < lista[medio] -> buscar en mitad izquierda
    - si objetivo > lista[medio] -> buscar en mitad derecha
    """
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return -1

    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio
    elif objetivo < lista[medio]:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)


# ============================================================
# 3) LISTAS LIGADAS (SIMPLE) + RECURSIVIDAD (equivalente al estilo del profe)
# ============================================================

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, dato):
        """
        Inserción iterativa para construir ejemplos rápido.
        (La recursividad se usa en las operaciones que se piden).
        """
        nuevo = NodoSimple(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")


def buscar_lineal_rec(nodo, objetivo):
    """
    Búsqueda lineal recursiva en lista ligada (lo correcto en listas ligadas).

    Caso base:
    - nodo is None -> no encontrado (False)

    Caso éxito:
    - nodo.dato == objetivo -> True

    Paso recursivo:
    - buscar en el siguiente nodo
    """
    if nodo is None:
        return False
    if nodo.dato == objetivo:
        return True
    return buscar_lineal_rec(nodo.siguiente, objetivo)


def contar_rec(nodo):
    """
    Contar nodos recursivamente.

    Caso base: nodo None -> 0
    Caso recursivo: 1 + contar_rec(nodo.siguiente)
    """
    if nodo is None:
        return 0
    return 1 + contar_rec(nodo.siguiente)


def a_lista_python_rec(nodo, acumulado=None):
    """
    Convertir lista ligada a lista normal (Python) usando recursividad.
    Esto permite luego usar búsqueda binaria si la lista ligada está ordenada.

    Caso base:
    - nodo None -> devolver acumulado

    Paso recursivo:
    - agregar dato y avanzar
    """
    if acumulado is None:
        acumulado = []
    if nodo is None:
        return acumulado
    acumulado.append(nodo.dato)
    return a_lista_python_rec(nodo.siguiente, acumulado)


def busqueda_binaria_desde_lista_ligada(cabeza, objetivo):
    """
    Alternativa: convertir a lista normal y aplicar búsqueda binaria.
    (Funciona solo si la lista ligada está ordenada).
    """
    lista_normal = a_lista_python_rec(cabeza)
    return busqueda_binaria(lista_normal, objetivo)


# ============================================================
# 4) LISTA CIRCULAR (SIMPLE) + RECURSIVIDAD
# ============================================================

class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, dato):
        """
        Inserción iterativa para construir ejemplos rápido.
        En una lista circular, el último apunta a la cabeza.
        """
        nuevo = NodoCircular(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = nuevo
            return

        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            actual = actual.siguiente
        actual.siguiente = nuevo
        nuevo.siguiente = self.cabeza

    def mostrar(self, limite=20):
        """
        Mostrar iterativo con límite de seguridad.
        """
        if self.cabeza is None:
            print("Circular vacía")
            return
        actual = self.cabeza
        for _ in range(limite):
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("(vuelve a cabeza)")


def buscar_circular_rec(actual, cabeza, objetivo, primero=True):
    """
    Buscar recursivamente en lista circular.

    Caso éxito:
    - actual.dato == objetivo -> True

    Caso base de parada:
    - si NO es la primera llamada y actual == cabeza -> dimos la vuelta completa -> False

    Paso recursivo:
    - buscar en actual.siguiente
    """
    if actual is None or cabeza is None:
        return False

    if actual.dato == objetivo:
        return True

    if (not primero) and actual == cabeza:
        return False

    return buscar_circular_rec(actual.siguiente, cabeza, objetivo, primero=False)


def contar_circular_rec(actual, cabeza, primero=True):
    """
    Contar recursivamente en lista circular.

    Caso base:
    - si NO es la primera llamada y actual == cabeza -> ya volvimos al inicio -> 0

    Paso recursivo:
    - 1 + contar del siguiente
    """
    if actual is None or cabeza is None:
        return 0

    if (not primero) and actual == cabeza:
        return 0

    return 1 + contar_circular_rec(actual.siguiente, cabeza, primero=False)


def sumar_circular_rec(actual, cabeza, primero=True):
    """
    Sumar recursivamente en lista circular.

    Caso base:
    - si NO es la primera llamada y actual == cabeza -> 0

    Paso recursivo:
    - dato actual + sumar del siguiente
    """
    if actual is None or cabeza is None:
        return 0

    if (not primero) and actual == cabeza:
        return 0

    return actual.dato + sumar_circular_rec(actual.siguiente, cabeza, primero=False)


# ============================================================
# 5) PRUEBAS (como el material del profe)
# ============================================================

if __name__ == "__main__":
    print("=== PRUEBAS POTENCIA ===")
    casos_pot = [(2, 0, 1), (2, 3, 8), (3, 4, 81), (5, 3, 125)]
    for b, e, esperado in casos_pot:
        r = potencia(b, e)
        print(f"potencia({b},{e}) = {r} (esperado: {esperado})")

    print("\n=== PRUEBAS POTENCIA OPTIMIZADA ===")
    for b, e, esperado in casos_pot:
        r = potencia_optimizada(b, e)
        print(f"potencia_optimizada({b},{e}) = {r} (esperado: {esperado})")

    print("\n=== PRUEBAS BUSQUEDA BINARIA ===")
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    objetivos = [7, 1, 19, 10, 0, 20]
    for obj in objetivos:
        print(f"buscar({obj}) = {busqueda_binaria(lista, obj)}")

    print("\n=== LISTA SIMPLE + RECURSIVIDAD ===")
    ls = ListaSimple()
    for x in [1, 3, 5, 7, 9, 11]:
        ls.insertar_final(x)
    ls.mostrar()

    print("Buscar lineal rec 7:", buscar_lineal_rec(ls.cabeza, 7))
    print("Buscar lineal rec 4:", buscar_lineal_rec(ls.cabeza, 4))
    print("Contar rec:", contar_rec(ls.cabeza))

    print("Binaria desde lista ligada (ordenada) buscar 11:",
          busqueda_binaria_desde_lista_ligada(ls.cabeza, 11))
    print("Binaria desde lista ligada (ordenada) buscar 4:",
          busqueda_binaria_desde_lista_ligada(ls.cabeza, 4))

    print("\n=== LISTA CIRCULAR + RECURSIVIDAD ===")
    lc = ListaCircular()
    for x in [10, 20, 30, 40]:
        lc.insertar_final(x)
    lc.mostrar()

    print("Contar circular rec:", contar_circular_rec(lc.cabeza, lc.cabeza))
    print("Sumar circular rec:", sumar_circular_rec(lc.cabeza, lc.cabeza))
    print("Buscar 30 circular rec:", buscar_circular_rec(lc.cabeza, lc.cabeza, 30))
    print("Buscar 99 circular rec:", buscar_circular_rec(lc.cabeza, lc.cabeza, 99))