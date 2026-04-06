#conj_clase
"""
                           CONJUNTOS
grupo de elementos -> sin orden, no hay duplicados, deben ser distinguibles
conjunto: A = {1, 2, 3, 4, 5}
cardinalidad: |A| = 5
conjunto vacío: conjunto sin elementos -> A = {}
conjunto unitario: conjunto con un solo elemento -> A = {1}
un conjunto pertenece ∈ o no pertenece  ∉: A = {1, 2, 3} -> 1 ∈ A, 4 ∉ A
En python: in, not in
Union: A ∪ B = {1, 2, 3} ∪ {3, 4, 5} = {1, 2, 3, 4, 5} En python: A|B o A.union(B)
Intersección: A ∩ B = {1, 2, 3} ∩ {3, 4, 5} = {3} En python: A&B o A.intersection(B)
Diferencia: A - B = {1, 2, 3} - {3, 4, 5} = {1, 2} ---A-B != B-A---  En python: A-B o A.difference(B) 
Diferencia simétrica: A Δ B = (A - B) ∪ (B - A) = {1, 2, 4, 5} En python: A^B o A.symmetric_difference(B)


                         SUBCONJUNTOS
Subconjunto propio: A ⊂ B -> A = {1, 2} ⊂ B = {1, 2, 3}
igualdad de conjuntos: A = B -> A = {1, 2, 3} = B = {1, 2, 3}
conjuntos disjuntos: A ∩ B = {} -> A = {1, 2} y B = {3, 4} son disjuntos porque no tienen elementos en común

"""

lista = [5, 5, 5, 5, 2, 4, 5, 3, 6, 7, 2, 1, 5, 3, 9, 0, 1, 0, 2, 5, 7, 6]
conjunto = set(lista) #Elimina los elementos duplicados y no tiene un orden específico
conjunto = list(set(lista)) #Convertir la lista en conjunto y el conjunto en lista
print(conjunto) #Imprime el conjunto resultante, que contiene los elementos únicos de la lista
print(len(conjunto)) #Imprime la cantidad de elementos únicos en el conjunto





"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 1: SPOTIFY - PLAYLISTS COMPARTIDAS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Spotify quiere implementar una función de "Playlists Compartidas".
Dados dos usuarios con sus canciones favoritas, el sistema debe:

1. Encontrar canciones que ambos disfrutan (para playlist compartida)
2. Sugerir canciones que uno tiene y el otro no
3. Mostrar el catálogo combinado de ambos
4. Verificar si un usuario escucha un subconjunto de lo que escucha otro

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

canciones_juan = {
    "Blinding Lights", "Bohemian Rhapsody", "Shape of You",
    "Despacito", "Hotel California", "Billie Jean",
    "Rolling in the Deep", "Smells Like Teen Spirit"
}

