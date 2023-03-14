# Una clase para representar un objeto graph
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # agrega bordes al graph no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Función para realizar un recorrido DFS en el graph en un graph
def DFS(graph, v, discovered):
 
    discovered[v] = True            # marca el nodo actual como descubierto
    print(v, end=' ')               # imprime el nodo actual
 
    # do para cada arista (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:       # si `u` aún no se descubre
            DFS(graph, u, discovered)
 
 
if __name__ == '__main__':
 
    # Lista de bordes de graph según el diagrama anterior
    edges = [
        # Observe que el nodo 0 está desconectado
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
 
    # número total de nodos en el graph (etiquetados de 0 a 12)
    n = 13
 
    # construye un graph a partir de los bordes dados
    graph = Graph(edges, n)
 
    # para realizar un seguimiento de si se descubre un vértice o no
    discovered = [False] * n
 
    # Realizar recorrido DFS de todos los nodos no descubiertos a
    # cubre todos los componentes conectados de un graph
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)