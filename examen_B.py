"""
═══════════════════════════════════════════════════════════════════════════════
                        QUIZ 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN B
                    Sistema de Gestión de Tareas (To-Do List)
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Una startup te ha contratado para implementar un sistema de gestión de tareas.
Debes diseñar e implementar el sistema usando listas enlazadas.
Cada tarea tiene una prioridad del 1 (baja) al 5 (urgente).

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Tarea) con los atributos necesarios
2. Diseñar la clase Lista (ListaTareas) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
-------------------------------------
Diseña las clases necesarias:

a) Clase NODO (Tarea):
   - Debe almacenar: descripción, prioridad (1-5), estado (completada o no)
   - Debe poder enlazarse con otra tarea
   
b) Clase LISTA (ListaTareas):
   - Debe mantener referencia al inicio de la lista
   - Las tareas deben mantenerse ORDENADAS por prioridad (mayor primero)


PUNTO 2 (1.0): AGREGAR TAREA ORDENADA - RECURSIVO
-------------------------------------------------
Implementa un método para agregar una nueva tarea.
- La tarea debe insertarse en la posición correcta según su prioridad
- Mayor prioridad va primero
- OBLIGATORIO usar recursividad

Ejemplo:
    Si la lista tiene prioridades [5, 3, 1] y agregas prioridad 4
    Debe quedar [5, 4, 3, 1]


PUNTO 3 (0.75): CONTAR PENDIENTES - RECURSIVO
---------------------------------------------
Implementa un método que cuente las tareas NO completadas
que tengan cierta prioridad.
- OBLIGATORIO usar recursividad

Ejemplo:
    contar_pendientes(5) retorna cuántas tareas urgentes hay sin completar


PUNTO 4 (1.0): OBTENER URGENTES - RECURSIVO
-------------------------------------------
Implementa un método que retorne una NUEVA lista con las tareas
de prioridad 4 o 5 que NO estén completadas.
- OBLIGATORIO usar recursividad
- No modificar la lista original

Ejemplo:
    urgentes = lista.obtener_urgentes()
    # Nueva lista solo con tareas urgentes pendientes


PUNTO 5 (1.25): LIMPIAR COMPLETADAS - RECURSIVO
-----------------------------------------------
Implementa un método que elimine TODAS las tareas completadas.
- OBLIGATORIO usar recursividad
- Modificar la lista original

Ejemplo:
    Antes:  [✓]Tarea1 -> [○]Tarea2 -> [✓]Tarea3 -> [○]Tarea4
    Después: [○]Tarea2 -> [○]Tarea4

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 1a: Clase Nodo (Tarea)
# TODO: Diseñar e implementar


# PUNTO 1b: Clase Lista (ListaTareas)
# TODO: Diseñar e implementar con los métodos de los puntos 2-5


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# (Descomenta cuando tengas tu implementación lista)
# ═══════════════════════════════════════════════════════════════════════════════

"""
if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL SISTEMA DE TAREAS")
    print("=" * 60)
    
    # Crear lista de tareas
    mis_tareas = ListaTareas()
    
    # Agregar tareas (deben quedar ordenadas por prioridad)
    mis_tareas.agregar("Comprar leche", 2)
    mis_tareas.agregar("Estudiar para parcial", 5)
    mis_tareas.agregar("Llamar al médico", 4)
    mis_tareas.agregar("Ver serie", 1)
    mis_tareas.agregar("Entregar proyecto", 5)
    mis_tareas.agregar("Hacer ejercicio", 3)
    
    print("\\n📋 Lista de tareas (ordenada por prioridad):")
    mis_tareas.mostrar()  # Implementa este método para visualizar
    print("   Esperado orden de prioridades: 5, 5, 4, 3, 2, 1")
    
    # Contar pendientes
    print("\\n🔢 Tareas urgentes (prioridad 5):", mis_tareas.contar_pendientes(5))
    print("   Esperado: 2")
    
    # Marcar algunas como completadas (implementa un método para esto)
    # mis_tareas.completar("Comprar leche")
    # mis_tareas.completar("Ver serie")
    # mis_tareas.completar("Estudiar para parcial")
    
    # Obtener urgentes
    print("\\n🚨 Tareas urgentes pendientes:")
    urgentes = mis_tareas.obtener_urgentes()
    urgentes.mostrar()
    
    # Limpiar completadas
    print("\\n🗑️ Eliminando tareas completadas...")
    mis_tareas.limpiar_completadas()
    mis_tareas.mostrar()
