# A spanning tree of a connected undirected graph is a subgraph that:
    # 1. Includes all the vertices of the original graph.
    # 2. Is connected (there is a path between any two vertices).
    # 3. Contains no cycles (it’s a tree).
# Essentially, it’s a tree that spans all vertices of the graph.
# A spanning tree connects all nodes with the minimum number of edges, 
# which is  V−1 for V vertices.

# Applications of Spanning Tree:
    # In Computer Networks:
        # Spanning Tree Protocol (STP) prevents loops in Ethernet networks.
        # Ensures a loop-free topology while allowing redundancy.
     # In Electrical Networks:
        # Designing circuits or power grids to 
        #  connect all nodes with minimal wiring cost.
    # Transportation Networks:
        # Road, railway, or pipeline networks to minimize construction costs
        #  while connecting all locations.
    # Clustering and Data Analysis:
        # Used in hierarchical clustering algorithms in machine learning.
    # Approximation Algorithms:
        # Basis for solving problems like the traveling salesman problem
        #  (TSP) approximately.

# Every connected graph has at least one spanning tree, and if weights are unique,
# the MST is unique. Spanning trees are foundational in networks, optimization,
# and algorithm design.


# Kruskal’s Algorithm: 
# Add edges in increasing weight order while avoiding cycles.
# Steps:
# 1. Sort all edges by weight.
# 2. Initialize each vertex as a separate set (Union-Find).
# 3. Add the smallest edge if it connects two different sets.
# 4. Repeat until  V−1 edges are added.

# Key Rule:
# If an edge connects vertices from different sets → include it and merge the sets.
# If an edge connects vertices in the same set → skip it (would form a cycle).


# Complexity: O(ElogE)

# This is a greedy algorithm as it makes a locally optimal choice at each step,
# hoping that these choices lead to a globally optimal solution.
# In Kruskal’s Algorithm, the greedy choice is:
# “At each step, choose the smallest-weight edge that doesn’t form a cycle.”
# This local decision — picking the lightest available edge — leads to
# a Minimum Spanning Tree (MST) because it keeps costs as low as 
# possible at each step and avoids cycles to maintain a valid tree.


# without using Union-Find method
def MST (adj):
    
    # node nums
    node_nums = len(adj[0])

    #Initialize sets
    disjoint_sets = dict()
    for i in range(node_nums):
        disjoint_sets[i] = {i}

    def find_node(node_i):
        for k,v in disjoint_sets.items():
            if node_i in v:
                return k
        return -1

    # Sort edges
    edge_list = []
    at_least_one_edge = False
    for node_i in range(node_nums):
        for node_j in range(node_i + 1, node_nums):
            if adj[node_i][node_j] != 0:
                at_least_one_edge = True
                edge_list.append((node_i, node_j, adj[node_i][node_j]))

    if not at_least_one_edge:
        return []
    edge_list.sort(key= lambda x: x[2])
    
    mst = []
    mst_nodes = set()
    while (edge_list):
        node_i, node_j, edge_weight = edge_list.pop(0)

        # find if node_i belongs to any set
        node_i_repr = find_node(node_i)
        # find if node_j belongs any set 
        node_j_repr = find_node(node_j)

        if node_i_repr == node_j_repr and node_i_repr != -1: 
            # makes cycle
            continue
        elif node_i_repr == -1 and node_j_repr >=0:
            disjoint_sets[node_j_repr].add(node_i)
            mst_nodes.update({node_i})
        elif node_i_repr >= 0 and node_j_repr == -1:
            disjoint_sets[node_i_repr].add(node_j)
            mst_nodes.update({node_j})
        elif node_i_repr >= 0 and node_j_repr >= 0:
            disjoint_sets[node_j_repr] = (
                disjoint_sets[node_j_repr] | disjoint_sets[node_i_repr])
            disjoint_sets.pop(node_i_repr)
            mst_nodes.update({node_i, node_j})
    
        mst.append((node_i, node_j, edge_weight))
        if len(mst_nodes) == node_nums:
            # all the nodes are covered
            break

    return mst

adj = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
print(MST(adj))


# using Union-Find (Disjoint Set)
class DisjointSet:
    def __init__(self, vertices):
        # Initialize
        self.parent = {v: v for v in vertices}
        # use rank to optimize unions
        self.rank = {v: 0 for v in vertices}

    def find(self, node):
        # Path compression: make representative the parent directly
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        # Union by rank: attach smaller tree under larger tree
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False  # would form cycle
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True

def kruskal(vertices, edges):
    """
    vertices: list of nodes, e.g. ['A','B','C','D']
    edges: list of tuples (weight, u, v)
    """
    # Sort edges by weight
    edges.sort()
    
    ds = DisjointSet(vertices)
    mst = [] 
    total_weight = 0

    for weight, u, v in edges:
        if ds.union(u, v):  # if no cycle
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


vertices = ['A', 'B', 'C', 'D']
edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (2, 'B', 'C'),
    (4, 'C', 'D')
]

mst, total_weight = kruskal(vertices, edges)
print("Edges in MST:", mst)
print("Total weight:", total_weight)
