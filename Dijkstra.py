# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:17:09 2024

@author: 3PW97LA_RS5
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 09:50:56 2023

@author: 3PW97LA_RS5
"""
def dijkstra(graph, inicio, fin):
    distancias = {calle: float('inf') for calle in graph}
    distancias[inicio] = 0

    nodos_no_visitados = set(graph)

    while nodos_no_visitados:
        nodo_actual = min(nodos_no_visitados, key=lambda calle: distancias[calle])
        nodos_no_visitados.remove(nodo_actual)

        for vecino, peso in graph[nodo_actual].items():
            if distancias[vecino] > distancias[nodo_actual] + peso:
                distancias[vecino] = distancias[nodo_actual] + peso

    return distancias[fin]

def obtener_ruta_mas_corta(graph, inicio, fin):
    distancias = {calle: float('inf') for calle in graph}
    distancias[inicio] = 0

    nodos_no_visitados = set(graph)
    padres = {}

    while nodos_no_visitados:
        nodo_actual = min(nodos_no_visitados, key=lambda calle: distancias[calle])
        nodos_no_visitados.remove(nodo_actual)

        for vecino, peso in graph[nodo_actual].items():
            if distancias[vecino] > distancias[nodo_actual] + peso:
                distancias[vecino] = distancias[nodo_actual] + peso
                padres[vecino] = nodo_actual

    # Reconstruir la ruta
    ruta = [fin]
    actual = fin
    while actual != inicio:
        actual = padres[actual]
        ruta.insert(0, actual)

    return ruta

# Grafo con nombres de calles y sus distancias
calles = {
    'Hidalgo': {'Morelos': 2, 'Benito Juárez': 1},
    'Morelos': {'Hidalgo': 2, 'Madero': 2, 'Emiliano Zapata': 2, 'Miguel Hidalgo': 4},
    'Benito Juárez': {'Hidalgo': 1, 'Miguel Hidalgo': 3, 'Independencia': 1},
    'Emiliano Zapata': {'Morelos': 2, 'Independencia': 3, 'Vicente Guerrero': 4},
    'Madero': {'Morelos': 4, 'Emiliano Zapata': 3, 'Lázaro Cárdenas': 4, 'Zaragoza': 7},
    'Miguel Hidalgo': {'Morelos': 3, 'Benito Juárez': 2, 'Zaragoza': 4, 'Vicente Guerrero': 7},
    'Lázaro Cárdenas': {'Madero': 7, 'Vicente Guerrero': 5, 'Zaragoza': 6},
    'Zaragoza': {'Madero': 6, 'Lázaro Cárdenas': 5, 'Independencia': 1},
    'Independencia': {'Benito Juárez': 1, 'Zaragoza': 6},
    'Vicente Guerrero': {'Emiliano Zapata': 4, 'Lázaro Cárdenas': 5, 'Zaragoza': 21746}
}

inicio_calle = 'Hidalgo'
fin_calle = 'Vicente Guerrero'

distancia_mas_corta = dijkstra(calles, inicio_calle, fin_calle)
ruta_mas_corta = obtener_ruta_mas_corta(calles, inicio_calle, fin_calle)

print(f"La longitud de la ruta más corta desde '{inicio_calle}' hasta '{fin_calle}' es: {distancia_mas_corta}")
print(f"La ruta más corta es pasar por las calles: {', '.join(ruta_mas_corta)}")
