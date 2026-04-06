#listas enlazadas 

"""
=================================================
LISTAS ENLAZADAS + RECURSIVIDAD
=================================================
- Cada nodo apunta al siguiente
- No se usan listas de Python []
- Todo se recorre con referencias
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None


# crear lista: 5 -> 10 -> 15
n1 = Nodo(5)
n2 = Nodo(10)
n3 = Nodo(15)

n1.sig = n2
n2.sig = n3


# ============================================
# EJERCICIO 1: contar nodos (recursivo)
# ============================================

def contar(nodo):
    if nodo is None:
        return 0
    
    return 1 + contar(nodo.sig)

print("Contar:", contar(n1))


# ============================================
# EJERCICIO 2: suma total
# ============================================

def suma(nodo):
    if nodo is None:
        return 0
    
    return nodo.valor + suma(nodo.sig)

print("Suma:", suma(n1))


# ============================================
# EJERCICIO 3: máximo
# ============================================

def maximo(nodo):
    if nodo.sig is None:
        return nodo.valor
    
    return max(nodo.valor, maximo(nodo.sig))

print("Max:", maximo(n1))


# ============================================
# EJERCICIO 4: mínimo
# ============================================

def minimo(nodo):
    if nodo.sig is None:
        return nodo.valor
    
    return min(nodo.valor, minimo(nodo.sig))

print("Min:", minimo(n1))


# ============================================
# EJERCICIO 5: buscar valor
# ============================================

def buscar(nodo, x):
    if nodo is None:
        return False
    
    if nodo.valor == x:
        return True
    
    return buscar(nodo.sig, x)

print("Buscar 10:", buscar(n1,10))


# ============================================
# EJERCICIO 6: eliminar valor
# ============================================

def eliminar(nodo, x):
    if nodo is None:
        return None
    
    if nodo.valor == x:
        return nodo.sig
    
    nodo.sig = eliminar(nodo.sig, x)
    return nodo

nueva = eliminar(n1,10)


# ============================================
# EJERCICIO 7: imprimir
# ============================================

def imprimir(nodo):
    if nodo is None:
        return
    
    print(nodo.valor)
    imprimir(nodo.sig)

print("Lista:")
imprimir(nueva)


# ============================================
# EJERCICIO 8: invertir lista
# ============================================

def invertir(nodo, prev=None):
    if nodo is None:
        return prev
    
    siguiente = nodo.sig
    nodo.sig = prev
    
    return invertir(siguiente, nodo)

invertida = invertir(nueva)

print("Invertida:")
imprimir(invertida)