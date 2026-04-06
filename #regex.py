#regex
import re

# =========================================================
# ARCHIVO 1: EXPRESIONES REGULARES (REGEX)
# =========================================================
# re = librería de Python para trabajar con regex
# se importa porque permite:
# re.match()
# re.search()
# re.findall()
# re.sub()

# =========================================================
# EJERCICIO 1
# Validar usuario
# - empieza con letra
# - números permitidos
# - guion bajo permitido
# - mínimo 5 caracteres
# =========================================================

regex = r'^[a-zA-Z][a-zA-Z0-9_]{4,}$'

# ^ = inicio cadena
# [a-zA-Z] = una letra obligatoria
# [a-zA-Z0-9_] = letras números o _
# {4,} = mínimo 4 repeticiones
# $ = final cadena

usuario = input("Ingrese usuario: ")

if re.match(regex, usuario):
    print("Usuario válido")
else:
    print("Usuario inválido")


# =========================================================
# EJERCICIO 2
# extraer números
# =========================================================

texto = "Tengo 3 perros y 20 gatos"

numeros = re.findall(r'\d+', texto)

# \d = dígito
# + = uno o más

print(numeros)


# =========================================================
# EJERCICIO 3
# validar email simple
# =========================================================

regex_email = r'^[a-zA-Z0-9._]+@[a-z]+\.[a-z]+$'

correo = input("Ingrese correo: ")

if re.match(regex_email, correo):
    print("Correo válido")
else:
    print("Correo inválido")


# =========================================================
# EJERCICIO 4
# validar contraseña
# mínimo 8
# una mayúscula
# un número
# =========================================================

regex_pass = r'^(?=.*[A-Z])(?=.*\d).{8,}$'

# (?=.*[A-Z]) = al menos una mayúscula
# (?=.*\d) = al menos un número
# .{8,} = mínimo 8 caracteres

password = input("Ingrese password: ")

print("Segura" if re.match(regex_pass, password) else "Débil")


# =========================================================
# EJERCICIO 5
# extraer palabras
# =========================================================

texto = "hola mundo python regex"

palabras = re.findall(r'\w+', texto)

# \w = letras y números

print(palabras)


# =========================================================
# EJERCICIO 6
# validar número decimal
# =========================================================

regex_decimal = r'^\d+(\.\d+)?$'

numero = input("Ingrese número: ")

if re.match(regex_decimal, numero):
    print("decimal válido")


# =========================================================
# EJERCICIO 7
# eliminar espacios múltiples
# =========================================================

texto = "hola    mundo    python"

nuevo = re.sub(r'\s+', ' ', texto)

# \s = espacio
# + = muchos

print(nuevo)


# =========================================================
# EJERCICIO 8
# validar placa ABC-123
# =========================================================

regex_placa = r'^[A-Z]{3}-\d{3}$'

placa = input("Ingrese placa: ")

print("correcta" if re.match(regex_placa, placa) else "incorrecta")