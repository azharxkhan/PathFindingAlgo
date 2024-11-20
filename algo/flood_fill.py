def flood_fill(grid, start, end):
    """
    Flood fill algorithm to find a path from 'start' to 'end' in the grid.

    Args:
        grid (list of list of int): The grid representing the space, where 0 means empty space and 1 means wall.
        start (tuple): The starting point (x, y) for the flood fill.
        end (tuple): The ending point (x, y) to stop the flood fill.

    Returns:
        list of tuple: The path from start to end if reachable, otherwise an empty list.
    """
    x, y = start
    if grid[x][y] != 0:  
        return []

    stack = [start]
    path = []
    visited = set()

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        path.append(current)
        if current == end:
            return path

        for nx, ny in get_neighbors(current, grid):
            if (nx, ny) not in visited:  
                stack.append((nx, ny))

    return []  


def get_neighbors(current_state, grid):
    """
    Get valid neighbors of the current state within the grid.

    Args:
        current_state (tuple): The current position (x, y).
        grid (list of list of int): The grid representing the space.

    Returns:
        list of tuple: Valid neighbor positions.
    """
    neighbors = []
    x, y = current_state
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors
