#mixto_parcial 

"""
=================================================
EJERCICIOS MIXTOS TIPO PARCIAL
Regex + conjuntos + recursividad + listas
=================================================
"""

import re


# ============================================
# EJERCICIO 1
# validar usuario y guardar en conjunto
# ============================================

regex = r'^[a-zA-Z]\w{4,}$'

usuarios = set()

for u in ["juan1","ana","Pedro_22"]:
    if re.match(regex,u):
        usuarios.add(u)

print("Usuarios validos:",usuarios)


# ============================================
# EJERCICIO 2
# contar repetidos con conjuntos
# ============================================

lista = [1,2,2,3,4,4,5]

repetidos = len(lista) - len(set(lista))

print("Repetidos:",repetidos)


# ============================================
# EJERCICIO 3
# recursividad suma
# ============================================

def suma(n):
    if n==0:
        return 0
    return n + suma(n-1)

print("Suma:",suma(5))


# ============================================
# EJERCICIO 4
# regex extraer numeros
# ============================================

texto = "precio 200 cantidad 3"

nums = re.findall(r"\d+",texto)

print(nums)


# ============================================
# EJERCICIO 5
# subset + conjuntos
# ============================================

def subset(nums,target,i=0):
    if target==0:
        return True
    
    if i>=len(nums):
        return False
    
    return subset(nums,target-nums[i],i+1) or subset(nums,target,i+1)

print(subset([3,5,7],10))

# Definir un patrón regex como variable
patron_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"

# Usar el patrón para validar un correo
texto = "contacto@ejemplo.com"
if re.match(patron_email, texto):
    print("Correo válido")
else:
    print("Correo inválido")