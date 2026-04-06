#recursividad_memorizacion

"""
===========================================
RECURSIVIDAD + MEMOIZACION
===========================================
Guardar resultados para no recalcular
"""

memo = {}

# ============================================
# EJERCICIO 1: fibonacci memo
# ============================================

def fib(n):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print("Fib:", fib(10))


# ============================================
# EJERCICIO 2: factorial memo
# ============================================

memo2 = {}

def fact(n):
    if n in memo2:
        return memo2[n]
    
    if n == 0:
        return 1
    
    memo2[n] = n * fact(n-1)
    return memo2[n]

print("Fact:", fact(5))


# ============================================
# EJERCICIO 3: suma hasta n
# ============================================

def suma(n):
    if n == 0:
        return 0
    
    return n + suma(n-1)

print("Suma:", suma(5))


# ============================================
# EJERCICIO 4: potencia
# ============================================

def potencia(a,b):
    if b == 0:
        return 1
    
    return a * potencia(a,b-1)

print("Potencia:", potencia(2,5))


# ============================================
# EJERCICIO 5: contar caminos
# ============================================

memo3 = {}

def caminos(n):
    if n in memo3:
        return memo3[n]
    
    if n <= 1:
        return 1
    
    memo3[n] = caminos(n-1) + caminos(n-2)
    return memo3[n]

print("Caminos:", caminos(5))


# ============================================
# EJERCICIO 6: suma lista recursiva
# ============================================

def suma_lista(lista, i=0):
    if i == len(lista):
        return 0
    
    return lista[i] + suma_lista(lista,i+1)

print("Suma lista:", suma_lista([1,2,3,4]))


# ============================================
# EJERCICIO 7: máximo lista
# ============================================

def max_lista(lista,i=0):
    if i == len(lista)-1:
        return lista[i]
    
    return max(lista[i], max_lista(lista,i+1))

print("Max lista:", max_lista([1,5,2,9,3]))


# ============================================
# EJERCICIO 8: subset sum
# ============================================

def subset(nums, target, i=0):
    if target == 0:
        return True
    
    if i >= len(nums):
        return False
    
    return (subset(nums,target-nums[i],i+1) or
            subset(nums,target,i+1))

print("Subset:", subset([2,4,6],8))