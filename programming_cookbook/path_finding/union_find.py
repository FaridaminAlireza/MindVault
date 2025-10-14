# Union-Find: also called Disjoint Set Union, or DSU 
# is the key to writing an efficient Kruskal’s Algorithm
# and to mastering many graph and network algorithms.
# Union-Find is a data structure that keeps track 
# of a collection of disjoint (non-overlapping) sets.
#  Allowed operations: 
#  1. Find which set an element belongs to
#  2. Union two sets

# Union–Find is faster than set as
# it doesn’t actually store all the elements in nested sets.
# Instead, it only stores:
    # A parent pointer for each element.
    # (Optionally) a small rank or size for balancing.
# That means:
# 1. find(x) just follows parent links — 
# often only 1–2 hops (thanks to path compression).
# 2. union(x, y) just changes one pointer — O(1) time.


# Initialization 
def make_set(n):
    # Each node is its own parent at the start
    parent = [i for i in range(n)]
    rank = [0] * n  # Used to keep trees balanced
    return parent, rank

def find(x, parent):
    # Recursively find root with path compression
    if parent[x] != x:
        parent[x] = find(parent[x], parent)  # path compression
    return parent[x]

def union(x, y, parent, rank):
    root_x = find(x, parent)
    root_y = find(y, parent)

    if root_x == root_y:
        return False  # cycle

    # Union by rank: attach smaller tree under larger one
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

    return True
