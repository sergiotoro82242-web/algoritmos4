"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 2: EVALUACIÓN DE EXPRESIONES POSTFIJAS
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════

Notación Postfija (Polaca Inversa):
- El operador va DESPUÉS de los operandos
- No necesita paréntesis ni reglas de precedencia
- Se evalúa de izquierda a derecha usando una pila

Ejemplos:
    Infija: 3 + 4        →  Postfija: 3 4 +
    Infija: 3 + 4 * 2    →  Postfija: 3 4 2 * +
    Infija: (3 + 4) * 2  →  Postfija: 3 4 + 2 *
"""

from ejemplo_01_pila import Pila


def evaluar_postfija(expresion):
    """
    Evalúa una expresión en notación postfija.
    
    Algoritmo:
    1. Recorrer tokens de izquierda a derecha
    2. Si es número → push a la pila
    3. Si es operador → pop dos operandos, operar, push resultado
    4. Al final, el resultado está en el tope
    
    Args:
        expresion: String con tokens separados por espacios
    
    Returns:
        Resultado numérico de la expresión
    """
    pila = Pila()
    tokens = expresion.split()
    
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '//': lambda a, b: a // b,
        '%': lambda a, b: a % b,
        '**': lambda a, b: a ** b,
    }
    
    print(f"\n📝 Evaluando: {expresion}")
    print("-" * 40)
    
    for token in tokens:
        if token.lstrip('-').replace('.', '').isdigit():
            # Es un número (soporta negativos y decimales)
            valor = float(token) if '.' in token else int(token)
            pila.push(valor)
            print(f"   Token '{token}' → push({valor})")
        elif token in operadores:
            # Es un operador
            b = pila.pop()  # Segundo operando (sale primero)
            a = pila.pop()  # Primer operando
            resultado = operadores[token](a, b)
            pila.push(resultado)
            print(f"   Token '{token}' → {a} {token} {b} = {resultado}")
        else:
            raise ValueError(f"Token no reconocido: {token}")
        
        print(f"            Pila: {pila}")
    
    return pila.pop()


# ═══════════════════════════════════════════════════════════════════════════════
# DEMOSTRACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("   EVALUACIÓN DE EXPRESIONES POSTFIJAS")
    print("=" * 50)
    
    # Ejemplos de expresiones
    expresiones = [
        ("3 4 +", "3 + 4"),
        ("3 4 2 * +", "3 + 4 * 2"),
        ("3 4 + 2 *", "(3 + 4) * 2"),
        ("5 1 2 + 4 * + 3 -", "5 + (1 + 2) * 4 - 3"),
        ("2 3 ** 4 +", "2 ** 3 + 4"),
        ("10 3 /", "10 / 3"),
    ]
    
    for postfija, infija in expresiones:
        resultado = evaluar_postfija(postfija)
        print(f"\n✅ Resultado: {resultado}")
        print(f"   (Equivale a: {infija} = {eval(infija)})")
        print("=" * 50)
