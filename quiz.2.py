# =========================================================
# 1. VARIABLES (CAJAS QUE GUARDAN DATOS)
# =========================================================

nombre = "Juan"     # texto
edad = 20           # entero
altura = 1.75       # decimal
activo = True       # booleano

print(nombre)
print(edad)


# =========================================================
# 2. LISTAS
# =========================================================

# lista = varios elementos
numeros = [1,2,3,4]

# acceder a posición
print(numeros[0])  # 1

# agregar elemento
numeros.append(5)

print(numeros)


# =========================================================
# 3. BUCLE FOR
# =========================================================

# recorre elementos
for num in numeros:
    print(num)


# =========================================================
# 4. BUCLE WHILE
# =========================================================

i = 0

while i < 3:
    print(i)
    i += 1


# =========================================================
# 5. CONDICIONALES
# =========================================================

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")


# =========================================================
# 6. FUNCIONES
# =========================================================

def sumar(a,b):
    return a + b

print(sumar(2,3))


# =========================================================
# 7. RANGE()
# =========================================================

# range(fin)
for i in range(5):
    print(i)   # 0 1 2 3 4


# range(inicio, fin)
for i in range(2,6):
    print(i)   # 2 3 4 5


# range(inicio, fin, salto)
for i in range(0,10,2):
    print(i)   # 0 2 4 6 8


# recorrer lista con range
lista = [10,20,30]

for i in range(len(lista)):
    print(lista[i])


# =========================================================
# 8. CONJUNTOS (SET)
# =========================================================

A = {1,2,3,4}
B = {3,4,5,6}


# UNION
print(A | B)   # {1,2,3,4,5,6}

# INTERSECCION
print(A & B)   # {3,4}

# DIFERENCIA
print(A - B)   # {1,2}

# DIFERENCIA INVERSA
print(B - A)   # {5,6}

# DIFERENCIA SIMETRICA
print(A ^ B)   # {1,2,5,6}


# =========================================================
# 9. LISTA → SET (ELIMINAR REPETIDOS)
# =========================================================

lista = [1,2,2,3,3,4]

print(set(lista))   # {1,2,3,4}


# =========================================================
# 10. DETECTAR REPETIDOS
# =========================================================

def tiene_repetidos(lista):
    return len(lista) != len(set(lista))

print(tiene_repetidos([1,2,3,3]))


# =========================================================
# 11. SUBCONJUNTOS
# =========================================================

A = {1,2}
B = {1,2,3}

print(A.issubset(B))  # True


# =========================================================
# 12. VALIDAR LISTA 1-9
# =========================================================

def validar_lista(lista):
    return set(lista) == set(range(1,10))

print(validar_lista([1,2,3,4,5,6,7,8,9]))


# =========================================================
# 13. SUDOKU
# =========================================================

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


# =========================================================
# VALIDAR FILAS
# =========================================================

def validar_filas(tablero):

    correcto = set(range(1,10))

    for fila in tablero:
        if set(fila) != correcto:
            return False

    return True


# =========================================================
# VALIDAR COLUMNAS
# =========================================================

def validar_columnas(tablero):

    correcto = set(range(1,10))

    for col in range(9):

        columna = []

        for fila in range(9):
            columna.append(tablero[fila][col])

        if set(columna) != correcto:
            return False

    return True


# =========================================================
# VALIDAR SUBCUADROS
# =========================================================

def validar_subcuadros(tablero):

    correcto = set(range(1,10))

    for fila in range(0,9,3):
        for col in range(0,9,3):

            bloque = []

            for i in range(fila,fila+3):
                for j in range(col,col+3):
                    bloque.append(tablero[i][j])

            if set(bloque) != correcto:
                return False

    return True


# =========================================================
# VALIDAR TODO
# =========================================================

def validar_sudoku(tablero):

    return (
        validar_filas(tablero)
        and validar_columnas(tablero)
        and validar_subcuadros(tablero)
    )


print(validar_sudoku(TABLERO))


# =========================================================
# TRUCOS IMPORTANTES PARA EL PARCIAL
# =========================================================

# generar 1..9
set(range(1,10))

# eliminar repetidos
set(lista)

# detectar repetidos
len(lista) != len(set(lista))

# subconjunto
A.issubset(B)

# union
A | B

# interseccion
A & B

# diferencia
A - B

# diferencia simetrica
A ^ B

# recorrer sudoku columnas
tablero[fila][col]

# recorrer subcuadros
for fila in range(0,9,3):
    for col in range(0,9,3):
        pass