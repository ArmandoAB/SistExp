import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}
        
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight
        
def A_star(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        (cost, current_node, path) = heapq.heappop(queue)
        if current_node == end:
            return path + [current_node]
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.edges[current_node]:
                if neighbor not in visited:
                    total_cost = graph.weights[(current_node, neighbor)] + cost
                    heuristic_cost = heuristic(neighbor, end)
                    priority = total_cost + heuristic_cost
                    heapq.heappush(queue, (priority, neighbor, path + [current_node]))
                    
def heuristic(node, goal):
    # Distancia en línea recta entre dos puntos
    x1, y1 = node
    x2, y2 = goal
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

g = Graph()
g.add_edge((1, 1), (1, 2), 1)
g.add_edge((1, 2), (2, 2), 2)
g.add_edge((2, 2), (3, 3), 3)
g.add_edge((1, 1), (2, 2), 2)
g.add_edge((2, 2), (1, 1), 2)
g.add_edge((3, 3), (4, 4), 4)
g.add_edge((4, 4), (4, 5), 2)
g.add_edge((4, 5), (5, 5), 1)
g.add_edge((5, 5), (6, 6), 3)
path = A_star(g, (1, 1), (3, 3))
print(path)

