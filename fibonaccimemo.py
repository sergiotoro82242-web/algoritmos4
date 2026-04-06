 
def fibonacci_memo(n,cache={}):
    if n<=1:
        return n
    if n in cache:
        return cacache[n]

    cache[n] = fibonacci_memo(n-1,cache) + fibonachi_memo(n-2,cache)
    return cache[n]

def cambio(cantidad,monedas):
    if cantidad==0:
        return 0
    if cantidad < 0:
        return float('inf')
    minimo =float('inf')

for monedas in monedas:
    resultado=cambio(cantidad-moneda,monedas)
    minimo= min(resultado+1, minimo)

    return minimo
monedas=[1,5,10,25]
print(cambia(50,monedas))

def cambiomemo(cantidad,monedas,memo={}):
    if cantidad is memo:
        return memo(cantidad)
    if cantidad==0:
        return 0
    if cantidad < 0:
        return float('inf')

    minimo= float('inf')
    for moneda in monedas:
        resultado=cambiomemo(cantidad -moneda,monedas, memo)
        min=min(minimo,resultado+1)
    memo[cantidad] = minimo
    return minimo

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None
        self.tamanio = 0

    def esta_vacio(self):
        return self.tope is None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamanio += 1
    
    def pop(self):
        if self.esta_vacio():
            raise Exception("error, la pila está vacía.")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return dato
    
    def peek(self):
        if self.esta_vacio():
            raise Exception("error, la pila está vacía.")
        dato = self.tope.dato
        return dato
    
    def evaluar_postf ija(self, n):
        if tope == None:
            return "No hay valores en la pila"
        if 
        


    