from collections import deque

def bfs(graph, start, target):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print(bfs(graph, 'A', 'E'))  # True




# Approach:
# Explores all neighbors at the current depth before going deeper.
# Guaranteed to find shortest path in unweighted graphs.

# Time Complexity: O(V + E)

