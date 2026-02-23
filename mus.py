"""
REPRODUCTOR DE MUSICA (PLAYLIST) CON NODOS Y LISTA CIRCULAR DOBLE
Hecho con el estilo de los ejemplos del profe (potencia / búsqueda binaria):
- Docstring claro con algoritmo
- Caso base y caso recursivo explicados
- Pruebas al final (como en el material)

Requisito: "todo lo que permita hacer sea por recursividad"
En este código, las operaciones del reproductor se hacen recursivas:
- agregar canción (al final)
- contar
- mostrar
- buscar por título
- seleccionar (usa buscar)
- siguiente / anterior (mover N pasos)
- eliminar (por título)
- reproducir actual (solo imprime, no recorre)

Nota: no reproduce audio real; solo simula el reproductor con la canción actual.
"""

# ============================================================
# 1) NODO (lista doble circular)
# ============================================================

class NodoCancion:
    """
    Nodo de una lista circular doble:
    - siguiente: apunta a la siguiente canción
    - anterior: apunta a la canción anterior
    """
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.siguiente = None
        self.anterior = None

    def etiqueta(self):
        return f"{self.titulo} - {self.artista}"


# ============================================================
# 2) PLAYLIST CIRCULAR DOBLEMENTE LIGADA (operaciones recursivas)
# ============================================================

