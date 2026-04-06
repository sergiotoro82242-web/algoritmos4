#un poco de todo 2
import re

# =========================================================
# 🧠 PARCIAL TIPO EXAMEN (CON PREGUNTAS + SOLUCIONES)
# =========================================================


# =========================================================
# 🔹 1. REGEX (NIVEL PARCIAL)
# =========================================================

# ❓ EJERCICIO 1:
# Crear una regex que valide un usuario con:
# - Empieza con letra
# - Puede tener números
# - Puede tener "_" pero no dos seguidos
# - Mínimo 5 caracteres
# - No puede terminar en "_"

regex_user = r'^[a-zA-Z](?!.*__)[a-zA-Z0-9_]{3,}[a-zA-Z0-9]$'

usuarios = ["juan_1", "ana__", "1pedro", "juan_", "maria123"]

print("\n--- REGEX USUARIO ---")
for u in usuarios:
    print(u, "✔" if re.match(regex_user, u) else "✘")


# ---------------------------------------------------------

# ❓ EJERCICIO 2:
# Extraer TODOS los números de un texto

texto = "Compra 3 libros por 200 y 2 cuadernos por 50"

numeros = re.findall(r"\d+", texto)

print("\n--- NÚMEROS ---")
print(numeros)


# ---------------------------------------------------------

# ❓ EJERCICIO 3:
# Validar contraseña:
# - mínimo 8 caracteres
# - al menos 1 número
# - al menos 1 mayúscula

regex_pass = r'^(?=.*\d)(?=.*[A-Z]).{8,}$'

print("\n--- PASSWORD ---")
print("Segura:", "✔" if re.match(regex_pass, "Hola1234") else "✘")


# =========================================================
# 🔹 2. LISTAS ENLAZADAS + RECURSIVIDAD
# =========================================================

# ❓ EJERCICIO 4:
# Crear una función recursiva que cuente los nodos

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None


# lista: 5 -> 10 -> 15
n1 = Nodo(5)
n2 = Nodo(10)
n3 = Nodo(15)

n1.sig = n2
n2.sig = n3


def contar(nodo):
    # caso base
    if nodo is None:
        return 0
    # caso recursivo
    return 1 + contar(nodo.sig)


print("\n--- CONTAR NODOS ---")
print(contar(n1))


# ---------------------------------------------------------

# ❓ EJERCICIO 5:
# Encontrar el valor máximo en la lista enlazada

def maximo(nodo):
    if nodo is None:
        return float("-inf")

    if nodo.sig is None:
        return nodo.valor

    return max(nodo.valor, maximo(nodo.sig))


print("\n--- MÁXIMO ---")
print(maximo(n1))


# ---------------------------------------------------------

# ❓ EJERCICIO 6:
# Eliminar un valor X de la lista (recursivo)

def eliminar(nodo, x):
    if nodo is None:
        return None

    if nodo.valor == x:
        return nodo.sig  # salta el nodo

    nodo.sig = eliminar(nodo.sig, x)
    return nodo


print("\n--- ELIMINAR 10 ---")
nueva = eliminar(n1, 10)

def imprimir(nodo):
    if nodo is None:
        return
    print(nodo.valor)
    imprimir(nodo.sig)

imprimir(nueva)


# =========================================================
# 🔹 3. CONJUNTOS
# =========================================================

# ❓ EJERCICIO 7:
# Dadas dos listas, devolver elementos en común SIN repetidos

a = [1, 2, 2, 3]
b = [2, 3, 4]

inter = list(set(a) & set(b))

print("\n--- INTERSECCIÓN ---")
print(inter)


# ---------------------------------------------------------

# ❓ EJERCICIO 8:
# Ver si una lista tiene duplicados

def tiene_duplicados(lista):
    return len(lista) != len(set(lista))


print("\n--- DUPLICADOS ---")
print(tiene_duplicados([1, 2, 3, 2]))


# =========================================================
# 🔹 4. RECURSIVIDAD CON MEMORIZACIÓN
# =========================================================

# ❓ EJERCICIO 9:
# Fibonacci con memo

memo = {}

def fib(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


print("\n--- FIB ---")
print(fib(10))


# ---------------------------------------------------------

# ❓ EJERCICIO 10:
# Problema de monedas:
# ¿Cuántas formas hay de sumar "target" usando monedas?

memo2 = {}

def monedas(coins, target):
    if target == 0:
        return 1
    if target < 0:
        return 0

    if target in memo2:
        return memo2[target]

    total = 0
    for c in coins:
        total += monedas(coins, target - c)

    memo2[target] = total
    return total


print("\n--- MONEDAS ---")
print(monedas([1, 2], 4))


# =========================================================
# 🔥 EJERCICIO FINAL (TIPO PARCIAL DURO)
# =========================================================

# ❓ Dado:
# - una lista de números
# - un target
# Determinar si existe un subconjunto que sume exactamente el target

memo3 = {}

def subset(nums, target, i=0):
    if (i, target) in memo3:
        return memo3[(i, target)]

    if target == 0:
        return True
    if i >= len(nums):
        return False

    res = (subset(nums, target - nums[i], i + 1) or
           subset(nums, target, i + 1))

    memo3[(i, target)] = res
    return res


print("\n--- SUBSET ---")
print(subset([2, 4, 6], 8))


# =========================================================
# 🎯 CONSEJO FINAL DE EXAMEN
# =========================================================

# Si ves:
# - "validar formato" → REGEX
# - "estructura con nodos" → LISTA ENLAZADA
# - "sin repetir" → SET
# - "muchas llamadas repetidas" → MEMORIZACIÓN