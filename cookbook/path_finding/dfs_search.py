def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    if start == target:
        return True
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
print(dfs(graph, 'A', 'E'))  # True



# Approach:
# Explores as far as possible along one branch before backtracking.
# Not guaranteed to find the shortest path.

# Time Complexity: O(V + E) for graph with V vertices and E edges.
