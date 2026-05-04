class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.h = heuristic
        self.children = []   # [( (child1, child2), cost ), ...]
        self.status = False  # solved or not
        self.solution = None

def ao_star(node):
    # If already solved, return heuristic
    if node.status:
        return node.h

    print("Expanding Node:", node.name)

    min_cost = float('inf')
    best_children = None

    # Evaluate all AND/OR paths
    for group, cost in node.children:
        total_cost = cost
        for child in group:
            total_cost += ao_star(child)

        if total_cost < min_cost:
            min_cost = total_cost
            best_children = group

    node.h = min_cost
    node.solution = best_children
    node.status = True

    return node.h

def print_solution(node):
    if node.solution is None:
        return

    print(node.name, "->", [child.name for child in node.solution])
    for child in node.solution:
        print_solution(child)

# -------- GRAPH CREATION --------

# Create nodes with heuristic values
A = Node('A', 10)
B = Node('B', 6)
C = Node('C', 4)
D = Node('D', 2)
E = Node('E', 8)
F = Node('F', 5)
G = Node('G', 3)

# Define AND-OR relationships
# (children group, cost)

A.children = [
    ((B, C), 2),   # AND condition
    ((D,), 4)      # OR condition
]

B.children = [
    ((E,), 3),
    ((F,), 2)
]

C.children = [
    ((G,), 2)
]

# Leaf nodes: D, E, F, G (no children)

# -------- RUN AO* --------
ao_star(A)

print("\nOptimal Solution Graph:")
print_solution(A)