"""
# PUNTO 1a: Clase Nodo (Tarea)
class Nodo:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion   # texto de la tarea
        self.prioridad = prioridad       # prioridad (1 a 5)
        self.completada = False          # estado (por defecto NO completada)
        self.siguiente = None            # referencia al siguiente nodo


# PUNTO 1b: Clase Lista (ListaTareas)
class ListaTareas:
    def __init__(self):
        self.inicio = None               # inicio de la lista


    # PUNTO 2: Agregar tarea ordenada (RECURSIVO)
    def agregar(self, descripcion, prioridad):
        nuevo = Nodo(descripcion, prioridad)         # crea nuevo nodo
        self.inicio = self._agregar_rec(self.inicio, nuevo)  # inserta recursivamente


    def _agregar_rec(self, nodo, nuevo):
        if nodo is None:              # caso base: lista vacía
            return nuevo              # el nuevo nodo será el inicio

        if nuevo.prioridad > nodo.prioridad:
            nuevo.siguiente = nodo    # el nuevo apunta al actual
            return nuevo              # el nuevo pasa a ser primero

        # si no, seguimos buscando posición
        nodo.siguiente = self._agregar_rec(nodo.siguiente, nuevo)
        return nodo                   # mantenemos el nodo actual


    # Método para mostrar la lista
    def mostrar(self):
        actual = self.inicio
        while actual:
            estado = "✓" if actual.completada else "○"  # muestra estado visual
            print(f"[{estado}] {actual.descripcion} (P{actual.prioridad})")
            actual = actual.siguiente


    # Método para marcar como completada (extra útil)
    def completar(self, descripcion):
        actual = self.inicio
        while actual:
            if actual.descripcion == descripcion:
                actual.completada = True
                return
            actual = actual.siguiente


    # PUNTO 3: Contar pendientes (RECURSIVO)
    def contar_pendientes(self, prioridad):
        return self._contar_rec(self.inicio, prioridad)


    def _contar_rec(self, nodo, prioridad):
        if nodo is None:                      # caso base
            return 0

        contar = 0
        if nodo.prioridad == prioridad and not nodo.completada:
            contar = 1                        # suma 1 si cumple condición

        return contar + self._contar_rec(nodo.siguiente, prioridad)


    # PUNTO 4: Obtener urgentes (RECURSIVO)
    def obtener_urgentes(self):
        nueva = ListaTareas()
        nueva.inicio = self._urgentes_rec(self.inicio)
        return nueva


    def _urgentes_rec(self, nodo):
        if nodo is None:
            return None

        resto = self._urgentes_rec(nodo.siguiente)

        # condición: prioridad 4 o 5 y NO completada
        if nodo.prioridad >= 4 and not nodo.completada:
            nuevo = Nodo(nodo.descripcion, nodo.prioridad)  # copia nodo
            nuevo.siguiente = resto
            return nuevo
        else:
            return resto


    # PUNTO 5: Limpiar completadas (RECURSIVO)
    def limpiar_completadas(self):
        self.inicio = self._limpiar_rec(self.inicio)


    def _limpiar_rec(self, nodo):
        if nodo is None:
            return None

        nodo.siguiente = self._limpiar_rec(nodo.siguiente)

        if nodo.completada:
            return nodo.siguiente   # elimina nodo
        else:
            return nodo             # conserva nodo