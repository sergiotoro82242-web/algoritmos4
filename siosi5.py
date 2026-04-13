"""
PARCIAL 1
Validar que cada fila del horario tenga materias únicas
y validar permisos con listas enlazadas
"""

MATERIAS = {"MAT","FIS","QUI"}

HORARIO = [
["MAT","FIS","QUI"],
["FIS","QUI","MAT"],
["QUI","MAT","FIS"]
]


# PUNTO 1 validar fila
def validar_fila(tabla, fila):
    # obtener fila
    datos = tabla[fila]

    # convertir a set y comparar
    return set(datos) == MATERIAS


# PUNTO 2 validar columna
def validar_columna(tabla, col):

    columna = []

    # recorrer filas
    for fila in tabla:
        columna.append(fila[col])

    # validar
    return set(columna) == MATERIAS



# LISTAS ENLAZADAS
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self,elementos=None):
        self.cabeza=None
        if elementos:
            for e in elementos:
                self.agregar(e)

    def pertenece(self,x):
        actual=self.cabeza
        while actual:
            if actual.dato==x:
                return True
            actual=actual.siguiente
        return False

    def agregar(self,x):
        if self.pertenece(x):
            return
        nuevo=Nodo(x)
        nuevo.siguiente=self.cabeza
        self.cabeza=nuevo


# subconjunto
def es_subconjunto(A,B):

    actual=A.cabeza

    while actual:

        if not B.pertenece(actual.dato):
            return False

        actual=actual.siguiente

    return True



"""
PARCIAL 2
Validar que cada fila tenga numeros 1..4 sin repetir
"""

VALIDOS={1,2,3,4}

TABLA=[
[1,2,3,4],
[2,3,4,1],
[3,4,1,2],
[4,1,2,3]
]


def validar_fila(tabla,fila):

    datos=tabla[fila]

    return set(datos)==VALIDOS


def validar_columna(tabla,col):

    columna=[]

    for fila in tabla:
        columna.append(fila[col])

    return set(columna)==VALIDOS


def validar_bloque(tabla,fi,ci):

    elementos=[]

    for i in range(fi,fi+2):
        for j in range(ci,ci+2):

            elementos.append(tabla[i][j])

    return set(elementos)==VALIDOS


"""
PARCIAL 3
Validar que cada rol tenga permisos únicos
"""

PERMISOS={"leer","editar","borrar"}

roles=[
["leer","editar","borrar"],
["editar","borrar","leer"],
["borrar","leer","editar"]
]


def validar_roles(roles):

    for rol in roles:

        if set(rol)!=PERMISOS:
            return False

    return True

"""
PARCIAL 4
Validar matriz letras A B C
"""

VALIDOS={"A","B","C"}

TABLA=[
["A","B","C"],
["B","C","A"],
["C","A","B"]
]


def validar_filas(tabla):

    for fila in tabla:

        if set(fila)!=VALIDOS:
            return False

    return True


def validar_columnas(tabla):

    for col in range(3):

        columna=[]

        for fila in range(3):
            columna.append(tabla[fila][col])

        if set(columna)!=VALIDOS:
            return False

    return True

"""
PARCIAL 5 COMPLETO
Validar filas + columnas + permisos
"""

VALIDOS={1,2,3}

TABLA=[
[1,2,3],
[2,3,1],
[3,1,2]
]


def validar_fila(tabla,fila):

    datos=tabla[fila]

    return set(datos)==VALIDOS


def validar_columna(tabla,col):

    columna=[]

    for fila in tabla:
        columna.append(tabla[fila][col])

    return set(columna)==VALIDOS


# listas enlazadas
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None


class Conjunto:

    def __init__(self,elementos=None):
        self.cabeza=None
        if elementos:
            for e in elementos:
                self.agregar(e)

    def pertenece(self,x):

        actual=self.cabeza

        while actual:
            if actual.dato==x:
                return True
            actual=actual.siguiente

        return False


    def agregar(self,x):

        if self.pertenece(x):
            return

        nuevo=Nodo(x)
        nuevo.siguiente=self.cabeza
        self.cabeza=nuevo


def es_subconjunto(A,B):

    actual=A.cabeza

    while actual:

        if not B.pertenece(actual.dato):
            return False

        actual=actual.siguiente

    return True


def tiene_permisos(usuario,requeridos):

    return es_subconjunto(requeridos,usuario)