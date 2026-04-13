# =========================================================
# PARTE 1 — CONJUNTOS SIN LISTAS ENLAZADAS (SETS)
# =========================================================

# Un conjunto NO permite repetidos
A = {1,2,3}
B = {3,4,5}

print(A)
print(B)


# ---------------------------------------------------------
# UNION -> todos los elementos sin repetir
# ---------------------------------------------------------
print(A | B)     # {1,2,3,4,5}


# ---------------------------------------------------------
# INTERSECCION -> elementos comunes
# ---------------------------------------------------------
print(A & B)     # {3}


# ---------------------------------------------------------
# DIFERENCIA -> elementos en A que no estan en B
# ---------------------------------------------------------
print(A - B)     # {1,2}


# ---------------------------------------------------------
# DIFERENCIA INVERSA
# ---------------------------------------------------------
print(B - A)     # {4,5}


# ---------------------------------------------------------
# DIFERENCIA SIMETRICA
# elementos que estan en uno o en otro pero no en ambos
# ---------------------------------------------------------
print(A ^ B)     # {1,2,4,5}


# ---------------------------------------------------------
# SUBCONJUNTO
# ---------------------------------------------------------
C = {1,2}
D = {1,2,3,4}

print(C.issubset(D))   # True
print(D.issubset(C))   # False


# ---------------------------------------------------------
# ELIMINAR REPETIDOS
# ---------------------------------------------------------
lista = [1,2,2,3,3,4]

sin_repetidos = set(lista)

print(sin_repetidos)   # {1,2,3,4}


# ---------------------------------------------------------
# DETECTAR REPETIDOS
# ---------------------------------------------------------
def tiene_repetidos(lista):

    # si el tamaño cambia habia repetidos
    return len(lista) != len(set(lista))

print(tiene_repetidos([1,2,3,3]))   # True
print(tiene_repetidos([1,2,3]))     # False


# =========================================================
# VALIDAR LISTA 1..9
# =========================================================

def validar_lista(lista):

    # compara con numeros 1 al 9
    return set(lista) == set(range(1,10))

print(validar_lista([1,2,3,4,5,6,7,8,9]))


# =========================================================
# EJEMPLOS EXTRA DE CONJUNTOS
# =========================================================

A = {1,2,3,4}
B = {2,4}

# B es subconjunto de A
print(B.issubset(A))  # True

# union
print(A | B)

# interseccion
print(A & B)

# diferencia
print(A - B)

# simetrica
print(A ^ B)


# =========================================================
# PARTE 2 — SUDOKU
# =========================================================

NUMEROS_VALIDOS = set(range(1,10))

TABLERO = [
[5,3,4,6,7,8,9,1,2],
[6,7,2,1,9,5,3,4,8],
[1,9,8,3,4,2,5,6,7],
[8,5,9,7,6,1,4,2,3],
[4,2,6,8,5,3,7,9,1],
[7,1,3,9,2,4,8,5,6],
[9,6,1,5,3,7,2,8,4],
[2,8,7,4,1,9,6,3,5],
[3,4,5,2,8,6,1,7,9]
]


# ---------------------------------------------------------
# VALIDAR FILA
# ---------------------------------------------------------
def validar_fila(tablero, num_fila):

    fila = tablero[num_fila]

    # convierte a set y compara
    return set(fila) == NUMEROS_VALIDOS


print(validar_fila(TABLERO,0))


# ---------------------------------------------------------
# VALIDAR COLUMNA
# ---------------------------------------------------------
def validar_columna(tablero, num_col):

    columna = []

    # recorrer filas
    for fila in tablero:
        columna.append(fila[num_col])

    return set(columna) == NUMEROS_VALIDOS


print(validar_columna(TABLERO,0))


# ---------------------------------------------------------
# VALIDAR SUBCUADRO
# ---------------------------------------------------------
def validar_subcuadro(tablero, fila_inicio, col_inicio):

    elementos = []

    # recorrer subcuadro 3x3
    for i in range(fila_inicio, fila_inicio+3):
        for j in range(col_inicio, col_inicio+3):

            elementos.append(tablero[i][j])

    return set(elementos) == NUMEROS_VALIDOS


print(validar_subcuadro(TABLERO,0,0))


# ---------------------------------------------------------
# VALIDAR TODO EL SUDOKU
# ---------------------------------------------------------
def validar_sudoku(tablero):

    # validar filas y columnas
    for i in range(9):

        if not validar_fila(tablero,i):
            return False

        if not validar_columna(tablero,i):
            return False

    # validar subcuadros
    for i in range(0,9,3):
        for j in range(0,9,3):

            if not validar_subcuadro(tablero,i,j):
                return False

    return True


print(validar_sudoku(TABLERO))


# =========================================================
# PARTE 3 — CONJUNTOS CON LISTAS ENLAZADAS
# =========================================================

# nodo
class Nodo:

    def __init__(self,dato):

        self.dato = dato
        self.siguiente = None


# conjunto con lista enlazada
class Conjunto:

    def __init__(self):

        self.cabeza = None


    # -----------------------------------------------------
    # pertenece
    # busca elemento
    # -----------------------------------------------------
    def pertenece(self,x):

        actual = self.cabeza

        while actual:

            if actual.dato == x:
                return True

            actual = actual.siguiente

        return False


    # -----------------------------------------------------
    # agregar
    # agrega si no existe
    # -----------------------------------------------------
    def agregar(self,x):

        if self.pertenece(x):
            return

        nuevo = Nodo(x)

        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo


    # -----------------------------------------------------
    # mostrar
    # -----------------------------------------------------
    def mostrar(self):

        actual = self.cabeza

        while actual:

            print(actual.dato)

            actual = actual.siguiente


# =========================================================
# SUBCONJUNTO LISTA ENLAZADA
# =========================================================

def es_subconjunto(A,B):

    actual = A.cabeza

    while actual:

        # si no esta en B
        if not B.pertenece(actual.dato):
            return False

        actual = actual.siguiente

    return True


# =========================================================
# PERMISOS
# =========================================================

def tiene_permisos(usuario,requeridos):

    # requeridos ⊆ usuario
    return es_subconjunto(requeridos,usuario)


# =========================================================
# EJEMPLO 1
# =========================================================

A = Conjunto()
B = Conjunto()

A.agregar(1)
A.agregar(2)

B.agregar(1)
B.agregar(2)
B.agregar(3)

print(es_subconjunto(A,B))   # True


# =========================================================
# EJEMPLO 2
# =========================================================

usuario = Conjunto()
usuario.agregar("leer")
usuario.agregar("editar")
usuario.agregar("borrar")

requeridos = Conjunto()
requeridos.agregar("leer")
requeridos.agregar("editar")

print(tiene_permisos(usuario,requeridos))


# =========================================================
# EJEMPLO 3
# =========================================================

A = Conjunto()
B = Conjunto()

A.agregar(1)
A.agregar(5)

B.agregar(1)
B.agregar(2)
B.agregar(3)

print(es_subconjunto(A,B))   # False


# =========================================================
# TRUCOS IMPORTANTES PARCIAL
# =========================================================

# validar sudoku
set(fila) == set(range(1,10))

# subconjunto sets
A.issubset(B)

# union
A | B

# interseccion
A & B

# diferencia
A - B

# simetrica
A ^ B

# detectar repetidos
len(lista) != len(set(lista))

# subconjunto lista enlazada
es_subconjunto(A,B)

# permisos
tiene_permisos(usuario,requeridos)