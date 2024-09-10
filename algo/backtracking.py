def is_safe(grid, x, y, visited):
    # Check if (x, y) is within the bounds, not an obstacle, and not visited
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and (x, y) not in visited

def backtracking(grid, start, end):
    path = []
    visited = set()  # Track visited cells
    if solve_backtracking(grid, start[0], start[1], end, path, visited):
        return path
    return []  # Return an empty path if no solution is found

def solve_backtracking(grid, x, y, end, path, visited):
    # Base case: if the end is reached, return True
    if (x, y) == end:
        path.append((x, y))
        return True

    # Check if the current position is valid and safe to move into
    if is_safe(grid, x, y, visited):
        # Mark the current cell as visited
        visited.add((x, y))

        # Mark the current cell as part of the path
        path.append((x, y))

        # Try moving in each direction (right, down, left, up)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if solve_backtracking(grid, x + dx, y + dy, end, path, visited):
                return True

        # Backtrack: remove the current cell from the path
        path.pop()

    return False
