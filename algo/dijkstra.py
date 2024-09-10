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
    path.append(current_state)  
    return path[::-1]

def dijkstra(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    distance = {start: 0}

    while open_set:
        current_distance, current_state = heapq.heappop(open_set)

        if current_state == goal:
            return reconstruct_path(came_from, current_state)

        for neighbor_state in get_neighbors(current_state, grid):
            new_distance = current_distance + 1
            if neighbor_state not in distance or new_distance < distance[neighbor_state]:
                distance[neighbor_state] = new_distance
                came_from[neighbor_state] = current_state
                heapq.heappush(open_set, (new_distance, neighbor_state))

    return []
