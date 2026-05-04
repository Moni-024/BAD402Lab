import heapq

# A* Algorithm
def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        # Goal reached
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            print("Optimal Path:", path)
            return

        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            new_cost = g_cost[current_node] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current_node

    print("No path found")

# -------- GRAPH --------
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# -------- HEURISTIC --------
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# -------- RUN --------
start = 'A'
goal = 'F'

a_star(graph, start, goal, heuristic)
