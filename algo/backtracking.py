def is_safe(grid, x, y, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and (x, y) not in visited

def backtracking(grid, start, end):
    path = []
    visited = set()  
    if solve_backtracking(grid, start[0], start[1], end, path, visited):
        return path
    return []  

def solve_backtracking(grid, x, y, end, path, visited):
    if (x, y) == end:
        path.append((x, y))
        return True

    if is_safe(grid, x, y, visited):
        visited.add((x, y))

        path.append((x, y))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if solve_backtracking(grid, x + dx, y + dy, end, path, visited):
                return True

        path.pop()

    return False
