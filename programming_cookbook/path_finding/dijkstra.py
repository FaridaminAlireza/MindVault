# Dijkstra’s algorithm is a graph search algorithm used to find the shortest path
# from a starting node (source) to all other nodes in a weighted graph 
# with non-negative edge weights.
# It is widely used in routing, network optimization, and GPS navigation systems.

# Approach:
# 1. Initialize:
#    - Set the distance to the source node as 0.
#    - Set the distance to all other nodes as infinity (∞).
#    - Use a priority queue (min-heap) to always select the next node with the smallest known distance.
# 2. Step 2:
#    - For the current node, examine all its neighbors.
#    - If the distance to a neighbor through the current node is smaller than the previously known distance,
#      update the distance.
# 3. Repeat until all nodes have been visited or the priority queue is empty.


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


# The importance of using priority queue:
# - The heapq (priority queue) ensures that we always process the next node 
#   with the smallest current distance. Without a heap, selecting the smallest distance
#   node each time would take O(V) time per iteration.
# - With a heap, this selection becomes O(log V), significantly improving efficiency.


# Complexity Analysis:
# Let:
# V = number of vertices
# E = number of edges

# Using a binary heap (heapq):
# Insertion into heap: O(log V)
# Extract-min operation: O(log V)
# Each edge is relaxed once.

# Overall time complexity: O((V + E) * log V)
# If implemented with an adjacency matrix (without heap): O(V²)

# Space complexity: O(V + E)


# Example Explanation:

# Consider a graph:
# A --1--> B --2--> C
# A --4--> C

# Source = A

# Step 1: Initialize
# dist[A]=0, dist[B]=∞, dist[C]=∞

# Step 2: Start with A (smallest distance)
# - Visit B: dist[B] = 0 + 1 = 1
# - Visit C: dist[C] = 0 + 4 = 4

# Step 3: Next node = B (distance 1)
# - Visit C via B: dist[C] = min(4, 1 + 2) = 3

# Step 4: Done. Final distances:
# A: 0, B: 1, C: 3
