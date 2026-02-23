"""
TALLER: LISTAS LIGADAS + RECURSIVIDAD (Python)
Incluye:
1) Lista simple (ya la tenías)
2) Lista doble (más funciones recursivas)
3) Lista circular (funciones recursivas con control para no ciclar infinito)

Basado en tus ejemplos:
- Caso base: condición para parar (como len(s)<=1 o nodo is None)
- Paso recursivo: llamada con un problema más pequeño (como nodo.siguiente)
- En listas circulares: el caso base suele ser "volví al inicio"
"""

# ============================================================
# 1) DEFINICIONES BASE
# ============================================================

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo = NodoSimple(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")


class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def mostrar_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

    def mostrar_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.anterior
        print("None")


class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    """
    Lista circular simple:
    - Si tiene nodos, el último nodo apunta de vuelta a la cabeza.
    """
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, dato):
        """
        Inserción iterativa para armar ejemplos:
        - Si está vacía: cabeza apunta a sí misma.
        - Si no: buscar último y enlazar.
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
        Mostrar iterativo con límite por seguridad.
        """
        if self.cabeza is None:
            print("ListaCircular vacía")
            return
        actual = self.cabeza
        for _ in range(limite):
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("(vuelve a cabeza)")


# ============================================================
# 2) RECURSIVIDAD EN LISTA DOBLE (más ejemplos)
# ============================================================

def contar_doble_rec(nodo):
    """
    Contar nodos yendo hacia adelante (cabeza -> cola).

    Caso base:
    - nodo None => 0

    Paso recursivo:
    - 1 + contar del siguiente
    """
    if nodo is None:
        return 0
    return 1 + contar_doble_rec(nodo.siguiente)


def sumar_doble_rec(nodo):
    """
    Sumar valores yendo hacia adelante.

    Caso base: nodo None => 0
    Paso recursivo: dato actual + suma del siguiente
    """
    if nodo is None:
        return 0
    return nodo.dato + sumar_doble_rec(nodo.siguiente)


def buscar_doble_adelante_rec(nodo, dato):
    """
    Buscar yendo hacia adelante.

    Caso base: nodo None => False
    Éxito: nodo.dato == dato => True
    Paso recursivo: buscar en nodo.siguiente
    """
    if nodo is None:
        return False
    if nodo.dato == dato:
        return True
    return buscar_doble_adelante_rec(nodo.siguiente, dato)


def buscar_doble_atras_rec(nodo, dato):
    """
    Buscar yendo hacia atrás (cola -> cabeza).

    Caso base: nodo None => False
    Éxito: nodo.dato == dato => True
    Paso recursivo: buscar en nodo.anterior
    """
    if nodo is None:
        return False
    if nodo.dato == dato:
        return True
    return buscar_doble_atras_rec(nodo.anterior, dato)


def imprimir_doble_adelante_rec(nodo):
    """
    Imprimir de cabeza a cola (recursivo).

    Caso base: nodo None => parar
    Paso recursivo: imprimir actual y seguir
    """
    if nodo is None:
        return
    print(nodo.dato, end=" ")
    imprimir_doble_adelante_rec(nodo.siguiente)


def imprimir_doble_atras_rec(nodo):
    """
    Imprimir de cola a cabeza (recursivo).

    Caso base: nodo None => parar
    Paso recursivo: imprimir actual y moverse al anterior
    """
    if nodo is None:
        return
    print(nodo.dato, end=" ")
    imprimir_doble_atras_rec(nodo.anterior)


def eliminar_primera_doble_rec(nodo, dato):
    """
    Eliminar primera aparición (recursivo) en lista doble.

    Importante:
    - Retornamos la nueva cabeza de esa "sublista"
    - Ajustamos enlaces anterior/siguiente

    Caso base:
    - nodo None => None

    Caso eliminación:
    - si nodo.dato == dato:
        retornamos nodo.siguiente y además arreglamos su anterior (si existe)

    Paso recursivo:
    - nodo.siguiente = eliminar_primera_doble_rec(nodo.siguiente, dato)
      y si nodo.siguiente existe => su anterior debe apuntar a nodo
    """
    if nodo is None:
        return None

    if nodo.dato == dato:
        nuevo_inicio = nodo.siguiente
        if nuevo_inicio is not None:
            nuevo_inicio.anterior = nodo.anterior
        return nuevo_inicio

    nodo.siguiente = eliminar_primera_doble_rec(nodo.siguiente, dato)
    if nodo.siguiente is not None:
        nodo.siguiente.anterior = nodo
    return nodo


