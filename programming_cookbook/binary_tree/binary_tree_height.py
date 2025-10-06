class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1  # or return 0 if you define empty tree height as 0
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)

# Example
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)

print(height(root))  # Output: 2
