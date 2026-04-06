#conj_list_class

# Conjuntos con Listas Enlazadas o simplemente ligadas 
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamano = 0

        if elementos:
            for elemento in elementos:
                self.agregar(elemento)

    def esta_vacio(self):
        return self.cabeza is None
    
    #Tamaño del conjunto
    def cardinalidad(self):
        return self.tamano
    
    #Buscar elemento en un conjunto
    #Recorre la lista nodo por nodo, si alguno de los nodos es el elemento buscado, devuelve True. 
    #Si llega al final de la lista sin encontrar el elemento, devuelve False.
    def pertenece(self, elemento):
        actual = self.cabeza
        while actual:
            if actual.dato == elemento:
                return True
            actual = actual.siguiente
        return False
    
    #Agregar elemento a un conjunto
    #Primero verifica si el elemento ya pertenece al conjunto utilizando el método pertenece. 
    # Si el elemento ya está presente, no se agrega y se devuelve False.
    def agregar(self, elemento):
        if self.pertenece(elemento):
            return False        
        nuevo = Nodo(elemento)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1
        return True
    
    #Eliminar elemento de un conjunto
    #Primero verifica si el conjunto está vacío. Si lo está, no se puede eliminar ningún elemento y se devuelve False.
    #Luego, verifica si el elemento a eliminar es el primer nodo (cabeza). Si es así, actualiza la cabeza para que apunte al siguiente nodo y disminuye el tamaño del conjunto.
    #Si el elemento no es la cabeza, recorre la lista buscando el nodo que contiene el elemento a eliminar. Si lo encuentra, actualiza el enlace del nodo anterior para saltar el nodo a eliminar y disminuye el tamaño del conjunto. Si no encuentra el elemento, devuelve False.
    def eliminar(self, elemento):
        if self.esta_vacio():
            return False
        if self.cabeza.dato == elemento:
            self.cabeza = self.cabeza.siguiente
            self.tamano -= 1
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == elemento:
                actual.siguiente = actual.siguiente.siguiente
                self.tamano -= 1
                return True
            actual = actual.siguiente
            return False
        
    #Unión de conjuntos
    #Crea un nuevo conjunto resultado. Luego, recorre ambos conjuntos (self y otro) y agrega cada elemento al conjunto resultado utilizando el método agregar. Finalmente, devuelve el conjunto resultado que contiene la unión de los dos conjuntos.
    def union(self, otro):
        #Crea un nuevo conjunto resultado. 
        resultado = Conjunto()

        #Recorre el primer conjunto (self) y agrega cada elemento al conjunto resultado utilizando el método agregar.
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        #Recorre el otro conjunto y agrega cada elemento al conjunto resultado utilizando el método agregar.
        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    #Intersección de conjuntos
    #Crea un nuevo conjunto resultado. Luego, recorre el primer conjunto (self) y verifica si cada elemento pertenece al otro conjunto utilizando el método pertenece. 
    #Si un elemento pertenece a ambos conjuntos, se agrega al conjunto resultado utilizando el método agregar. 
    #Finalmente, devuelve el conjunto resultado que contiene la intersección de los dos conjuntos.
    def interseccion(self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    #Diferencia de conjuntos
    def diferencia(self, otro):
        #Crear un nuevo conjunto resultado.
        resultado = Conjunto()
        #Recorrer el primer conjunto (self) y verificar si cada elemento no pertenece al otro conjunto utilizando el método pertenece.
        actual = self.cabeza
        #Si un elemento no pertenece al otro conjunto, se agrega al conjunto resultado utilizando el método agregar.
        while actual:
            #Si no pertenece al otro conjunto, se agrega al resultado utilizando el método agregar.
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    #Diferencia simétrica de conjuntos
    def diferencia_simetrica(self, otro):
        #Hacemos la unión de la diferencia de mi conjunto con el otro y 
        #la diferencia del otro conjunto con el mío, es decir, los elementos que están en uno de los conjuntos pero no en ambos.
        return self.union(otro).union(otro.diferencia(self))
    
    #Convertir el conjunto a una lista
    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado    
    
    #Representación del conjunto como cadena
    def __str__(self):
        return "{" + ", ".join(str(x) for x in self.a_lista()) + "}"
    

    
    """
                                  ACTIVIDAD
    Enunciado:
    Una empresa necesita un sistema de control de acceso basado en los roles.
    Cada rol tiene un conjunto de permisos. El sistema debe:
    1.Verificar si un usuario puede realizar una acción
    2.Encontrar permisos comunes entre roles
    3.Encontrar permisos exclusivos de un rol
    4.Verificar si un rol es "superior" a otro (tiene todos sus permiso)
    5.Crear un nuevo rol combinando permisos de otros.

    Implementar usando operaciones de conjuntos.

    """

    #Datos
    roles = {
        "admin" :{
            "leer", "escribir", "eliminar", "crear usuarios",
            "ver_logs", "configurar", "backup", "restaurar"
        },
        "editor":{"leer", "escribir", "subir_archivos"},
        "viewer":{"leer"},
        "moderator":{"leer","escribir", "eliminar", "ver_logs"},
        "auditor":{"leer", "ver_logs", "exportar_reportes"},
    }
    usuarios = {
        "Juan": "admin",
        "Maria": "editor",
        "Pedro": "viewer",
        "Ana": "moderator",
        "Carlos": "auditor"
    }

    #1.Verificar si un usuario puede realizar una acción
    def verificar_accion(usuario, accion):
        rol = Conjunto.roles.get(Conjunto.usuarios.get(usuario))
        if rol and accion in rol:
            return True
        return False
    
    #2.Encontrar permisos comunes entre roles
    def permisos_comunes(rol1, rol2):
        return Conjunto.roles.get(rol1, set()) & Conjunto.roles.get(rol2, set()) #Intersección de los permisos de ambos roles

    #3.Encontrar permisos exclusivos de un rol
    def permisos_exclusivos(rol):
        return Conjunto.roles.get(rol, set()) - set().union(*Conjunto.roles.values()) #Diferencia de los permisos del rol con la unión de los permisos de todos los roles
    # 4. ¿Un rol es "superior" a otro?
    print("\n" + "=" * 60)
    print("4. JERARQUÍA DE ROLES")
    print("=" * 60)

    for r1 in roles:
        for r2 in roles:
            if r1 != r2 and roles[r2] < roles[r1]:
                print(f"  {r1} contiene todos los permisos de {r2}")

    # 5. Crear nuevo rol combinando otros
    print("\n" + "=" * 60)
    print("5. CREAR ROL COMBINADO")
    print("=" * 60)

    nuevo_rol = roles["editor"] | roles["auditor"]
    print(f"  editor + auditor = {sorted(nuevo_rol)}")

    # Verificar que no tenga permisos peligrosos
    permisos_peligrosos = {"eliminar", "crear_usuarios", "configurar"}
    conflictos = nuevo_rol & permisos_peligrosos
    if conflictos:
        print(f"  Alerta: tiene permisos peligrosos: {conflictos}")
    else:
        print(f"  Sin permisos peligrosos")

    #Tarea: Validar si un conjunto es subconjunto de otro
    def es_subconjunto(conjunto1, conjunto2):
        return conjunto1.issubset(conjunto2) #Verificar si conjunto1 es subconjunto de conjunto2 utilizando el método issubset de los conjuntos de Python
    
    #Tarea: implementar con listas