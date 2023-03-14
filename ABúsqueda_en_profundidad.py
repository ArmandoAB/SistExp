def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (node, path) = stack.pop()
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in maze[node]:
                stack.append((neighbor, path + [neighbor]))
    return None

maze = {(0, 0): [(1, 0)], (1, 0): [(0, 0), (1, 1)], (1, 1): [(1, 0)]}
path = dfs(maze, (0, 0), (1, 1))
print(path)

