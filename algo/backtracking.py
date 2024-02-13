import pygame

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set screen dimensions
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 40
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Backtracking Algorithm Visualization")
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

def draw_state(state, color):
    pygame.draw.rect(screen, color, (state[1] * CELL_SIZE, state[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def get_neighbors(current_state, grid):
    neighbors = []
    x, y = current_state
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors

def backtracking(current_state, grid):
    if current_state == goal_state:
        return True
    
    for neighbor_state in get_neighbors(current_state, grid):
        if grid[neighbor_state[0]][neighbor_state[1]] == 1:
            grid[neighbor_state[0]][neighbor_state[1]] = 2
            if backtracking(neighbor_state, grid):
                return True
            grid[neighbor_state[0]][neighbor_state[1]] = 1
        
        # Update visualization
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(WHITE)
        draw_grid()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    draw_state((row, col), BLACK)
                elif (row, col) == start_state:
                    draw_state((row, col), GREEN)
                elif (row, col) == goal_state:
                    draw_state((row, col), BLUE)
                elif grid[row][col] == 2:
                    draw_state((row, col), RED)
        pygame.display.update()
        clock.tick(30)
    
    return False

# Example usage:
grid = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

start_state = (0, 0)
goal_state = (5, 5)

path_found = backtracking(start_state, grid)

if path_found:
    print("Path found.")
else:
    print("No path found.")
