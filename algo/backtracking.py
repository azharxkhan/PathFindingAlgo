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


def backtracking(grid):
    start_state = (1, 1)
    goal_state = (78, 38)
    path = []

    def backtrack(x, y):
        if (x, y) == goal_state:
            return True
        if grid[x][y] == 0:
            return False

        grid[x][y] = 0  # mark as visited
        path.append((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if backtrack(x + dx, y + dy):
                return True

        path.pop()
        return False

    if backtrack(*start_state):
        return path
    return []


