import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, node = heapq.heappop(heap)
        for neighbor, weight in graph[node]:
            if current_dist + weight < dist[neighbor]:
                dist[neighbor] = current_dist + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))
    return dist

graph_w = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
print(dijkstra(graph_w, 'A'))  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}


# Dijkstra’s Algorithm (for weighted graphs) Approach:

# Finds shortest path from a source node to all nodes.
# Uses a priority queue (min-heap).

# Time Complexity: O((V + E) log V) using min-heap