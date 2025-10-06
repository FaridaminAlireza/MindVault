# In a tree: The number of edges E = V - 1 
# (since trees are acyclic and connected).

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

inorder(root)  # 5 10 15

# v2
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)



def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

preorder(root)  # 10 5 15

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

postorder(root)  # 5 15 10



#Recursive Approach
def search_bst(node, key):
    if node is None:
        return False

    if node.value == key:
        return True
    elif key < node.value:
        return search_bst(node.left, key)   # search left subtree
    else:
        return search_bst(node.right, key)  # search right subtree

root = Node(10)
root.left = Node(5)
root.right = Node(15)

print(search_bst(root, 15))  # True
print(search_bst(root, 7))   # False


#Iterative Approach
def search_iterative(root, x):
    current = root
    while current:
        if current.val == x:
            return True
        elif x < current.val:
            current = current.left
        else:
            current = current.right
    return False



# Time Complexity:
# In the worst case, you may have to visit every node to find the target: O(n)
# Best case: O(1) (if the element is at the root)
# Average case: O(n) (no ordering guarantees)

# Space Complexity:
# This depends on how you traverse it:
# Recursive DFS: Uses call stack. O(h), where h is the height of the tree. 
# Worst case (skewed tree): O(n)
# Best case (balanced tree): O(logn)
# Iterative: O(1), it is Loop-based, more memory-efficient.



class BST:
    def __init__(self):
        self.root = None

    # Insert a value into BST
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    # Search for a value
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    # Delete a value from BST
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node found
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Node with two children → get inorder successor
            successor = self._min_value_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Inorder Traversal
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)


# ✅ Example Usage
bst = BST()
for v in [10, 5, 15, 2, 7, 12, 20]:
    bst.insert(v)

print("Inorder: ", end="")
bst.inorder()  # 2 5 7 10 12 15 20

print("Search 7:", bst.search(7))   # True
print("Search 99:", bst.search(99)) # False

bst.delete(10)  # delete root
print("After deleting 10: ", end="")
bst.inorder()   # 2 5 7 12 15 20