class PlaylistCircular:
    """
    Playlist implementada como lista circular doble.
    Se mantiene:
    - cabeza: primer nodo
    - actual: canción seleccionada (la que "suena")
    """

    def __init__(self):
        self.cabeza = None
        self.actual = None

    # --------------------------------------------------------
    # 2.1) AGREGAR CANCION (recursivo)
    # --------------------------------------------------------

    def agregar(self, titulo, artista):
        """
        Agrega una canción al final de la lista.

        Algoritmo:
            1. Crear nodo nuevo
            2. Si la lista está vacía:
               - cabeza = nuevo
               - actual = nuevo
               - nuevo.siguiente = nuevo (cierra círculo)
               - nuevo.anterior = nuevo (cierra círculo)
            3. Si NO está vacía:
               - encontrar el último nodo de forma recursiva
               - enlazar el nuevo entre el último y la cabeza

        Caso base (lista vacía):
            cabeza is None

        Caso recursivo (lista con elementos):
            buscar el "último" avanzando hasta que nodo.siguiente == cabeza
        """
        nuevo = NodoCancion(titulo, artista)

        if self.cabeza is None:
            self.cabeza = nuevo
            self.actual = nuevo
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            return

        self._insertar_al_final_rec(self.cabeza, self.cabeza, nuevo)

    def _insertar_al_final_rec(self, nodo, inicio, nuevo):
        """
        Inserta el nodo 'nuevo' al final (recursivo).

        Caso base:
            nodo.siguiente == inicio
            Significa que 'nodo' es el último, porque apunta a la cabeza.

        Paso recursivo:
            avanzar a nodo.siguiente
        """
        if nodo.siguiente == inicio:
            # Enlazar: ultimo <-> nuevo <-> cabeza
            nodo.siguiente = nuevo
            nuevo.anterior = nodo

            nuevo.siguiente = inicio
            inicio.anterior = nuevo
            return

        return self._insertar_al_final_rec(nodo.siguiente, inicio, nuevo)

    # --------------------------------------------------------
    # 2.2) CONTAR (recursivo)
    # --------------------------------------------------------

    def contar(self):
        """
        Cuenta cuántas canciones hay en la playlist.

        Caso base:
            lista vacía -> 0

        Caso recursivo:
            contar desde cabeza hasta volver a cabeza
        """
        if self.cabeza is None:
            return 0
        return self._contar_rec(self.cabeza, self.cabeza, primero=True)

    def _contar_rec(self, nodo, inicio, primero):
        """
        Caso base:
            si no es la primera llamada y nodo == inicio -> dimos la vuelta -> 0

        Caso recursivo:
            1 + contar del siguiente
        """
        if (not primero) and nodo == inicio:
            return 0
        return 1 + self._contar_rec(nodo.siguiente, inicio, primero=False)

    # --------------------------------------------------------
    # 2.3) MOSTRAR PLAYLIST (recursivo)
    # --------------------------------------------------------

    def mostrar(self):
        """
        Muestra todas las canciones de la playlist.

        Caso base:
            lista vacía -> imprimir mensaje

        Caso recursivo:
            imprimir nodo y avanzar hasta volver a cabeza
        """
        if self.cabeza is None:
            print("Playlist vacía.")
            return
        self._mostrar_rec(self.cabeza, self.cabeza, primero=True)

    def _mostrar_rec(self, nodo, inicio, primero):
        """
        Caso base:
            si no es primera llamada y nodo == inicio -> parar

        Caso recursivo:
            imprimir y avanzar
        """
        if (not primero) and nodo == inicio:
            return

        marca = "  (ACTUAL)" if nodo == self.actual else ""
        print(f"- {nodo.etiqueta()}{marca}")
        return self._mostrar_rec(nodo.siguiente, inicio, primero=False)

    # --------------------------------------------------------
    # 2.4) BUSCAR POR TITULO (recursivo)
    # --------------------------------------------------------

    def buscar(self, titulo):
        """
        Busca una canción por título (ignorando mayúsculas/minúsculas).

        Returns:
            NodoCancion si la encuentra, o None si no.

        Caso base:
            lista vacía -> None
        """
        if self.cabeza is None:
            return None
        return self._buscar_rec(self.cabeza, self.cabeza, titulo, primero=True)

    def _buscar_rec(self, nodo, inicio, titulo, primero):
        """
        Caso base:
            si no es primera llamada y nodo == inicio -> no encontrado -> None

        Caso éxito:
            si nodo.titulo coincide -> nodo

        Paso recursivo:
            buscar en nodo.siguiente
        """
        if (not primero) and nodo == inicio:
            return None

        if nodo.titulo.lower() == titulo.lower():
            return nodo

        return self._buscar_rec(nodo.siguiente, inicio, titulo, primero=False)

    # --------------------------------------------------------
    # 2.5) SELECCIONAR (usa buscar recursivo)
    # --------------------------------------------------------

    def seleccionar(self, titulo):
        """
        Selecciona una canción como actual.

        Algoritmo:
            1. buscar(titulo)
            2. si existe, actual = nodo encontrado
            3. si no, no cambia

        Returns:
            True si selecciona, False si no existe
        """
        nodo = self.buscar(titulo)
        if nodo is None:
            return False
        self.actual = nodo
        return True

    # --------------------------------------------------------
    # 2.6) SIGUIENTE / ANTERIOR (mover N pasos, recursivo)
    # --------------------------------------------------------

    def siguiente(self, pasos=1):
        """
        Avanza 'pasos' canciones.

        Caso base:
            lista vacía -> no hacer nada

        Caso recursivo:
            mover pasos usando recursión
        """
        if self.cabeza is None:
            return
        self.actual = self._mover_rec(self.actual, pasos, direccion="sig")

    def anterior(self, pasos=1):
        """
        Retrocede 'pasos' canciones.
        """
        if self.cabeza is None:
            return
        self.actual = self._mover_rec(self.actual, pasos, direccion="ant")

    def _mover_rec(self, nodo, pasos, direccion):
        """
        Moverse N pasos desde un nodo.

        Caso base:
            pasos == 0 -> retornar nodo (ya se movió lo necesario)

        Paso recursivo:
            - si direccion == 'sig': ir a nodo.siguiente y pasos-1
            - si direccion == 'ant': ir a nodo.anterior y pasos-1
        """
        if pasos == 0:
            return nodo

        if direccion == "sig":
            return self._mover_rec(nodo.siguiente, pasos - 1, direccion)
        else:
            return self._mover_rec(nodo.anterior, pasos - 1, direccion)

    # --------------------------------------------------------
    # 2.7) ELIMINAR POR TITULO (recursivo)
    # --------------------------------------------------------

    def eliminar(self, titulo):
        """
        Elimina la primera canción cuyo título coincida.

        Algoritmo:
            1. Si lista vacía -> False
            2. Recorrer recursivamente hasta encontrar coincidencia
            3. Si se encuentra:
               - Si es el único nodo -> lista queda vacía
               - Si no:
                 reconectar anterior y siguiente
                 actualizar cabeza si es necesario
                 actualizar actual si es necesario

        Returns:
            True si elimina, False si no se encuentra
        """
        if self.cabeza is None:
            return False
        return self._eliminar_rec(self.cabeza, self.cabeza, titulo, primero=True)

    def _eliminar_rec(self, nodo, inicio, titulo, primero):
        """
        Caso base:
            si no es primera llamada y nodo == inicio -> dimos la vuelta -> False

        Caso éxito:
            si coincide el título -> eliminar ese nodo y retornar True

        Paso recursivo:
            avanzar al siguiente nodo
        """
        if (not primero) and nodo == inicio:
            return False

        if nodo.titulo.lower() == titulo.lower():
            return self._eliminar_nodo(nodo)

        return self._eliminar_rec(nodo.siguiente, inicio, titulo, primero=False)

    def _eliminar_nodo(self, nodo):
        """
        Elimina un nodo ya encontrado.

        Casos:
        1) Solo hay un nodo:
           nodo.siguiente == nodo y nodo.anterior == nodo
           -> cabeza = None, actual = None

        2) Hay más de uno:
           - reconectar vecinos
           - si nodo es cabeza -> mover cabeza
           - si nodo es actual -> mover actual
        """
        if nodo.siguiente == nodo and nodo.anterior == nodo:
            self.cabeza = None
            self.actual = None
            return True

        # Reconectar
        nodo.anterior.siguiente = nodo.siguiente
        nodo.siguiente.anterior = nodo.anterior

        # Si era cabeza, mover cabeza
        if nodo == self.cabeza:
            self.cabeza = nodo.siguiente

        # Si era actual, mover actual
        if nodo == self.actual:
            self.actual = nodo.siguiente

        return True

    # --------------------------------------------------------
    # 2.8) REPRODUCIR (solo imprime la actual)
    # --------------------------------------------------------

    def reproducir(self):
        """
        Imprime la canción actual.
        No recorre, por eso no necesita recursión.
        """
        if self.actual is None:
            print("Playlist vacía.")
            return
        print("Reproduciendo:", self.actual.etiqueta())


