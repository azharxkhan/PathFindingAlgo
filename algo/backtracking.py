def is_safe(grid, x, y):
    # Check if (x, y) is within the bounds and not an obstacle
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1

def backtracking(grid, start, end):
    path = []
    if solve_backtracking(grid, start[0], start[1], end, path):
        return path
    return []  # Return an empty path if no solution is found

def solve_backtracking(grid, x, y, end, path):
    # Base case: if the end is reached, return True
    if (x, y) == end:
        path.append((x, y))
        return True

    # Check if the current position is valid
    if is_safe(grid, x, y):
        # Mark the current cell as part of the path
        path.append((x, y))

        # Try moving in each direction (right, down, left, up)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if solve_backtracking(grid, x + dx, y + dy, end, path):
                return True

        # Backtrack: remove the current cell from the path
        path.pop()

    return False
