"""
Ejercicio: Fibonacci Recursivo
"""

def fibonacci(n):
    # Caso base
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Caso recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)


# ===== EJEMPLO DIRECTO =====

n = 7
resultado = fibonacci(n)
print("fibonacci(", n, ") =", resultado)