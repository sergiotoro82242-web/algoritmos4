#CONJUNTOS

"""
===========================================
CONJUNTOS (SET)
===========================================
- No repiten elementos
- Operaciones matemáticas
"""

# ============================================
# EJERCICIO 1: unión
# ============================================

a = {1,2,3}
b = {3,4,5}

print("Union:", a | b)


# ============================================
# EJERCICIO 2: intersección
# ============================================

print("Interseccion:", a & b)


# ============================================
# EJERCICIO 3: diferencia
# ============================================

print("Diferencia:", a - b)


# ============================================
# EJERCICIO 4: subconjunto
# ============================================

A = {1,2}
B = {1,2,3}

print("Subconjunto:", A.issubset(B))


# ============================================
# EJERCICIO 5: eliminar duplicados
# ============================================

lista = [1,2,2,3,4,4]

sin_dup = list(set(lista))

print("Sin duplicados:", sin_dup)


# ============================================
# EJERCICIO 6: elementos comunes
# ============================================

a = [1,2,3]
b = [2,3,4]

print("Comunes:", set(a) & set(b))


# ============================================
# EJERCICIO 7: verificar duplicados
# ============================================

def tiene_dup(lista):
    return len(lista) != len(set(lista))

print("Duplicados:", tiene_dup([1,2,3,2]))


# ============================================
# EJERCICIO 8: diferencia simétrica
# ============================================

a = {1,2,3}
b = {3,4,5}

print("Dif simetrica:", a ^ b)