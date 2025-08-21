# with recursion
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# ------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def dfs_recursive(node):
    if node is None:
        return
    # Visit the node
    print(node.data, end=' ')
    # Traverse left subtree
    dfs_recursive(node.left)
    # Traverse right subtree
    dfs_recursive(node.right)

# Example tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

dfs_recursive(root)  # Output: 1 2 4 5 3

# ------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def dfs_recursive(node):
    if node is None:
        return []
    # Combine current node + left subtree + right subtree
    return [node.data] + dfs_recursive(node.left) + dfs_recursive(node.right)

# Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = dfs_recursive(root)
print(result)  # Output: [1, 2, 4, 5, 3]

# -------------------------------

def dfs_iterative(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data, end=' ')
        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

dfs_iterative(root)  # Output: 1 2 4 5 3

# Stack mimics the call stack of recursion.
# Right child is pushed first so the left child is processed first.

# Recursive DFS is simple and elegant.
# Iterative DFS avoids recursion depth issues.
# Both can be adapted to graphs, but for graphs, you need a visited set to avoid cycles.