canciones_maria = {
    "Shape of You", "Despacito", "Bad Guy",
    "Blinding Lights", "Watermelon Sugar", "Levitating",
    "Rolling in the Deep", "drivers license"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   SPOTIFY - PLAYLISTS COMPARTIDAS")
print("=" * 60)

print(f"\nCanciones de Juan ({len(canciones_juan)}):")
for c in sorted(canciones_juan):
    print(f"  ♪ {c}")

print(f"\nCanciones de María ({len(canciones_maria)}):")
for c in sorted(canciones_maria):
    print(f"  ♪ {c}")

# 1. Playlist compartida (intersección)
compartidas = canciones_juan & canciones_maria
print(f"\n1. Playlist compartida ({len(compartidas)} canciones):")
for c in sorted(compartidas):
    print(f"  ♪ {c}")

# 2. Sugerencias (diferencia)
sugerencias_para_juan = canciones_maria - canciones_juan
sugerencias_para_maria = canciones_juan - canciones_maria

print(f"\n2. Sugerencias para Juan ({len(sugerencias_para_juan)}):")
for c in sorted(sugerencias_para_juan):
    print(f"  → {c}")

print(f"\n   Sugerencias para María ({len(sugerencias_para_maria)}):")
for c in sorted(sugerencias_para_maria):
    print(f"  → {c}")

# 3. Catálogo combinado (unión)
catalogo = canciones_juan | canciones_maria
print(f"\n3. Catálogo combinado ({len(catalogo)} canciones únicas):")
for c in sorted(catalogo):
    print(f"  ♪ {c}")

# 4. ¿Un usuario escucha subconjunto del otro?
print(f"\n4. ¿Juan escucha subconjunto de María? {canciones_juan <= canciones_maria}")
print(f"   ¿María escucha subconjunto de Juan? {canciones_maria <= canciones_juan}")

# Bonus: Canciones exclusivas (diferencia simétrica)
exclusivas = canciones_juan ^ canciones_maria
print(f"\n5. Canciones que solo uno de los dos escucha ({len(exclusivas)}):")
for c in sorted(exclusivas):
    print(f"  ♪ {c}")






algoritmos = {
    "Ana", "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel","Helena", "Ivan"
}

bases_de_datos = {
    "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel","Helena", "Ivan", "Jorge"
}
redes = {
    "Diana", "Eduardo", "Fernanda",
    "Gabriel","Helena", "Ivan", "Jorge", "Karla"
}
estudian_todas = algoritmos & bases_de_datos & redes #Intersección de los conjuntos
estudian_algoritmos = algoritmos - (bases_de_datos | redes) #Diferencia de algoritmos con la unión de bases de datos y redes
estudian_algoritmos_redes = (algoritmos & redes) - bases_de_datos #Intersección de algoritmos y redes menos la intersección de algoritmos y bases de datos
estudian_algoritmos_o_redes = algoritmos | redes #Unión de algoritmos y redes
estudian_algoritmos_no_redes = algoritmos - redes #Diferencia de algoritmos con redes
solo_algoritmos = algoritmos - bases_de_datos - redes #Diferencia de algoritmos con la unión de bases de datos y redes
solo_bases_de_datos = bases_de_datos - algoritmos - redes #Diferencia de bases de datos con la unión de algoritmos y redes
solo_redes = redes - algoritmos - bases_de_datos #Diferencia de redes con la unión de algoritmos y bases de datos
solo_una_materia = solo_algoritmos | solo_bases_de_datos | solo_redes #Unión de los tres conjuntos menos la intersección de los tres conjuntos
print(len(solo_una_materia))

reporte = {}
todos = algoritmos | bases_de_datos | redes
for estudiante in todos:
    materias = []
    if estudiante in algoritmos:
        materias.append("Algoritmos")
    if estudiante in bases_de_datos:
        materias.append("Bases de Datos")
    if estudiante in redes:
        materias.append("Redes")
    reporte[estudiante] = materias
print(reporte)




"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 2: UNIVERSIDAD - CRUCE DE HORARIOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
La universidad necesita un sistema para analizar la matrícula de estudiantes.
Dados los estudiantes inscritos en diferentes materias, el sistema debe:

1. Encontrar estudiantes que cursan ambas materias (para evitar cruces)
2. Encontrar estudiantes que solo cursan una materia
3. Total de estudiantes únicos entre todas las materias
4. Verificar si todos los de una materia están en otra
5. Encontrar estudiantes que cursan las 3 materias

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

algoritmos = {
    "Ana", "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel", "Helena", "Ivan"
}

bases_datos = {
    "Carlos", "Diana", "Juan", "Karen",
    "Gabriel", "Luis", "Maria"
}

redes = {
    "Diana", "Eduardo", "Gabriel", "Karen",
    "Natalia", "Oscar", "Ivan"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   UNIVERSIDAD - CRUCE DE HORARIOS")
print("=" * 60)

print(f"\nAlgoritmos ({len(algoritmos)}): {sorted(algoritmos)}")
print(f"Bases de Datos ({len(bases_datos)}): {sorted(bases_datos)}")
print(f"Redes ({len(redes)}): {sorted(redes)}")

# 1. Estudiantes en Algoritmos Y Bases de Datos (posible cruce)
cruce_alg_bd = algoritmos & bases_datos
print(f"\n1. Cursan Algoritmos Y Bases de Datos: {sorted(cruce_alg_bd)}")

cruce_alg_redes = algoritmos & redes
print(f"   Cursan Algoritmos Y Redes: {sorted(cruce_alg_redes)}")

cruce_bd_redes = bases_datos & redes
print(f"   Cursan Bases de Datos Y Redes: {sorted(cruce_bd_redes)}")

# 2. Estudiantes que SOLO cursan una materia
solo_algoritmos = algoritmos - bases_datos - redes
solo_bd = bases_datos - algoritmos - redes
solo_redes = redes - algoritmos - bases_datos

print(f"\n2. Solo Algoritmos: {sorted(solo_algoritmos)}")
print(f"   Solo Bases de Datos: {sorted(solo_bd)}")
print(f"   Solo Redes: {sorted(solo_redes)}")

# 3. Total de estudiantes únicos
todos = algoritmos | bases_datos | redes
print(f"\n3. Total estudiantes únicos: {len(todos)}")
print(f"   Estudiantes: {sorted(todos)}")

# 4. ¿Todos los de Algoritmos están en Bases de Datos?
print(f"\n4. ¿Algoritmos ⊆ Bases de Datos? {algoritmos <= bases_datos}")
print(f"   ¿Cruce Alg-BD ⊆ Algoritmos? {cruce_alg_bd <= algoritmos}")

# 5. Estudiantes en las 3 materias
en_las_tres = algoritmos & bases_datos & redes
print(f"\n5. Cursan las 3 materias: {sorted(en_las_tres)}")

# Bonus: Resumen por estudiante
print("\n" + "=" * 60)
print("RESUMEN POR ESTUDIANTE")
print("=" * 60)
for estudiante in sorted(todos):
    materias = []
    if estudiante in algoritmos:
        materias.append("Algoritmos")
    if estudiante in bases_datos:
        materias.append("BD")
    if estudiante in redes:
        materias.append("Redes")
    print(f"  {estudiante}: {', '.join(materias)} ({len(materias)} materias)")








catalogo = {
    "Inception": {"ciencia ficción", "acción", "thriller", "drama"},
    "The Matrix": {"ciencia ficción", "acción", "thriller"},
    "Titanic": {"drama", "romance", "histórica"},
    "The Notebook": {"romance", "drama"},
    "Avengers": {"acción", "ciencia ficción", "aventura"},
    "John Wick": {"acción", "thriller", "crimen"},
    "Interstellar": {"ciencia ficción", "drama", "aventura"},
    "The Godfather": {"crimen", "drama", "thriller"},
    "Toy Story": {"animación", "comedia", "aventura"},
    "Shrek": {"animación", "comedia", "aventura"},
}
peliculas = set(catalogo.keys())
peliculas_comunes = []
for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        generos_comunes = catalogo[p1] & catalogo[p2] #Intersección de los géneros de las dos películas
        if len(generos_comunes) >= 2: #Si tienen al menos 2 géneros en común
            peliculas_comunes.append((p1, p2, generos_comunes)) #Añadir la tupla (película 1, película 2, géneros comunes) a la lista de películas comunes
print(peliculas_comunes)


favoritos_mios = {"acción","thriller","aventura"}
recomendaciones = []
for pelicula, generos in catalogo.items():
    coincidencias = favoritos_mios & generos #Intersección de los géneros favoritos con los géneros de la película
    if coincidencias:
        porcentaje = round(len(coincidencias) / len(favoritos_mios) * 100, 2)#Calcular el porcentaje de coincidencias
        recomendaciones.append((pelicula, porcentaje)) #Añadir la tupla (película, porcentaje) a la lista de recomendaciones
recomendaciones.sort(key=lambda x: x[1], reverse=True) #Ordenar las recomendaciones por porcentaje de coincidencias de mayor a menor
print(recomendaciones)