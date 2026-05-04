from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    # initial state (0,0)
    queue.append((0, 0, []))

    while queue:
        x, y, path = queue.popleft()

        # If already visited, skip
        if (x, y) in visited:
            continue

        visited.add((x, y))

        # Add current state to path
        path = path + [(x, y)]

        # Check if target reached
        if x == target or y == target:
            print("Steps to reach target:")
            for step in path:
                print(step)
            return

        # Possible operations:

        # 1. Fill Jug1
        queue.append((jug1_capacity, y, path))

        # 2. Fill Jug2
        queue.append((x, jug2_capacity, path))

        # 3. Empty Jug1
        queue.append((0, y, path))

        # 4. Empty Jug2
        queue.append((x, 0, path))

        # 5. Pour Jug1 → Jug2
        transfer = min(x, jug2_capacity - y)
        queue.append((x - transfer, y + transfer, path))

        # 6. Pour Jug2 → Jug1
        transfer = min(y, jug1_capacity - x)
        queue.append((x + transfer, y - transfer, path))

    print("No solution found.")

# ----------- INPUT -----------
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

water_jug_bfs(jug1, jug2, target)
