from collections import deque

#BFS Approach
def flood_fill(grid, i, j, target, replacement):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != target:
        return
    grid[i][j] = replacement
    flood_fill(grid, i+1, j, target, replacement)
    flood_fill(grid, i-1, j, target, replacement)
    flood_fill(grid, i, j+1, target, replacement)
    flood_fill(grid, i, j-1, target, replacement)

#DFS Approach
def flood_fill(image, sr, sc, new_color):
    rows, cols = len(image), len(image[0])
    target_color = image[sr][sc]
    if target_color == new_color:
        return image
    
    queue = deque([(sr, sc)])
    while queue:
        r, c = queue.popleft()
        if (0 <= r < rows and 0 <= c < cols and image[r][c] == target_color):
            image[r][c] = new_color
            queue.extend([(r+1, c), (r-1, c), (r, c+1), (r, c-1)])
    return image

# Applications:
# Paint programs (bucket fill).
# Maze solving (finding connected regions).
# Connected component labeling in images.
# Game development (filling territories, map exploration).
# Graph traversal problems in grids.


# Time Complexity: For DFS and BFS: 𝑂(𝑁×𝑀)

# In the worst case, the algorithm might need to visit every cell in the grid once.
# Each visit does O(1) work (checking color, updating, enqueuing neighbors).
# So overall: linear in the number of cells.

# Space Complexity

# DFS (recursive): Uses the call stack. Worst-case depth = size of connected region.
# So worst case = 𝑂(𝑁×𝑀) stack frames (if the entire grid is one connected region).
#In practice, this can cause a stack overflow on large images.

#DFS (iterative with stack): Same asymptotic space O(N×M), but avoids recursion limit.

# BFS (queue):Stores frontier (neighbors to explore).
#Worst case: queue might contain almost all cells at once (e.g., if everything is connected).
# O(N×M) space in the worst case.

# 1 flood fill