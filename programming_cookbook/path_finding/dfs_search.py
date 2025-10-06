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

# Time Complexity:
#  O(V + E) for graph with V vertices and E edges.

#  DFS visits each vertex at most once but it also needs to explore every edge connected
#  to those vertices. That’s why it’s not just O(V).

# Each vertex is visited exactly once by the DFS procedure.
# This gives a base cost of O(V).

# For every vertex, DFS looks at all adjacent edges in its adjacency list.
# In an adjacency list representation the total number of adjacency entries across
# all vertices equals E (each edge appears once for directed graphs, 
# or twice for undirected graphs). Therefore, across the entire traversal,
# DFS will check each edge once (directed) or twice (undirected).

# Combining Both: T(V,E)=O(V)+O(E)=O(V+E)


