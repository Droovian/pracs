from collections import deque

def dfs(graph, start):
    visited = set()
    stack = deque([start])

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            print(vertex, end="")
            visited.add(vertex)

            for neigbour in reversed(graph[vertex]):
                if neigbour not in visited:
                    stack.append(neigbour)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

print("DFS starting from vertex A")
dfs(graph, 'A')