def es_palindromo_lista_doble(izq, der):
    """
    Palíndromo en lista doble (como tu es_palindromo del string).

    Caso base:
    - izq == der (centro) => True
    - izq.anterior == der (se cruzaron) => True

    Caso fallo:
    - izq.dato != der.dato => False

    Paso recursivo:
    - avanzar hacia centro: (izq.siguiente, der.anterior)
    """
    if izq is None or der is None:
        return True

    if izq == der or izq.anterior == der:
        return True

    if izq.dato != der.dato:
        return False

    return es_palindromo_lista_doble(izq.siguiente, der.anterior)


def invertir_doble_rec(nodo):
    """
    Invertir lista doble recursivamente (retorna la nueva cabeza).

    Idea:
    - Similar a invertir lista simple, pero hay que ajustar anterior también.

    Caso base:
    - nodo None o nodo.siguiente None => este nodo será la nueva cabeza.

    Paso recursivo:
    - invierto desde el siguiente y luego reconecto.

    Reconexión:
    - Sea A=nodo, B=nodo.siguiente
      Queremos que B apunte a A:
        B.siguiente = A
        A.anterior = B
      Y A queda como final de esa parte:
        A.siguiente = None
    """
    if nodo is None or nodo.siguiente is None:
        if nodo is not None:
            nodo.anterior = None  # la nueva cabeza no tiene anterior
        return nodo

    nueva_cabeza = invertir_doble_rec(nodo.siguiente)

    # B = nodo.siguiente
    b = nodo.siguiente
    b.siguiente = nodo
    nodo.anterior = b

    nodo.siguiente = None

    return nueva_cabeza


def actualizar_cola_doble(cabeza):
    """
    Después de invertir/eliminar, a veces toca recalcular cola.
    Esto es iterativo por simplicidad.
    """
    if cabeza is None:
        return None
    actual = cabeza
    while actual.siguiente:
        actual = actual.siguiente
    return actual


# ============================================================
# 3) RECURSIVIDAD EN LISTA CIRCULAR
# ============================================================

def contar_circular_rec(actual, cabeza):
    """
    Contar nodos en lista circular.

    Caso base:
    - Si cabeza es None => lista vacía => 0 (pero eso se maneja antes)
    - Si actual.siguiente == cabeza => actual es el último => contamos 1 y paramos
      (esto evita ciclo infinito)

    Paso recursivo:
    - 1 + contar del siguiente
    """
    if actual.siguiente == cabeza:
        return 1
    return 1 + contar_circular_rec(actual.siguiente, cabeza)


def buscar_circular_rec(actual, cabeza, dato):
    """
    Buscar un dato en lista circular.

    Caso base de éxito:
    - si actual.dato == dato => True

    Caso base de parada (no encontrado):
    - si actual.siguiente == cabeza => ya dimos la vuelta completa y no estaba => False

    Paso recursivo:
    - buscar en el siguiente
    """
    if actual.dato == dato:
        return True
    if actual.siguiente == cabeza:
        return False
    return buscar_circular_rec(actual.siguiente, cabeza, dato)


def imprimir_circular_rec(actual, cabeza):
    """
    Imprimir circular recursivo.

    Caso base:
    - si actual.siguiente == cabeza:
        imprimo actual y paro (para no repetir cabeza infinito)

    Paso recursivo:
    - imprimo y avanzo
    """
    print(actual.dato, end=" -> ")
    if actual.siguiente == cabeza:
        print("(vuelve a cabeza)")
        return
    imprimir_circular_rec(actual.siguiente, cabeza)


def sumar_circular_rec(actual, cabeza):
    """
    Sumar en lista circular.

    Caso base:
    - si actual.siguiente == cabeza => último => retorno su dato

    Paso recursivo:
    - dato actual + suma del siguiente
    """
    if actual.siguiente == cabeza:
        return actual.dato
    return actual.dato + sumar_circular_rec(actual.siguiente, cabeza)


def eliminar_primera_circular_rec(actual, cabeza, dato):
    """
    Eliminar primera aparición en lista circular (recursivo).
    Retorna la nueva cabeza.

    Casos importantes:
    1) Lista vacía => None
    2) Si la cabeza tiene el dato:
       - Si solo hay un nodo (cabeza.siguiente == cabeza) => retorna None
       - Si hay más:
         - buscamos el último para reconectar (iterativo por claridad)
         - nuevo_inicio = cabeza.siguiente
         - ultimo.siguiente = nuevo_inicio
         - retorna nuevo_inicio
    3) Si no es cabeza:
       - recorremos recursivamente llevando actual (nodo anterior)
       - caso base de parada: si actual.siguiente == cabeza => dimos la vuelta => no encontrado
       - si actual.siguiente.dato == dato => saltamos ese nodo
    """
    if cabeza is None:
        return None

    # Caso: eliminar en cabeza
    if cabeza.dato == dato:
        if cabeza.siguiente == cabeza:
            return None  # solo había un nodo

        # buscar último para apuntar al nuevo inicio
        ultimo = cabeza
        while ultimo.siguiente != cabeza:
            ultimo = ultimo.siguiente

        nuevo_inicio = cabeza.siguiente
        ultimo.siguiente = nuevo_inicio
        return nuevo_inicio

    # Caso: eliminar en el resto (usamos 'actual' como nodo anterior)
    # Si ya dimos la vuelta, no está
    if actual.siguiente == cabeza:
        return cabeza

    # Si el siguiente es el que hay que borrar, lo saltamos
    if actual.siguiente.dato == dato:
        actual.siguiente = actual.siguiente.siguiente
        return cabeza

    # Paso recursivo: avanzar
    return eliminar_primera_circular_rec(actual.siguiente, cabeza, dato)


# ============================================================
# 4) PRUEBAS / EJEMPLOS
# ============================================================

if __name__ == "__main__":
    print("LISTA DOBLE: crear")
    ld = ListaDoble()
    for x in [1, 2, 3, 2, 1]:
        ld.insertar_final(x)
    ld.mostrar_adelante()

    print("Contar doble (rec):", contar_doble_rec(ld.cabeza))
    print("Sumar doble (rec):", sumar_doble_rec(ld.cabeza))
    print("Buscar 3 adelante (rec):", buscar_doble_adelante_rec(ld.cabeza, 3))
    print("Buscar 3 atrás (rec):", buscar_doble_atras_rec(ld.cola, 3))

    print("Imprimir doble adelante (rec):", end=" ")
    imprimir_doble_adelante_rec(ld.cabeza)
    print()

    print("Imprimir doble atrás (rec):", end=" ")
    imprimir_doble_atras_rec(ld.cola)
    print()

    print("Palíndromo doble (rec):", es_palindromo_lista_doble(ld.cabeza, ld.cola))

    print("Eliminar primera '2' doble (rec):")
    ld.cabeza = eliminar_primera_doble_rec(ld.cabeza, 2)
    ld.cola = actualizar_cola_doble(ld.cabeza)
    ld.mostrar_adelante()

    print("Invertir doble (rec):")
    ld.cabeza = invertir_doble_rec(ld.cabeza)
    ld.cola = actualizar_cola_doble(ld.cabeza)
    ld.mostrar_adelante()
    ld.mostrar_atras()

    print("\nLISTA CIRCULAR: crear")
    lc = ListaCircular()
    for x in [10, 20, 30, 40]:
        lc.insertar_final(x)
    lc.mostrar()

    print("Imprimir circular (rec):")
    imprimir_circular_rec(lc.cabeza, lc.cabeza)

    print("Contar circular (rec):", contar_circular_rec(lc.cabeza, lc.cabeza))
    print("Sumar circular (rec):", sumar_circular_rec(lc.cabeza, lc.cabeza))
    print("Buscar 30 circular (rec):", buscar_circular_rec(lc.cabeza, lc.cabeza, 30))
    print("Buscar 99 circular (rec):", buscar_circular_rec(lc.cabeza, lc.cabeza, 99))

    print("Eliminar 20 circular (rec):")
    lc.cabeza = eliminar_primera_circular_rec(lc.cabeza, lc.cabeza, 20)
    lc.mostrar()

    print("Eliminar 10 (cabeza) circular (rec):")
    lc.cabeza = eliminar_primera_circular_rec(lc.cabeza, lc.cabeza, 10)
    lc.mostrar()