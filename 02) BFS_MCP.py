import heapq

# Check if state is valid
def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

# Heuristic: remaining people on left side
def heuristic(state):
    m_left, c_left, boat = state
    return m_left + c_left

def best_first_search():
    start = (3, 3, 0)   # (M_left, C_left, Boat_left=0)
    goal = (0, 0, 1)

    visited = set()
    pq = []

    # push (heuristic, state, path)
    heapq.heappush(pq, (heuristic(start), start, [start]))

    while pq:
        h, current, path = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            print("Solution Path:")
            for step in path:
                print(step)
            return

        m_left, c_left, boat = current
        m_right = 3 - m_left
        c_right = 3 - c_left

        # Possible moves
        moves = [
            (1, 0), (2, 0),   # missionaries
            (0, 1), (0, 2),   # cannibals
            (1, 1)            # both
        ]

        for m, c in moves:
            if boat == 0:  # boat on left → move to right
                new_state = (m_left - m, c_left - c, 1)
            else:          # boat on right → move to left
                new_state = (m_left + m, c_left + c, 0)

            new_m_left, new_c_left, new_boat = new_state
            new_m_right = 3 - new_m_left
            new_c_right = 3 - new_c_left

            if is_valid(new_m_left, new_c_left, new_m_right, new_c_right):
                heapq.heappush(pq, (heuristic(new_state), new_state, path + [new_state]))

    print("No solution found.")

# -------- RUN --------
best_first_search()
