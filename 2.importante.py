# =========================================================
# EJERCICIO 1
# PROBLEMA:
# Validar que una fila tenga numeros del 1 al 5 sin repetir
# =========================================================

NUM_VALIDOS = {1,2,3,4,5}   # conjunto esperado

def validar_fila(fila):

    # convertir lista a conjunto
    # comparar con conjunto valido
    return set(fila) == NUM_VALIDOS


print(validar_fila([1,2,3,4,5]))



# =========================================================
# EJERCICIO 2
# PROBLEMA:
# Validar columnas de matriz 3x3
# =========================================================

VALIDOS = {1,2,3}

matriz = [
[1,2,3],
[2,3,1],
[3,1,2]
]

def validar_columna(matriz, col):

    columna = []  # guardar columna

    # recorrer filas
    for fila in matriz:

        # tomar elemento columna
        columna.append(fila[col])

    # validar sin repetidos
    return set(columna) == VALIDOS


print(validar_columna(matriz,0))



# =========================================================
# EJERCICIO 3
# PROBLEMA:
# Validar bloque 2x2 dentro matriz
# =========================================================

def validar_bloque(matriz, fila_inicio, col_inicio):

    elementos = []   # guardar elementos

    # recorrer bloque
    for i in range(fila_inicio, fila_inicio+2):
        for j in range(col_inicio, col_inicio+2):

            elementos.append(matriz[i][j])

    # validar bloque
    return set(elementos) == {1,2,3,4}



# =========================================================
# EJERCICIO 4
# PROBLEMA:
# Validar filas letras A B C
# =========================================================

tabla = [
["A","B","C"],
["B","C","A"],
["C","A","B"]
]

VALIDOS = {"A","B","C"}

def validar_filas(tabla):

    # recorrer filas
    for fila in tabla:

        # validar fila
        if set(fila) != VALIDOS:
            return False

    return True


print(validar_filas(tabla))



# =========================================================
# EJERCICIO 5
# PROBLEMA:
# Validar columnas letras
# =========================================================

def validar_columnas(tabla):

    for col in range(3):

        columna = []

        # recorrer filas
        for fila in range(3):

            columna.append(tabla[fila][col])

        # validar columna
        if set(columna) != VALIDOS:
            return False

    return True


print(validar_columnas(tabla))



# =========================================================
# EJERCICIO 6
# PROBLEMA:
# Validar matriz completa
# =========================================================

def validar_tabla(tabla):

    # validar filas
    if not validar_filas(tabla):
        return False

    # validar columnas
    if not validar_columnas(tabla):
        return False

    return True


print(validar_tabla(tabla))



# =========================================================
# EJERCICIO 7
# PROBLEMA:
# Validar bloques 2x2
# =========================================================

matriz4 = [
[1,2,3,4],
[3,4,1,2],
[2,1,4,3],
[4,3,2,1]
]

def validar_bloques(tabla):

    VALIDOS = {1,2,3,4}

    # recorrer bloques
    for fila in range(0,4,2):
        for col in range(0,4,2):

            bloque = []

            for i in range(fila,fila+2):
                for j in range(col,col+2):

                    bloque.append(tabla[i][j])

            if set(bloque) != VALIDOS:
                return False

    return True


print(validar_bloques(matriz4))



# =========================================================
# PARTE 2 — LISTAS ENLAZADAS
# =========================================================

# nodo
class Nodo:

    def __init__(self,dato):

        self.dato = dato
        self.siguiente = None


# conjunto lista enlazada
class Conjunto:

    def __init__(self):

        self.cabeza = None


    # buscar elemento
    def pertenece(self,x):

        actual = self.cabeza

        # recorrer lista
        while actual:

            if actual.dato == x:
                return True

            actual = actual.siguiente

        return False


    # agregar sin repetir
    def agregar(self,x):

        # si existe no agregar
        if self.pertenece(x):
            return

        nuevo = Nodo(x)

        # insertar inicio
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo



# =========================================================
# EJERCICIO 8
# PROBLEMA:
# verificar subconjunto
# =========================================================

def es_subconjunto(A,B):

    actual = A.cabeza

    # recorrer A
    while actual:

        # si elemento no esta en B
        if not B.pertenece(actual.dato):
            return False

        actual = actual.siguiente

    return True



# =========================================================
# EJERCICIO 9
# PROBLEMA:
# union listas enlazadas
# =========================================================

def union(A,B):

    resultado = Conjunto()

    actual = A.cabeza

    # copiar A
    while actual:

        resultado.agregar(actual.dato)
        actual = actual.siguiente

    actual = B.cabeza

    # copiar B
    while actual:

        resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado



# =========================================================
# EJERCICIO 10
# PROBLEMA:
# interseccion listas enlazadas
# =========================================================

def interseccion(A,B):

    resultado = Conjunto()

    actual = A.cabeza

    while actual:

        # si esta en ambos
        if B.pertenece(actual.dato):

            resultado.agregar(actual.dato)

        actual = actual.siguiente

    return resultado



# =========================================================
# EJERCICIO 11
# PROBLEMA:
# diferencia listas enlazadas
# =========================================================

def diferencia(A,B):

    resultado = Conjunto()

    actual = A.cabeza

    while actual:

        # si no esta en B
        if not B.pertenece(actual.dato):

            resultado.agregar(actual.dato)

        actual = actual.siguiente

    return resultado



# =========================================================
# EJERCICIO 12
# PROBLEMA:
# permisos usuario
# =========================================================

def tiene_permisos(usuario,requeridos):

    # requeridos ⊆ usuario
    return es_subconjunto(requeridos,usuario)



# =========================================================
# EJEMPLO FINAL
# =========================================================

usuario = Conjunto()
usuario.agregar("leer")
usuario.agregar("editar")
usuario.agregar("borrar")

requeridos = Conjunto()
requeridos.agregar("leer")
requeridos.agregar("editar")

print(tiene_permisos(usuario,requeridos))