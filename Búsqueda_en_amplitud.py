graph = {'A': ['B', 'C'],
         'B': ['D'],
         'C': ['D'],
         'D': []}

from queue import Queue

def shortest_path(graph, start, end):
    visited = set()
    queue = Queue()
    queue.put((start, [start]))
    
    while not queue.empty():
        (current_node, path) = queue.get()
        if current_node == end:
            return path
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.put((neighbor, path + [neighbor]))

path = shortest_path(graph, 'A', 'D')
print(path)