# ============================================================
# 3) MENU RECURSIVO (estilo material: se repite por recursión)
# ============================================================

def menu(playlist):
    """
    Menu recursivo.

    Caso base:
        opción 0 -> terminar (return)

    Caso recursivo:
        ejecutar acción y volver a llamar menu(playlist)
    """
    print("\n--- MENU REPRODUCTOR ---")
    print("1) Agregar canción")
    print("2) Mostrar playlist")
    print("3) Reproducir actual")
    print("4) Siguiente (N pasos)")
    print("5) Anterior (N pasos)")
    print("6) Buscar por título")
    print("7) Seleccionar por título")
    print("8) Eliminar por título")
    print("9) Contar canciones")
    print("0) Salir")

    op = input("Opción: ").strip()

    if op == "0":
        print("Saliendo...")
        return

    if op == "1":
        titulo = input("Título: ").strip()
        artista = input("Artista: ").strip()
        playlist.agregar(titulo, artista)
        print("Canción agregada.")

    elif op == "2":
        playlist.mostrar()

    elif op == "3":
        playlist.reproducir()

    elif op == "4":
        n = input("Pasos (enter=1): ").strip()
        pasos = int(n) if n else 1
        playlist.siguiente(pasos)
        playlist.reproducir()

    elif op == "5":
        n = input("Pasos (enter=1): ").strip()
        pasos = int(n) if n else 1
        playlist.anterior(pasos)
        playlist.reproducir()

    elif op == "6":
        titulo = input("Título a buscar: ").strip()
        nodo = playlist.buscar(titulo)
        if nodo:
            print("Encontrada:", nodo.etiqueta())
        else:
            print("No encontrada.")

    elif op == "7":
        titulo = input("Título a seleccionar: ").strip()
        ok = playlist.seleccionar(titulo)
        if ok:
            playlist.reproducir()
        else:
            print("No se encontró esa canción.")

    elif op == "8":
        titulo = input("Título a eliminar: ").strip()
        ok = playlist.eliminar(titulo)
        print("Eliminada." if ok else "No se encontró para eliminar.")

    elif op == "9":
        print("Total canciones:", playlist.contar())

    else:
        print("Opción inválida.")

    return menu(playlist)


# ============================================================
# 4) PRUEBAS (como en el material del profe)
# ============================================================

if __name__ == "__main__":
    p = PlaylistCircular()

    # Canciones de prueba
    p.agregar("Blinding Lights", "The Weeknd")
    p.agregar("Viva La Vida", "Coldplay")
    p.agregar("Hysteria", "Muse")

    # Mostrar estado inicial
    print("Playlist inicial:")
    p.mostrar()
    p.reproducir()

    # Pruebas rápidas tipo material
    print("\nPrueba buscar:")
    print("buscar('Hysteria') ->", "OK" if p.buscar("Hysteria") else "FAIL")
    print("buscar('NoExiste') ->", "OK" if p.buscar("NoExiste") is None else "FAIL")

    print("\nPrueba contar:")
    print("contar() ->", p.contar(), "(esperado 3)")

    print("\nPrueba siguiente/anterior:")
    p.siguiente()
    p.reproducir()
    p.anterior()
    p.reproducir()

    print("\nPrueba eliminar:")
    ok = p.eliminar("Viva La Vida")
    print("eliminar('Viva La Vida') ->", ok, "(esperado True)")
    print("contar() ->", p.contar(), "(esperado 2)")
    p.mostrar()

    # Iniciar menu interactivo
    menu(p)