import heapq

def heuristic(current_state, goal_state):
    x1, y1 = current_state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)

def get_neighbors(current_state, grid):
    neighbors = []
    x, y = current_state
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
            neighbors.append((nx, ny))
    return neighbors

def reconstruct_path(came_from, current_state):
    path = []
    while current_state in came_from:
        path.append(current_state)
        current_state = came_from[current_state]
    path.append(current_state)  # add the start state
    return path[::-1]

def a_star(grid):
    start_state = (1, 1)
    goal_state = (78, 38)
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, start_state))
    came_from = {}
    g_score = {start_state: 0}
    f_score = {start_state: heuristic(start_state, goal_state)}

    while open_set:
        _, current_state = heapq.heappop(open_set)

        if current_state == goal_state:
            return reconstruct_path(came_from, current_state)

        closed_set.add(current_state)

        for neighbor_state in get_neighbors(current_state, grid):
            if neighbor_state in closed_set:
                continue

            tentative_g_score = g_score[current_state] + 1

            if neighbor_state not in g_score or tentative_g_score < g_score[neighbor_state]:
                came_from[neighbor_state] = current_state
                g_score[neighbor_state] = tentative_g_score
                f_score[neighbor_state] = g_score[neighbor_state] + heuristic(neighbor_state, goal_state)
                heapq.heappush(open_set, (f_score[neighbor_state], neighbor_state))

    return []

