import heapq

def a_star(graph, start, goal, h):
    open_set = []
    heapq.heappush(open_set, (h(start, goal), start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor, weight in graph[current]:
            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    return None

def heuristic(node, goal):
    return 0  # for simple Dijkstra-like behavior


graph_w = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print(a_star(graph_w, 'A', 'D', heuristic))  # ['A', 'B', 'C', 'D']


# A Algorithm* (Heuristic search) Approach: 
# Similar to Dijkstra but uses heuristic h(n) to guide search toward target.
# Finds shortest path efficiently if heuristic is admissible 
# (never overestimates).

# Time Complexity:
# O(E) worst case (same as Dijkstra)
# Often faster in practice due to heuristic

