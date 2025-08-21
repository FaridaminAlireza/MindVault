def bellman_ford(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
    
    # Check negative cycles
    for node in graph:
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                return "Graph contains negative weight cycle"
    
    return dist

graph_neg = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', -3), ('D', 2)],
    'C': [('D', 3)],
    'D': []
}
print(bellman_ford(graph_neg, 'A'))  # {'A': 0, 'B': 4, 'C': 1, 'D': 4}


# Bellman-Ford Algorithm (weighted graphs with negative edges) Approach:

# Computes shortest path from a single source.
# Can handle negative weights, detects negative cycles.
# Time Complexity: O(V * E)