def flood_fill(grid, start, fill_value=2):
    """
    Flood fill algorithm to fill a connected area in the grid starting from 'start'.

    Args:
        grid (list of list of int): The grid representing the space, where 0 means empty space and 1 means wall.
        start (tuple): The starting point (x, y) for the flood fill.
        fill_value (int): The value to fill the connected area with (default is 2).

    Returns:
        list of list of int: The grid with the filled area.
    """
    x, y = start
    if grid[x][y] != 0:  
        return grid

    stack = [start]
    original_value = grid[x][y]

    while stack:
        x, y = stack.pop()

        grid[x][y] = fill_value

        for nx, ny in get_neighbors((x, y), grid):
            if grid[nx][ny] == original_value:  
                stack.append((nx, ny))

    return grid

def get_neighbors(current_state, grid):
    neighbors = []
    x, y = current_state
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors