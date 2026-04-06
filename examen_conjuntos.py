"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL - CONJUNTOS
                    Validador de Sudoku + Sistema de Permisos
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
--------------
1. Completar las funciones donde dice TODO
2. No modificar el código base proporcionado


═══════════════════════════════════════════════════════════════════════════════
                            PARTE 1: VALIDADOR DE SUDOKU (3.5)
═══════════════════════════════════════════════════════════════════════════════

Usar conjuntos de Python para validar un tablero de Sudoku.

REGLAS DEL SUDOKU:
- Cada fila debe contener los números 1-9 sin repetir
- Cada columna debe contener los números 1-9 sin repetir
- Cada subcuadro 3x3 debe contener los números 1-9 sin repetir
"""

NUMEROS_VALIDOS = {1, 2, 3, 4, 5, 6, 7, 8, 9}

TABLERO = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


# PUNTO 1.1 (1.0): Validar una fila
def validar_fila(tablero, num_fila):
    """
    Retorna True si la fila contiene exactamente los números 1-9 sin repetir.
    
    Ejemplo:
        validar_fila(TABLERO, 0) -> True (fila [5,3,4,6,7,8,9,1,2])
    """
    fila = tablero[num_fila]
    return set(fila) == NUMEROS_VALIDOS


# PUNTO 1.2 (1.0): Validar una columna
def validar_columna(tablero, num_columna):
    """
    Retorna True si la columna contiene exactamente los números 1-9 sin repetir.
    
    
    Ejemplo:
        validar_columna(TABLERO, 0) -> True (columna [5,6,1,8,4,7,9,2,3])
    """
    columna = []

    for fila in tablero:
        columna.append(fila[num_columna])

    return set(columna) == NUMEROS_VALIDOS


# PUNTO 1.3 (1.5): Validar un subcuadro 3x3
def validar_subcuadro(tablero, fila_inicio, col_inicio):
    """
    Retorna True si el subcuadro 3x3 contiene exactamente los números 1-9.
    
    fila_inicio y col_inicio indican la esquina superior izquierda del subcuadro.
    Los valores válidos son: 0, 3, 6
    
    Ejemplo:
        validar_subcuadro(TABLERO, 0, 0) -> True (subcuadro superior izquierdo)
        validar_subcuadro(TABLERO, 3, 6) -> True (subcuadro central derecho)
    
    """
    elementos = []

    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(col_inicio, col_inicio + 3):
            elementos.append(tablero[i][j])

    return set(elementos) == NUMEROS_VALIDOS


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 2: SISTEMA DE PERMISOS CON LISTAS (2.0)
═══════════════════════════════════════════════════════════════════════════════

Implementar operaciones de subconjuntos usando la clase Conjunto con listas enlazadas.

CONTEXTO:
Un sistema tiene roles con diferentes permisos. Debes verificar si un rol
tiene todos los permisos necesarios para realizar ciertas acciones.
"""


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO BASE - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0
        if elementos:
            for e in elementos:
                self.agregar(e)
    
    def esta_vacio(self):
        return self.cabeza is None
    
    def pertenece(self, x):
        """Retorna True si x está en el conjunto"""
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x):
        """Agrega x si no existe"""
        if self.pertenece(x):
            return False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True
    
    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "{" + ", ".join(elementos) + "}"


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTOS A IMPLEMENTAR
# ═══════════════════════════════════════════════════════════════════════════════

# PUNTO 2.1 (1.0): Verificar si es subconjunto
def es_subconjunto(conjunto_a, conjunto_b):
    """
    Retorna True si conjunto_a es subconjunto de conjunto_b.
    Es decir, si TODOS los elementos de A están en B.
    
    A ⊆ B significa: para todo x en A, x también está en B
    """
    actual = conjunto_a.cabeza

    while actual:
        if not conjunto_b.pertenece(actual.dato):
            return False
        actual = actual.siguiente

    return True


# PUNTO 2.2 (0.5): Verificar permisos de usuario
def tiene_permisos(permisos_usuario, permisos_requeridos):
    """
    Retorna True si el usuario tiene TODOS los permisos requeridos.
    """
    return es_subconjunto(permisos_requeridos, permisos_usuario)